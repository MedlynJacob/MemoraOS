from utils.context_formatter import format_context
from prompts.prompt_generator import build_prompt
from retrieval.retrieval import retrieve
from llm.ollama_client import generate_response
from models.message import Message

def get_answer(query: str,history:list[Message]) -> str:
    retrieval_results = retrieve(query)

    context = format_context(retrieval_results)

    prompt= build_prompt(query, context, history)
    answer= generate_response(prompt)
    return answer