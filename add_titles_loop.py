# Имя пользователя
username = input('Имя пользователя: ')  # Переменная для имени пользователя

# Основная идея
titles1 = []  # Список для хранения заголовков основных идей
while True:  # Бесконечный цикл, до тех пор, пока не будет выполнено условие для выхода (if title1 == "":)
    title1 = input('Основные идеи (введите заголовок или оставьте пустым для завершения):  ')
    if title1 == "":
        break  # Прерываем цикл при выполненном условии if title1 == "": (пустое пространство - ввод)
    titles1.append(title1)  # Добавляем введенный заголовок title1 в список titles1 с помощью .append

# Заголовок
titles2 = []  # Список для хранения заголовков
while True:  # Бесконечный цикл до тех пор, пока не будет выполнено условие для выхода
    title2 = input('Список задач (введите заголовок или оставьте пустым для завершения): ')
    if title2 == "":
        break  # Прерываем цикл
    titles2.append(title2)  # Добавляем заголовок в список

# Описание и статус заметки
content = input('Описание заметки: ')  # Переменная для описания заметки
status = input('Статус заметки (В работе/Не в работе): ')  # Переменная для статуса заметки
# Дата начала задачи/дедлайн
created_date = input('Дата начала задачи (ДД/ММ/ГГГГ): ')  # Дата начала заметки (проекта)
issue_date = input('Дата завершения задачи (ДД/ММ/ГГГГ): ')  # Дедлайн

# Улучшение структуры хранения данных заметки в виде списка
note = [
        username,
        titles1,
        titles2,
        content,
        status,
        created_date,
        issue_date
        ]

# For run
print(f'Имя пользователя: {note[0]}') # Выводим введенное имя пользователя из списка
print('Заголовки основных идей:')
for title in note[1]:
    print(f'{title}')  # Выводим введенные заголовки идей ссылаясь на список (for title in note[1])

print('Заголовки списка задач:')
for title in note[2]:
    print(f'{title}')  # Выводим введенные заголовки задач ссылаясь на список (for title in note[2])

print(f'Описание заметки: {note[3]}')
print(f'Статус заметки: {note[4]}')
print(f'Дата начала задачи: {note[5][:5]}')
print(f'Дата завершения задачи: {note[6][:5]}')

print(note)