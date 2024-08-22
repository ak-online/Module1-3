def domain_check(recp,send):
    domain = [".com", ".ru", ".net"]
    res = True
    for k in domain:
        if k in recp and k in send:
            #print("K ", k, "есть домен.")
            break
        else:
            #print("K ", k, "нет такого домена.")
            res = False
    return res

# Создайте функцию send_email
def send_email(message, recipient,sender = "university.help@gmail.com"):
    if "@" not in sender and "@" not in recipient and not domain_check(recipient,sender):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    if recipient == sender:
        print("Невозможно отправить письмио с адреса", sender, "на адрес", recipient)
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса ", sender, "на адрес", recipient)
    else:
         print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
# end of send_email():

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')