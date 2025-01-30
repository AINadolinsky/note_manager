# Список для хранения заметок
notes = []

# Удаление заметки по "имя пользователя" или "наименование заголовка"
def delete_notes(notes):
    # Запрос критерия для удаления
    criterion = input('Введите критерий для удаления заметки (имя пользователя/наименование заголовка: ')
    if criterion == 'имя пользователя':
        username_to_delete = input('Введите имя пользователя, заметки которого хотите удалить: ')
        notes = [note for note in notes if note['username'] != username_to_delete]
        print(f'заметки с именем пользователя "{username_to_delete}" удалены')

    elif criterion ==  'заголовок':
        title_to_delete = input('Введите наименование заголовка, чтобы удалить заметку: ')
        notes = [
            note for note in notes if title_to_delete not in note['titles1'] or
            title_to_delete not in note['titles2']
        ]
        print(f'заметка с заголовком "{title_to_delete}" удалены')
    else:
        print('некорректный ввод, введите снова')
    return notes

while True:
    username = input('Имя пользователя: ')

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

    # Описание заметки
    content = input('Описание заметки: ')  # Переменная для описания заметки

    # Список возможных статусов
    statuses = ['в работе', 'не в работе', 'выполнено', 'отложено']

    # Запрос на ввод статуса заметки
    status = input('Статус заметки (в работе/не в работе/выполнено/отложено): ')

    # Проверка введенного статуса (status)
    while status not in statuses: # Если введенный статус не соответствует предложенным вариантам
        print('Некорректный ввод. Выберите один из предложенных статусов')
        status = input('Статус заметки (в работе/не в работе/выполнено/отложено): ')

    # Даем возможность изменить статус заметки, если предыдущее условие было выполнено
    while True:
        new_status = input(f'текущий статус: {status}. Желаете изменить? (да/нет): ')
        if new_status == 'да':
            while True:
                status = input(f'Выберите новый статус из предложенного: {", ".join(statuses)}: ')
                if status in statuses:
                    print(f'Статус обновлен на: {status}')
                    break
                else:
                    print('Некорректный ввод. Выберите один из предложенных статусов.')
            break # Завершаем цикл изменений статуса заметки
        elif new_status == 'нет':
            print(f'Статус остается: {status}')
            break
        else:
            print('Ответьте: да/нет')

    # Дата начала задачи/дедлайн
    from datetime import datetime

    # функция для проверки формата даты
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    created_date = input('Дата начала задачи (ДД/ММ/ГГГГ): ')

    # Проверка формата даты начало проекта
    while not is_valid_date(created_date):
        print('Некорректный формат даты. Введите дату в формате ДД/ММ/ГГГГ.')
        created_date = input('Дата начала задачи (ДД/ММ/ГГГГ): ')

    issue_date = input('Дата завершения задачи (ДД/ММ/ГГГГ): ')
    # Проверка формата даты начало проекта
    while not is_valid_date(issue_date):
        print('Некорректный формат даты. Введите дату в формате ДД/ММ/ГГГГ.')
        issue_date = input('Дата завершения задачи (ДД/ММ/ГГГГ): ')

    # Преобразуем строки с датами в объекты datetime
    created_date_obj = datetime.strptime(created_date, '%d/%m/%Y')
    issue_date_obj = datetime.strptime(issue_date, '%d/%m/%Y')

    # Получаем текущую дату
    current_date = datetime.now()

    # Выводим текущую дату
    print(f'Текущая дата: {current_date.strftime("%d/%m/%Y")}')

    # Проверка на истечение срока дедлайна
    if current_date > issue_date_obj:
        print('Дедлайн истек')
    else:
        remaining_days = (issue_date_obj - current_date).days
        if remaining_days == 0:
            print('Срок сдачи сегодня')
        else:
            print(f'До дедлайна осталось {remaining_days} дня(ей).')

    # Улучшение структуры хранения данных заметки в виде списка
    note = {'username': username,
            'titles1': titles1,
            'titles2': titles2,
            'content': content,
            'status': status,
            'created_date': created_date,
            'issue_date': issue_date}

    # добавляем заметку в список
    notes.append(note)

    # Запрос на добавление следующей заметки
    stop_input = input('Хотите добавить еще одну заметку? (да/нет): ')
    if stop_input == 'нет':
        break

# For run
print("\nВсе заметки:")
for i, note in enumerate(notes, start=1):
    print(f"\nЗаметка {i}:")
    print(f"Имя пользователя: {note['username']}")
    print('Заголовки основных идей:')
    for title in note['titles1']:
        print(f'{title}')
    print('Заголовки списка задач:')
    for title in note['titles2']:
        print(f'{title}')
    print(f'Описание заметки: {note["content"]}')
    print(f'Статус заметки: {note["status"]}')
    print(f'Дата начала задачи: {note["created_date"]}')
    print(f'Дата завершения задачи: {note["issue_date"]}')

# Возможность удаления заметок
notes = delete_notes(notes)

# Отображаем все оставшиеся заметки
print("\nОставшиеся заметки:")
for i, note in enumerate(notes, start=1):
    print(f"\nЗаметка {i}:")
    print(f"Имя пользователя: {note['username']}")
    print('Заголовки основных идей:')
    for title in note['titles1']:
        print(f'{title}')
    print('Заголовки списка задач:')
    for title in note['titles2']:
        print(f'{title}')
    print(f'Описание заметки: {note["content"]}')
    print(f'Статус заметки: {note["status"]}')
    print(f'Дата начала задачи: {note["created_date"]}')
    print(f'Дата завершения задачи: {note["issue_date"]}')
