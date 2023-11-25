import openai

# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = "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"


def chat_bot(prompt):
    # задаем модель и промпт
    model_engine = "text-davinci-003"


    # задаем макс кол-во слов
    max_tokens = 128

    # генерируем ответ
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # выводим ответ
    print(completion.choices[0].text)
    return completion.choices[0].text