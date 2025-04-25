import openai
from config import settings

openai.api_key = "your_openai_api_key"

def generate_threat_report(incident_details):
    prompt = f"""
    A potential cyberattack was detected with the following details:
    {incident_details}
    
    Generate a professional incident report summarizing key risks, likely causes, and recommended next steps.
    """
    
    response = openai.ChatCompletion.create(
        model=settings.LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
