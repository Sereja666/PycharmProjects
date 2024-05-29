import requests



#
# test = telegram_bot_sendtext("Testing Telegram bot")
# print(test)

# import requests
#
#
# def send_message_to_telegram_channel(bot_token, chat_id, message):
#    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
#    params = {
#       'chat_id': chat_id,
#       'text': message
#    }
#    response = requests.post(url, data=params)
#
#    if response.status_code == 200:
#       print("Сообщение успешно отправлено в канал Telegram!")
#    else:
#       print("Ошибка при отправке сообщения в канал Telegram.")
#
#
# # Пример использования функции
# bot_token = '7062504863:AAEN-z4DUGN3PfMVD5oIpRGVPlElKOWLOdw'
# chat_id = '-1002027147296'
# message = "тест!"