import requests
import prompts.story_prompts as p

def generate_response(topic, model="falcon", url='http://localhost:11434/api/generate', stream=False):
    prompt = p.create_story_prompt(topic)
    data = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json().get('response')
    else:
        return f"Error: Unable to generate a response. Status code: {response.status_code}"

