import json
from pprint import pprint
from typing import Callable


phonebook: str = 'Phonebook.json'
contacts: list[dict] = []

try:
    with open(phonebook, 'r', encoding='utf-8') as file_read:
        contacts = json.load(file_read)
except json.decoder.JSONDecodeError:
    print('Телефонная книга пустая, добавьте новый контакт')


def rewrite_file(phonebook: str) -> None:
    with open(phonebook, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)


def add_contact() -> None:
    first_name: str = input('\nВведите имя нового контакта: ').capitalize()
    last_name: str = input('Введите фамилию нового контакта: ').capitalize()
    telephone_number: str = input('Введите номер телефона: ')
    city: str = input('Введите город контакта: ').capitalize()
    new_contact: dict[str, str] = {
        'first name': first_name,
        'last name': last_name,
        'full name': first_name + ' ' + last_name,
        'telephone number': telephone_number,
        'city or state': city
    }
    contacts.append(new_contact)
    rewrite_file(phonebook)
    print(f'Контакт {telephone_number}  сохранён')


def find_contact() -> None:
    parameter: str = input('\nВыберите по какому параметру осуществить поиск:\n'
                     '1- поиск по имени\n'
                     '2- поиск по фамилии\n'
                     '3- поиск по полному имени\n'
                     '4- поиск по номеру телефона\n'
                     '5- поиск по городу\n'
                     'или "q" для выхода\n'
                     '->  ')
    if parameter == 'q':
        exit()
    parameter_dict: dict = {
        '1': 'first name',
        '2': 'last name',
        '3': 'full name',
        '4': 'telephone number',
        '5': 'city or state'
    }
    key = parameter_dict.get(parameter)

    search: str = input('Введите данные контакта для поиска, '
                   'или "q" для выхода: ').capitalize()
    if search == "Q":
        exit()
    else:
        for contact in contacts:
            if contact[key] == search:
                pprint(contact)
                return
        else:
            print('Контакт не найден, попробуйте снова')
            find_contact()


def edit_contact() -> None:
    print('\nНайдите контакт, который хотите откорректировать')
    search: str = input('Введите номер телефона для поиска, или "q" для выхода: ')
    if search == "Q":
        exit()
    else:
        for contact in contacts:
            if contact['telephone number'] == search:
                pprint(contact)
                parametr_dict: dict[str, str] = {
                    '1': 'first name',
                    '2': 'last name',
                    '3': 'telephone number',
                    '4': 'city or state'
                }
                key_choice: str = input('1- имя\n'
                                   '2- фамилия\n'
                                   '3- номер телефона\n'
                                   '4- город\n'
                                   'Выберите параметр, который хотите '
                                   'откорректировать:')
                key = parametr_dict.get(key_choice)
                contact[key] = input('Введите новое значение: ')
                rewrite_file(phonebook)
                print('изменения сохранены')
                return
        else:
            print('Контакт не найден, попробуйте снова')
            edit_contact()


def del_contact() -> None:
    number_for_del: str = input('Введите номер телефона для удаления, '
                           'или "q" для выхода: ')
    if number_for_del == 'q':
        exit()
    else:
        for contact in contacts:
            if contact['telephone number'] == number_for_del:
                contacts.remove(contact)
                rewrite_file(phonebook)
        else:
            print('Контакт не найден, попробуйте снова')
            del_contact()


phonebook_dict: dict[str, Callable[..., None]] = {'1': add_contact,
                  '2': find_contact,
                  '3': edit_contact,
                  '4': del_contact,
                  '5': exit}

while True:
    function_choice = input('\nВыберите команду для работы с телефонной '
                                 'книгой:\n'
                            '1 - добавить контакт\n'
                            '2 - найти контакт\n'
                            '3 - внести изменения\n'
                            '4 - удалить контакт\n'
                            '5 - выйти\n'
                            '-> ')
    phonebook_function = phonebook_dict.get(function_choice)
    if phonebook_function:
        phonebook_function()


