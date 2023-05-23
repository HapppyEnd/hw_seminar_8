import sys


def get_all_subscribers() -> list:
    """Возвращает список всех абонентов."""
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        subscribers_list = []
        for line in file.readlines():
            subscribers_list.append(line.replace('\n', ''))
        return subscribers_list


def print_all_subscribers(subscribers: list) -> list:
    """Выводит и возвращает список всех абонентов."""
    for subscriber in subscribers:
        print(subscriber)
    return subscribers


def add_new_person(subscribers: list) -> list:
    """Добавляет нового абонента."""
    values = ('Фамилию', 'Имя', 'Отчество', 'Номер телефона')
    result = ''
    for value in values:
        result += input(f'Введите {value}: ') + ' '
    subscribers.append(result + '\n')
    print('Ваша запись добавлена в справочник.')
    return subscribers


def find_info(subscribers: list) -> list:
    """Поиск абонента."""
    text = input('Введите фамилию или имя для поиска абонента: ')
    for line in subscribers:
        if (text.lower() == line.split()[0].lower()
                or text.lower() == line.split()[1].lower()):
            print(line)
    return subscribers


def all_commands() -> None:
    """Выводит список всех команд."""
    print('Что будем делать?')
    COMMANDS = [
        'add - добавить информацию',
        'find - найти информацию ',
        'show - показать весь список',
        'edit - редактировать информацию',
        'delete - удалить данные',
        'q - выход']
    for command in COMMANDS:
        print(f'\t {command}')


def delete_persone(subscribers: list) -> list:
    """Удаляет абонента из справочника."""
    text = input('Введите фамилию или имя для поиска абонента: ')
    for value in subscribers:
        if (text.lower() == value.split()[0].lower()
                or text.lower() == value.split()[1].lower()):
            subscribers.remove(value)
    return subscribers


def edit_info(subscribers: list) -> list:
    """Редактирует данные абонента."""
    subscribers = delete_persone(subscribers)
    subscribers = add_new_person(subscribers)
    return subscribers


def check_commands(text: str, subscribers: list) -> list:
    """Возвращает обработанный список после выполнения функции или
    текущий список, если команда не найдена."""
    CASES = {
        'show': print_all_subscribers,
        'add': add_new_person,
        'find': find_info,
        'edit': edit_info,
        'delete': delete_persone,
        'q': exit,
    }
    if text in CASES:
        return CASES[text](subscribers)
    else:
        print('Такой команды нет. Попробуйте снова.')
        return subscribers


def exit(subscribers: list) -> None:
    """Сохраняет все изменения в файл и завершает работу программы."""
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        for subscriber in subscribers:
            file.write(f'{subscriber}\n')
    sys.exit('До новых встреч.')


def main() -> None:
    all_commands()
    subscribers = get_all_subscribers()
    while True:
        text = input('Введите команду: ')
        subscribers = check_commands(text, subscribers)


if __name__ == '__main__':
    main()
