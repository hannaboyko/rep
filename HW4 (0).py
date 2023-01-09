password = input('Введите пароль:')
digits = '1234567890'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
symbols = '!@#$%^&*()-+'
acceptable = digits + upper_letters + lower_letters + symbols

passwd = list(password)
if any(char not in acceptable for char in passwd):
    print('Ошибка. Запрещенный спецсимвол')
else:
    recommendations = []
    if len(password) < 12:
        recommendations.append(f'увеличить число символов - {12 - len(password)}')
    for value, message in ((digits, 'цифру'),
                          (symbols, 'спецсимвол'),
                          (upper_letters, 'заглавную букву'),
                          (lower_letters, 'строчную букву')):
        if all(char not in value for char in passwd):
            recommendations.append(f'добавить  {message}')

    if recommendations:
        print("Слабый пароль. Рекомендации:", ", ".join(recommendations))
    else:
        print('Сильный пароль.')
