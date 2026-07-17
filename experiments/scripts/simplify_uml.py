#!/usr/bin/env python3
"""
simplify_uml.py --> normalizzare la sintassi del diagramma, senza modificarne il significato.

Converte JSON UML esportati dall'app/draw.io in JSON semplificati per test LLM.

Mantiene:
- classi
- attributi
- metodi, opzionali
- associazioni
- ereditarietà
- molteplicità
- ruoli, se presenti
- sinonimi e pesi, se il file contiene una sezione "reference"

Elimina:
- coordinate grafiche
- bounds
- path
- UUID interni non necessari
- elementi grafici non UML
- legenda/colori
- dati di layout

Uso:
    python simplify_uml.py input.json output_clean.json

Oppure su una cartella:
    python simplify_uml.py experiments/raw experiments/data/esercizio_01 --batch
"""

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


CLASS_TYPES = {"Class"}
ATTRIBUTE_TYPES = {"ClassAttribute"}
METHOD_TYPES = {"ClassMethod"}
IGNORED_ELEMENT_TYPES = {"ColorLegend"}


def normalize_text(value: Optional[str]) -> str:
    """Normalizza spazi e rimuove caratteri invisibili."""
    if value is None:
        return ""
    value = str(value).strip()
    value = re.sub(r"\s+", " ", value)
    return value


def clean_attribute_name(raw_name: str) -> Dict[str, Any]:
    """
    Pulisce attributi del tipo:
    '+ nome: String'
    '- password: String'
    '+tipo_evento : enum'

    Restituisce:
    {
      "name": "nome",
      "visibility": "+",
      "type": "String"
    }
    """
    text = normalize_text(raw_name)

    visibility = ""
    if text.startswith(("+", "-", "#", "~")):
        visibility = text[0]
        text = text[1:].strip()

    attr_type = ""
    if ":" in text:
        left, right = text.split(":", 1)
        name = left.strip()
        attr_type = right.strip()
    else:
        name = text.strip()

    return {
        "name": name,
        "visibility": visibility,
        "type": attr_type
    }


def get_elements_container(data: Dict[str, Any]) -> Any:
    """
    Gestisce due possibili formati:
    1. data["elements"] come lista
    2. data["model"]["elements"] come dizionario
    """
    if "elements" in data:
        return data["elements"]

    if "model" in data and isinstance(data["model"], dict) and "elements" in data["model"]:
        return data["model"]["elements"]

    return []


def get_relationships_container(data: Dict[str, Any]) -> Any:
    """
    Gestisce due possibili formati:
    1. data["relationships"] come lista
    2. data["model"]["relationships"] come dizionario
    """
    if "relationships" in data:
        return data["relationships"]

    if "model" in data and isinstance(data["model"], dict) and "relationships" in data["model"]:
        return data["model"]["relationships"]

    return []


def container_to_list(container: Any) -> List[Dict[str, Any]]:
    """Converte lista o dizionario di elementi in lista."""
    if isinstance(container, list):
        return [x for x in container if isinstance(x, dict)]
    if isinstance(container, dict):
        return [x for x in container.values() if isinstance(x, dict)]
    return []


def extract_reference_if_present(data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Se il file contiene una sezione 'reference', la semplifica separatamente.
    Utile per le soluzioni ufficiali già annotate con classi, sinonimi, pesi e associazioni.
    """
    reference = data.get("reference")
    if not isinstance(reference, dict):
        return None

    classes = []
    for cls in reference.get("classes", []):
        if not isinstance(cls, dict):
            continue

        attributes = []
        for attr in cls.get("attributes", []):
            if not isinstance(attr, dict):
                continue

            attributes.append({
                "name": normalize_text(attr.get("name")),
                "synonyms": attr.get("synonyms", []),
                "types": attr.get("types", []),
                "weight": normalize_text(attr.get("weight")),
                "allowsForeignKeyName": bool(attr.get("allowsForeignKeyName", False))
            })

        classes.append({
            "name": normalize_text(cls.get("name")),
            "synonyms": cls.get("synonyms", []),
            "weight": normalize_text(cls.get("weight")),
            "attributes": attributes,
            "forbiddenAttributes": cls.get("forbiddenAttributes", [])
        })

    associations = []
    for assoc in reference.get("associations", []):
        if not isinstance(assoc, dict):
            continue

        source = assoc.get("source", {}) or {}
        target = assoc.get("target", {}) or {}

        source_class = source.get("referenceClass", {}) or {}
        target_class = target.get("referenceClass", {}) or {}

        associations.append({
            "type": normalize_text(assoc.get("type")),
            "name": normalize_text(assoc.get("name")),
            "source": normalize_text(source_class.get("name")),
            "target": normalize_text(target_class.get("name")),
            "sourceMultiplicity": source.get("multiplicities", []),
            "targetMultiplicity": target.get("multiplicities", []),
            "sourceRole": normalize_text(source.get("role")),
            "targetRole": normalize_text(target.get("role")),
            "weight": normalize_text(assoc.get("weight"))
        })

    return {
        "classes": classes,
        "associations": associations,
        "forbiddenClasses": reference.get("forbiddenClasses", []),
        "forbiddenAssociations": reference.get("forbiddenAssociations", [])
    }


def simplify_model(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Semplifica un diagramma UML dal formato grafico.
    Risolve gli UUID delle relazioni sostituendoli con i nomi delle classi.
    """
    elements = container_to_list(get_elements_container(data))
    relationships_raw = container_to_list(get_relationships_container(data))

    element_by_id: Dict[str, Dict[str, Any]] = {}
    class_by_id: Dict[str, Dict[str, Any]] = {}
    attributes_by_owner: Dict[str, List[Dict[str, Any]]] = {}
    methods_by_owner: Dict[str, List[str]] = {}

    for el in elements:
        el_id = el.get("id")
        if el_id:
            element_by_id[el_id] = el

    for el in elements:
        el_type = el.get("type")
        el_id = el.get("id")

        if not el_id:
            continue

        if el_type in CLASS_TYPES:
            name = normalize_text(el.get("name"))
            if name:
                class_by_id[el_id] = el

        elif el_type in ATTRIBUTE_TYPES:
            owner = el.get("owner")
            name = normalize_text(el.get("name"))
            if owner and name:
                attributes_by_owner.setdefault(owner, []).append(clean_attribute_name(name))

        elif el_type in METHOD_TYPES:
            owner = el.get("owner")
            name = normalize_text(el.get("name"))
            if owner and name:
                methods_by_owner.setdefault(owner, []).append(name)

    classes = []
    for class_id, cls in class_by_id.items():
        class_name = normalize_text(cls.get("name"))

        attributes = attributes_by_owner.get(class_id, [])

        # fallback: se gli attributi sono referenziati nella classe ma non già raccolti
        if not attributes:
            for attr_id in cls.get("attributes", []):
                attr_el = element_by_id.get(attr_id)
                if attr_el and attr_el.get("type") in ATTRIBUTE_TYPES:
                    attr_name = normalize_text(attr_el.get("name"))
                    if attr_name:
                        attributes.append(clean_attribute_name(attr_name))

        methods = methods_by_owner.get(class_id, [])
        if not methods:
            for method_id in cls.get("methods", []):
                method_el = element_by_id.get(method_id)
                if method_el and method_el.get("type") in METHOD_TYPES:
                    method_name = normalize_text(method_el.get("name"))
                    if method_name:
                        methods.append(method_name)

        classes.append({
            "name": class_name,
            "attributes": attributes,
            "methods": methods
        })

    associations = []
    inheritance = []

    for rel in relationships_raw:
        rel_type = normalize_text(rel.get("type"))
        name = normalize_text(rel.get("name"))

        source = rel.get("source", {}) or {}
        target = rel.get("target", {}) or {}

        source_id = source.get("element")
        target_id = target.get("element")

        source_name = normalize_text(class_by_id.get(source_id, {}).get("name"))
        target_name = normalize_text(class_by_id.get(target_id, {}).get("name"))

        # ignora relazioni verso elementi non classe, es. ColorLegend
        if not source_name or not target_name:
            continue

        item = {
            "type": "Inheritance" if rel_type == "ClassInheritance" else "Association",
            "name": name,
            "source": source_name,
            "target": target_name,
            "sourceMultiplicity": normalize_text(source.get("multiplicity")),
            "targetMultiplicity": normalize_text(target.get("multiplicity")),
            "sourceRole": normalize_text(source.get("role")),
            "targetRole": normalize_text(target.get("role"))
        }

        if rel_type == "ClassInheritance":
            inheritance.append({
                "child": source_name,
                "parent": target_name
            })
        else:
            associations.append(item)

    simplified = {
        "diagramType": normalize_text(data.get("type", "ClassDiagram")),
        "classes": sorted(classes, key=lambda x: x["name"].lower()),
        "associations": sorted(associations, key=lambda x: (x["source"].lower(), x["target"].lower())),
        "inheritance": sorted(inheritance, key=lambda x: (x["child"].lower(), x["parent"].lower()))
    }

    reference = extract_reference_if_present(data)
    if reference is not None:
        simplified["reference"] = reference

    return simplified


def simplify_file(input_path: Path, output_path: Path) -> None:
    with input_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    simplified = simplify_model(data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(simplified, f, indent=2, ensure_ascii=False)

    print(f"Creato: {output_path}")


def simplify_batch(input_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    json_files = sorted(input_dir.glob("*.json"))
    if not json_files:
        print(f"Nessun file .json trovato in {input_dir}")
        return

    for input_file in json_files:
        output_file = output_dir / f"{input_file.stem}_clean.json"
        simplify_file(input_file, output_file)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Semplifica JSON UML eliminando dati grafici e mantenendo solo informazioni utili alla valutazione."
    )
    parser.add_argument("input", help="File JSON di input oppure cartella di input con --batch")
    parser.add_argument("output", help="File JSON di output oppure cartella di output con --batch")
    parser.add_argument("--batch", action="store_true", help="Elabora tutti i .json presenti nella cartella di input")

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if args.batch:
        simplify_batch(input_path, output_path)
    else:
        simplify_file(input_path, output_path)


if __name__ == "__main__":
    main()
