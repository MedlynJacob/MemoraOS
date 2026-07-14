from prompts.prompt_generator import build_prompt
from retrieval.retrieval import retrieve
from llm.ollama_client import generate_response
from models.message import Message

def get_answer(query: str,history:list[Message]) -> str:
    context= retrieve(query)
    prompt= build_prompt(query, context, history)
    answer= generate_response(prompt)
    print("\nRetrieved Context")
    print("=" * 40)
    print(context)
    print("=" * 40)
    return answer