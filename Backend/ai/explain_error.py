import openai
openai.api_key = "YOUR_OPENAI_API_KEY"

def explain_error(error_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Explain this error: {error_text}"}]
    )
    return response.choices[0].message.content
