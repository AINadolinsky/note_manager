# Creating variables
username = input('Имя пользователя: ') # Переменная для имени пользователя
title1 = input('Завязка: ') # Переменная для заголовка заметки
title2 = input('Кульминация: ') # Переменная для заголовка заметки
title3 = input('Развязка: ') # Переменная для заголовка заметки
titles = [title1, title2, title3]
content = input('Описание заметки: ') # Переменная для описания заметки
status = input('Статус заметки (В работе/Не в работе): ') # Переменная для статуса заметки
created_date = input('Дата начала задачи (ДД/ММ/ГГГГ): ') # Дата начала заметки
issue_date = input('Дата завершения задачи (ДД/ММ/ГГГГ): ') # Дедлайн

# Улучшение структуры хранения данных заметки в виде списка
note = [username,
        [titles],
        content,
        status,
        created_date,
        issue_date
        ]

# For run
print('Имя пользователя: '+ username + ", username")
print('Заголовок заметки: '+ str(titles) + ', ' + 'title')
print('Описание заметки: '+ content + ', ' + 'content')
print('Статус заметки: '+ status + ', ' + 'status')
print('Дата создания: '+ created_date[0:5] + ', ' + 'created_date')
print('Дата завершения: '+ issue_date[0:5] + ', ' + 'issue_date')

print(note)