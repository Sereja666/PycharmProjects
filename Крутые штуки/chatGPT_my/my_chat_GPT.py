import g4f


def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=messages
    )
    print(response)
    return response


messages = []
while True:
    messages.append({'role': 'user', 'content': input('-> ')})
    messages.append({'role': 'assistant', 'content': ask_gpt(messages=messages)})
