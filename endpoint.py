import requests

URL = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
}



def chat(prompt,max_tokens=200):
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a kind helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
        "max_tokens": max_tokens,
    }

    response = requests.post(URL, headers=headers, json=data)
    response_data = response.json()
    

   
    
    return response_data['choices'][0]['message']['content']



while True:
    user_prompt = input("user : ")
    response = chat(user_prompt)
    print("ChatGPT:", response)