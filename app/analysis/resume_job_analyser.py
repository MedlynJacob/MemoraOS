from analysis.resume_matcher import get_resume_and_jd
from utils.context_formatter import format_context
from prompts.resume_analysis_prompt import build_resume_analysis_prompt
from llm.ollama_client import generate_response

def analyze_resume(company: str)->str:
    resume_results,job_results=get_resume_and_jd(company)
    resume_context=format_context(resume_results)
    job_context=format_context(job_results)
    prompt=build_resume_analysis_prompt(resume_context, job_context)
    analysis= generate_response(prompt)
    return analysis
