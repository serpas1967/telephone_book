""" Реализовать телефонный справочник со следующими возможностями:
1.  Вывод постранично записей из справочника на экран
2.  Добавление новой записи в справочник
3.  Возможность редактирования записей в справочнике
4.  Поиск записей по одной или нескольким характеристикам

Требования к программе:
1.                   Реализация интерфейса через консоль (без веб- или графического интерфейса)
2.                   Хранение данных должно быть организовано в виде текстового файла, формат которого придумывает сам программист
3.                   В справочнике хранится следующая информация: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)"""


import os
import csv

# # Вывод меню выбора
# def display():
#     print("Телефонный справочник")
#     print("1. Вывод записей")
#     print("2. Добавление записи")
#     print("3. Редактирование записи")
#     print("4. Поиск записей")
#     print("5. Выход")
#     choice = input("Выберите пункт меню: ")
#
#     if choice == "1":
#         display_entries()
#     elif choice == "2":
#         add_entry()
#     elif choice == "3":
#         edit_entry()
#     elif choice == "4":
#         search_entries()
#     elif choice == "5":
#         exit()
#     else:
#         print("Некорректный выбор. Попробуйте снова.")

# Функция для вывода меню и обработки выбранного пункта
def menu():
    print("Телефонный справочник")
    print("1. Вывод записей")
    print("2. Добавление записи")
    print("3. Редактирование записи")
    print("4. Поиск записей")
    print("5. Выход")
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        display_entries()
    elif choice == "2":
        add_entry()
    elif choice == "3":
        edit_entry()
    elif choice == "4":
        search_entries()
    elif choice == "5":
        exit()
    else:
        print("Некорректный выбор. Попробуйте снова.")
    # display()
    menu()

# Функция для вывода записей из справочника
def display_entries():
    with open("data/телеф.справочник.txt", "r", encoding='cp1251') as file:
        #lines = file.readlines()
        file_reader = csv.reader(file, delimiter=",")
        # if len(lines) > 0:
        #     print("Записи в справочнике:")
        count = 0
        for entry in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Справочник содержит столбцы: \n{",       ".join(entry)}')
           # entry = line.split(", ")
            else:
                #print(f"Фамилия: {entry[0]}, Имя: {entry[1]}, Отчество: {entry[2]}, Организация: {entry[3]}, Рабочий телефон: {entry[4]}, Личный телефон: {entry[5]}")
                print(f" {count}. {entry[0]},  {entry[1]},  {entry[2]},  {entry[3]},  {entry[4]},  {entry[5]}")
                # print("Имя:", entry[1])
                # print("Отчество:", entry[2])
                # print("Организация:", entry[3])
                # print("Рабочий телефон:", entry[4])
                # print("Личный телефон:", entry[5])
                print("--------------------------------------------------------------------------")
            count += 1
        # menu()
        # else:
        #     print("Справочник пуст.")
        comm = input("для выхода из текущего режима введите * \n")
        if comm == "*":
            return

# Функция для добавления новой записи в справочник
def add_entry():
    entry_list = []
    comm = ""
    while comm != "*":
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        organization = input("Введите название организации: ")
        work_phone = input("Введите рабочий телефон: ")
        work_phone = "".join([fig for fig in work_phone if fig in "0123456789"])
        personal_phone = input("Введите личный телефон: ")
        personal_phone = "".join([fig for fig in personal_phone if fig in "0123456789"])

        entry = [last_name, first_name, middle_name, organization, work_phone, personal_phone]
        #entry = ", ".join([last_name,first_name,middle_name,organization,work_phone,personal_phone,"\n"])
        #entry = f"{last_name},{first_name},{middle_name},{organization},{work_phone},{personal_phone}\n"
        entry_list.append(entry)
        print("entry_list", entry_list)
        print("Запись успешно добавлена.")

        comm = input("Чтобы выйти из режима ввода записей введите *  , чтобы продолжть нажмите любой другой символ ")
    # if comm == "*":
        with open("data/телеф.справочник.txt", "a", encoding='cp1251') as file:
            file_writer = csv.writer(file, delimiter=",")
            [file_writer.writerow(entry) for entry in entry_list]
            #for entry in entry_list:
                #file.write(entry)
        return

def search_entries():
    info_to_find = input("Введите через пробел какие-либо поля записи(фамилия, имя, отчество, "
                    "название организации, телефон рабочий, телефон личный (сотовый)), "
                    "которую хотите найти ").split()
    info_to_find_dict = {word.strip() for word in info_to_find}
    #info_to_find_dict = {"".join([fig for fig in info_to_find_dict if fig in "0123456789"])}
    result = []
    with open("data/телеф.справочник.txt", "r", encoding='cp1251') as file:
        lines = file.readlines()
        #found = False

        for line in lines:
            entry = line.split()
            record = bool([True for el in info_to_find_dict if el in entry])
            if record:
                result.append(entry)
        return result

# Функция для редактирования записи в справочнике
def edit_entry():
    display_entries()
    # info_to_find = input("Введите фамилию либо  через пробел иные поля записи(фамилия, имя, отчество, "
    #                 "название организации, телефон рабочий, телефон личный (сотовый)), "
    #                 "которую хотите отредактировать: ").split()
    # info_to_find_dict = {word.strip() for word in info_to_find}
    #info_to_find_dict = {"".join([fig for fig in info_to_find_dict if fig in "0123456789"  else fig])}

    found = search_entries()
    #found = search_entries(info_to_find_dict)
    if len(found) > 0:
        with open("data/телеф.справочник.txt", "a", encoding='cp1251') as file:
            file_writer = csv.writer(file)
            for rec in found:
                rec_split = rec.split()
                print("Найдена запись:")
                print("Фамилия:", rec_split[0])
                print("Имя:", rec_split[1])
                print("Отчество:", rec_split[2])
                print("Организация:", rec_split[3])
                print("Рабочий телефон:", rec_split[4])
                print("Личный телефон:", rec_split[5])
                print("------------------------------")

                new_last_name = input("Введите новую фамилию (оставьте пустым, если оставить прежнюю): ")
                new_first_name = input("Введите новое имя (оставьте пустым, если оставить прежнее): ")
                new_middle_name = input("Введите новое отчество (оставьте пустым, если оставить прежнее): ")
                new_organization = input("Введите новое название организации (оставьте пустым, если оставить прежнее): ")
                new_work_phone = input("Введите новый рабочий телефон (оставьте пустым, если оставить прежний): ")
                new_personal_phone = input("Введите новый личный телефон (оставьте пустым, если оставить прежний): ")

                if new_last_name != "":
                    rec_split[0] = new_last_name.strip()
                if new_first_name != "":
                    rec_split[1] = new_first_name.strip()
                if new_middle_name != "":
                    rec_split[2] = new_middle_name.strip()
                if new_organization != "":
                    rec_split[3] = new_organization.strip()
                if new_work_phone != "":
                    rec_split[4] = "".join([fig for fig in new_work_phone if fig in "0123456789"])
                if new_personal_phone != "":
                    rec_split[5] = "".join([fig for fig in new_personal_phone if fig in "0123456789"])
                #file.write(", ".join(rec_split))
                file_writer.writerow(rec_split)
    else:
        print(f"Запись не найдена")
    comm = input("Чтобы выйти из режима редактирования введите *  , чтобы продолжть нажмите любой другой символ ") != "#"
    if comm == "*":
        return

if __name__ == "__main__":
    # comm = ""
    # while comm != "5":
    #     menu()
    #     comm = input()
    menu()