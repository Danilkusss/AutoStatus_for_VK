import vk_api
import time


texts = ["i'm good", "Nice", "я люблю кушать", "блин,этот статус меняется каждые 30 секунд",
         "я крутой)", "черттт,я программист", "обнови страничку и посмотри снова на стутс)", "жизнь так прекрасна)"
                                                                                             "если вы это видите,"
                                                                                         "значит мой комп "
                                                                                             "включен)"]
i = 1

result = input("ты хочешь запустить авто статус? ")

if result == "да":
    vk_session = vk_api.VkApi('Login', 'pass')
    vk_session.auth()
    i = 1
    vk = vk_session.get_api()

    try:
        while True:
            for text in texts:
                i = i + 1
                print("статус приянт успешно,начинаме смену задоного статуса")
                time.sleep(3)
                print("статус сменился на: ", text)
                print("количество изменений прошло: ", i)
                vk.status.set(text=text)
                time.sleep(27)
    except vk_api.exceptions.Captcha as captcha:
        captcha.sid  # Получение sid
        captcha.get_url()  # Получить ссылку на изображение капчи
        captcha.get_image()



    # while True:
    #     for text in texts:
    #         i = i + 1
    #         print("статус приянт успешно,начинаме смену задоного статуса")
    #         time.sleep(3)
    #         print("статус сменился на: ", text)
    #         print("количество изменений прошло: ", i)
    #         vk.status.set(text=text)
    #         time.sleep(27)


else:
    print("завершение")


# vk_session = vk_api.VkApi('', '')
# vk_session.auth()
#
# vk = vk_session.get_api()
#
# while True:
#     for text in texts:
#         vk.status.set(text=text)
#         time.sleep(30)
