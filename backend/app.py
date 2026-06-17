from flask import Flask, request, jsonify
from flask_cors import CORS

from database.db import engine, get_session
from database.models import (
    Base,
    Esercizio,
    ProvaStudente
)
app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return "Backend Flask attivo!"


# =========================
# CREA ESERCIZIO
# =========================
@app.route("/esercizi", methods=["POST"])
def crea_esercizio():

    data = request.json

    session = get_session()

    nuovo_esercizio = Esercizio(
        titolo=data["titolo"],
        testo=data["testo"],
        soluzione_json=data["soluzione_json"]
    )

    session.add(nuovo_esercizio)

    session.commit()

    return jsonify({
        "message": "Esercizio salvato correttamente"
    })


# =========================
# OTTIENI TUTTI GLI ESERCIZI
# =========================
@app.route("/esercizi", methods=["GET"])
def get_esercizi():

    session = get_session()

    esercizi = session.query(Esercizio).all()

    result = []

    for esercizio in esercizi:

        result.append({
            "id": esercizio.id,
            "titolo": esercizio.titolo,
            "testo": esercizio.testo,
            "soluzione_json": esercizio.soluzione_json
        })

    return jsonify(result)

@app.route("/prove_studenti", methods=["POST"])
def salva_prova_studente():

    data = request.json

    session = get_session()

    nuova_prova = ProvaStudente(

        id_esercizio=data["id_esercizio"],

        nome_file=data["nome_file"],

        contenuto_json=data["contenuto_json"],

        valutazione_ai=""
    )

    session.add(nuova_prova)

    session.commit()

    return jsonify({
        "message": "Prova studente salvata"
    })

@app.route("/prove_studenti/<int:id_esercizio>", methods=["GET"])
def get_prove_studenti(id_esercizio):

    session = get_session()

    prove = session.query(ProvaStudente).filter_by(
        id_esercizio=id_esercizio
    ).all()

    result = []

    for prova in prove:

        result.append({

            "id": prova.id,

            "nome_file": prova.nome_file,

            "contenuto_json": prova.contenuto_json,

            "valutazione_ai": prova.valutazione_ai

        })

    return jsonify(result)

# =========================
# OTTIENI UN SINGOLO ESERCIZIO
# =========================
@app.route("/esercizi/<int:id>", methods=["GET"])
def get_esercizio(id):

    session = get_session()

    esercizio = session.query(Esercizio).get(id)

    if not esercizio:

        return jsonify({
            "error": "Esercizio non trovato"
        }), 404

    return jsonify({
        "id": esercizio.id,
        "titolo": esercizio.titolo,
        "testo": esercizio.testo,
        "soluzione_json": esercizio.soluzione_json
    })


if __name__ == "__main__":

    Base.metadata.create_all(engine)

    app.run(debug=True)