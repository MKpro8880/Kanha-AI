from core.llm_engine.ollama_runner import ask_llm

def load_prompt():
    with open("core/personality/kanha_prompt.txt", "r") as f:
        return f.read()

def kanha_think(user_input):
    system_prompt = load_prompt()
    final_prompt = f"""
{system_prompt}

User: {user_input}
Kanha:
"""
    return ask_llm(final_prompt)