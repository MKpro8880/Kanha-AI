import subprocess

def ask_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "phi3"],
            input=prompt,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"LLM Error: {e}"