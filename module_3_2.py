def send_email(message, recipient, sender ='university.help@gmail.com'):
    endings = ['.ru', '.com', '.net']

    outcome_msgs = {
        'error_message': 'Невозможно отправить письмо с адреса ' + sender + ' на адрес ' + recipient,
        'error_message1':  'Невозможно отправить письмо самому себе!',
        'success_message': 'Письмо успешно отправлено с адреса ' + sender + ' на адрес ' + recipient,
        'success_message_unusual': 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ' + sender + ' на адрес ' + recipient
    }


    if '@' in sender and '@' in recipient:
        if '.' in recipient and '.' in sender:
            send_dot = sender.rindex('.')
            recip_dot = recipient.rindex('.')
            if sender[send_dot::] in endings and recipient[recip_dot::] in endings:
                if sender == recipient:
                    print(outcome_msgs['error_message1'])
                elif sender == 'university.help@gmail.com':
                    print(outcome_msgs['success_message'])
                else:
                    print(outcome_msgs['success_message_unusual'])
            else:
                print(outcome_msgs['error_message'])
        else:
            print(outcome_msgs['error_message'])
    else:
        print(outcome_msgs['error_message'])

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')