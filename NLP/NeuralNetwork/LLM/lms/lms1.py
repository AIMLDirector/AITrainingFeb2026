import lmstudio as lms

with lms.Client() as client:
    model = client.llm.model("gemma-3-4b-it-qat")
    result = model.respond("Who are you, and what can you do?")
    print(result)