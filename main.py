import openai

openai.api_key = "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"

messages = [
    {
        "role": "system", "content": "You are a kind helpful assistant."},
]
while True:
    message = input('user : ')
    if message:
        messages.append(
            {"role":"user","content":message}
            )
        chat = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',messages=messages
        )

    reply = chat['choices'][0]['message']['content']
    print(f"ChatGPT: {reply}")
    messages.append({"role":"assistant","content":reply})


    if message in ['exit','quit']:
        break