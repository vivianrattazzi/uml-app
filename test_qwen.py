from llama_cpp import Llama

MODEL_PATH = "/home/vrattazzi/models/qwen25-coder/qwen2.5-coder-7b-instruct-q4_k_m.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_gpu_layers=-1,
    n_ctx=2048,
    n_threads=4,
    verbose=True
)

response = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "Rispondi in italiano in modo sintetico."},
        {"role": "user", "content": "Cos'è una classe in un diagramma UML?"}
    ],
    temperature=0.1,
    max_tokens=200
)

print(response["choices"][0]["message"]["content"])
