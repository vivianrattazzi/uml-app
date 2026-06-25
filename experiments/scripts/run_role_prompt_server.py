import json
import requests
from pathlib import Path

BASE_URL = "http://127.0.0.1:8080/v1/chat/completions"

SOLUTION_FILE = Path("experiments/data/esercizio_01/20240701_soluzione_clean.json")
STUDENT_FILE = Path("experiments/data/esercizio_01/s292503_clean.json")
PROMPT_FILE = Path("experiments/prompts/role_prompt.txt")
RESULT_FILE = Path("experiments/results/role_result_s292503.txt")

solution_json = json.dumps(
    json.load(open(SOLUTION_FILE, encoding="utf-8")),
    ensure_ascii=False,
    indent=2
)

student_json = json.dumps(
    json.load(open(STUDENT_FILE, encoding="utf-8")),
    ensure_ascii=False,
    indent=2
)

prompt_template = open(PROMPT_FILE, encoding="utf-8").read()

prompt = prompt_template.replace("{solution_json}", solution_json)
prompt = prompt.replace("{student_json}", student_json)

payload = {
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0.1,
    "max_tokens": 150,
    "stream": False
}
print("Lunghezza prompt:", len(prompt))
print(prompt[:1000])
response = requests.post(BASE_URL, json=payload, timeout=120)
response.raise_for_status()

output = response.json()["choices"][0]["message"]["content"]

print(output)

RESULT_FILE.parent.mkdir(parents=True, exist_ok=True)
RESULT_FILE.write_text(output, encoding="utf-8")

print(f"\nRisultato salvato in: {RESULT_FILE}")