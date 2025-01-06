# Creating variables
username = input('Имя пользователя: ') # Переменная для имени пользователя
title = input('Наименование заголовка: ') # Переменная для заголовка заметки
content = input('Описание заметки: ') # Переменная для описания заметки
status = input('Статус заметки (В работе/Не в работе): ') # Переменная для статуса заметки
created_date = input('Дата начала задачи (ДД/ММ): ') # Дата начала заметки
issue_date = input('Дата завершения задачи (ДД/ММ): ') # Дедлайн

# For run
print('Имя пользователя: '+ username + ", username")
print('Заголовок заметки: '+ title + ', ' + 'title')
print('Описание заметки: '+ content + ', ' + 'content')
print('Статус заметки: '+ status + ', ' + 'status')
print('Дата создания: '+ created_date[0:5] + ', ' + 'created_date')
print('Дата завершения: '+ issue_date[0:5] + ', ' + 'issue_date')

