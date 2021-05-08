documents = [
    {"type": "passport", "number": "2207 876234", "name": "Leia Organa"},
    {"type": "invoice", "number": "11-2", "name": "Anakin Skywalker"},
    {"type": "insurance", "number": "10006", "name": "Han Solo"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def show_commands():
    commands = [
        'p – выводит имя человека по номеру документа',
        's - выводит номер полки на которой хранится документ по его номеру',
        'l - выводит список всех документов',
        'a - добавление нового документа в каталог и перечень полок',
        'd - удаление записи из базы по номеру документа',
        'm - перемещение документа на новую полку',
        'as - добавление новой полки',
        'h - выводит список всех доступных команд',
        'x - закончить работу с программой'
    ]
    return commands

def get_name_by_document_number(document_number):
    doc_info = [item for item in documents if item['number'] == document_number]
    return doc_info[0]['name'] if doc_info else f"no document #{document_number} in base"

def get_shelf_by_document_number(document_number):
    shelf_number = [shelf for shelf, values in directories.items() if document_number in values]
    return f"document #{document_number} stored on shelf#{shelf_number[0]}" if shelf_number \
        else f"no document #{document_number} in base"

def show_all_documents():
    return [' '.join(item.values()) for item in documents]

def add_new_shelf(shelf_number=''):
    if not shelf_number:
        shelf_number = input('Введите номер полки: ')

    if shelf_number not in directories.keys():
        directories[shelf_number] = []
        return shelf_number, True
    return shelf_number, False

def append_document_to_shelf(document_number, shelf_number):
    add_new_shelf(shelf_number)
    directories[shelf_number].append(document_number)

def add_new_document(document_number, document_type, name, shelf):
    documents.append(dict(type=document_type, number=document_number, name=name))
    append_document_to_shelf(document_number, shelf)
    return shelf

def remove_document_from_shelf(document_number):
    documents_list = [documents_list for documents_list in directories.values() if document_number in documents_list]
    documents_list[0].remove(document_number)

def remove_document(document_number):
    documents_row_index = [index for index, item in enumerate(documents) if item['number'] == document_number]
    if documents_row_index:
        del documents[documents_row_index[0]]
        remove_document_from_shelf(document_number)
        return document_number, True

def move_document(document_number, shelf_number):
    remove_document_from_shelf(document_number)
    append_document_to_shelf(document_number, shelf_number)

def main():
    print("Делопроизводство версия 0.1")
    print("введите 'h' что бы получить список всех доступных команд\n")

    while True:
        command = input('введите команду: ')

        if command in ('h', 'p', 's', 'l', 'a', 'd', 'm', 'as', 'x'):

            if command == 'h':
                print("Cписок всех доступных комманд: \n")
                print(*show_commands(), sep='\n')
                print()

            elif command == 'p':
                print("\nПоиск имени по номеру документа.")
                document_number = input("введите номер: ")
                print(get_name_by_document_number(document_number), '\n')

            elif command == 's':
                print("\nПоиск полки по номеру документа.")
                document_number = input("введите номер документа: ")
                print(get_shelf_by_document_number(document_number), '\n')

            elif command == 'l':
                print('\nСписок всех документов:')
                print(*show_all_documents(), sep='\n')
                print()

            elif command == 'a':
                print("\nДобавление нового документа:")
                document_number = input("номер документа: ")
                document_type = input("тип документа: ")
                name = input("имя владельца: ")
                shelf = input("номер полки: ")
                result = add_new_document(document_number, document_type, name, shelf)
                print(f"{document_number} добавлен на полку {result}")

            elif command == 'd':
                print("\nУдаление документа:")
                document_number = input("номер документа: ")
                remove_document(document_number)
                print(f"{document_number} удален\n")

            elif command == 'm':
                print('\nПеремещение документа на другую полку:')
                document_number = input('Введите номер документа: ')
                shelf_number = input('Введите номер полки для перемещения: ')
                move_document(document_number, shelf_number)
                print(f"{document_number} премещен на полку {shelf_number}")

            elif command == 'as':
                print('\nДобавление новой полки:')
                print(add_new_shelf())

            elif command == 'x':
                break

        else:
            print('введена несуществующая команда')
            print("введите 'h' что бы получить список всех доступных команд\n")


if __name__ == "__main__":
    main()