from prompts.prompt_generator import build_prompt
from retrieval.retrieval import retrieve
from llm.ollama_client import generate_response


def get_answer(query: str) -> str:
    context= retrieve(query)
    prompt= build_prompt(query, context)
    answer= generate_response(prompt)
    return answer