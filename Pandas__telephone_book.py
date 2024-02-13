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
import pandas as pd


#expand the output display to see more columns of a Pandas DataFrame
pd.set_option('display.expand_frame_repr', False)

col_names = ["фамилия", "имя", "отчество", "название организации", "телефон рабочий", "телефон личный (сотовый)"]
db = pd.read_csv("data/телеф.справочник.txt", names=col_names)
db["телефон рабочий"] = db["телефон рабочий"].astype('str')
db["телефон личный (сотовый)"] = db["телефон личный (сотовый)"].astype('str')


# Функция для вывода меню и обработки выбранного пункта
def menu(db):
    print("Телефонный справочник")
    print("1. Вывод записей")
    print("2. Добавление записи")
    print("3. Редактирование записи")
    print("4. Поиск записей")
    print("5. Выход")
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        display_entries(db)
    elif choice == "2":
        db = add_entry(db)
    elif choice == "3":
        db = edit_entry(db)
    elif choice == "4":
        db_searched = search_entries(db)
    elif choice == "5":
        exit()
    else:
        print("Некорректный выбор. Попробуйте снова.")
    menu(db)

# Функция для вывода записей из справочника
def display_entries(db):
    if len(db) == 0:
        print("Справочник пуст.")
    else:
        print("Телефонный справочник", "\n")
        num_rows_on_page = 10
        count_row = 0
        count_page = 0
        pd.set_option('display.max_rows', num_rows_on_page)
        while count_row <= len(db):
            print(db[count_row : count_row + num_rows_on_page])
            print(f"Страница {count_page + 1}".center(100,"-"), end="\n")
            print()
            count_row += num_rows_on_page
            count_page += 1
    comm = input("для выхода из текущего режима введите * \n")
    if comm == "*":
        return db

# Функция для добавления новой записи в справочник
def add_entry(db):
    entry_list = [] #список, в котором будут храниться вводимые/добавляемые записи
    comm = ""
    while comm != "*":
        alphabit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        last_name = input("Введите фамилию: ").strip().title()
        last_name = "".join([s for s in last_name if s.lower() in alphabit])
        first_name = input("Введите имя: ").strip().title()
        first_name = "".join([s for s in first_name if s.lower() in alphabit])
        middle_name = input("Введите отчество: ").strip().title()
        middle_name = "".join([s for s in middle_name if s.lower() in alphabit])
        organization = input("Введите название организации: ").strip().title()
        work_phone = input("Введите рабочий телефон: ")
        work_phone = "".join([fig for fig in work_phone if fig in "0123456789"])
        personal_phone = input("Введите личный телефон: ")
        personal_phone = "".join([fig for fig in personal_phone if fig in "0123456789"])

        entry = [last_name, first_name, middle_name, organization, work_phone, personal_phone]
        entry_list.append(entry)
        print("entry_list", entry_list)
        print("Запись успешно добавлена.")

        comm = input("Чтобы выйти из режима ввода записей, введите *  , чтобы продолжить нажмите \n "
                     "любой другой символ \n")

    col_names = ["фамилия", "имя", "отчество", "название организации", "телефон рабочий",
                     "телефон личный (сотовый)"]
    for entry in entry_list:
        db = pd.concat([db, pd.DataFrame([entry], columns= col_names)], ignore_index=True)
    db.to_csv("data/телеф.справочник.txt", index=False, header=False)
    return db

# Функция для поиска записи/записей в справочнике в соответствии с введенными значениями
def search_entries(db):
    searched_db = pd.DataFrame()
    col_names = ["фамилия", "имя", "отчество", "название организации", "телефон рабочий",
                 "телефон личный (сотовый)"]
    info_to_find = input("Введите через пробел какие-либо поля записи(фамилия, имя, отчество, \n"
                    "название организации, телефон рабочий, телефон личный (сотовый)), \n"
                    "которую хотите найти \n").split()
     # формируем список уникальных введенных пользователем значений для поиска нужной записи/записей
    info_to_find_list = list({word.title().strip() for word in info_to_find})
    intermidiate_db = db
    for feature in info_to_find_list:
        preliminary_db = db[db.isin([feature])].dropna(how="all")
        searched_db = intermidiate_db.loc[intermidiate_db.index.intersection(preliminary_db.index)]
        intermidiate_db = searched_db
    print("Найденные записи" , "\n", searched_db)
    return searched_db

# Функция для редактирования записи в справочнике
def edit_entry(db):
    alphabit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    comm = ""
    while comm != "*":
        try:
            found = search_entries(db)
        except TypeError as e:
            print("Не найдена запись с соответстующими значениями")
        else:
            if len(found) == 0:
                print("Не найдена запись с соответстующими значениями")
            else:
                print("Найдена запись:")
                print(found)
                #print("found.values", found.values, type(found))
                print("--------------------------------------------------------------------------------")
                for row in found.values:
1                    new_last_name = input("Введите новую фамилию (оставьте пустым, если оставить прежнюю): ").strip().title()
                    new_first_name = input("Введите новое имя (оставьте пустым, если оставить прежнее): ").strip().title()
                    new_middle_name = input("Введите новое отчество (оставьте пустым, если оставить прежнее): ").strip().title()
                    new_organization = input("Введите новое название организации (оставьте пустым, если оставить прежнее): ").strip()
                    new_work_phone = input("Введите новый рабочий телефон (оставьте пустым, если оставить прежний): ").strip()
                    new_personal_phone = input("Введите новый личный телефон (оставьте пустым, если оставить прежний): ").strip()

                    print("Введенная запись:", "\n", row)
                    if new_last_name != "":
                        db.loc[db['фамилия'] == row[0], ['фамилия']] = new_last_name
                    if new_first_name != "":
                        db.loc[db['имя'] == row[1], ['имя']] = new_first_name
                    if new_middle_name != "":
                        db.loc[db['отчество'] == row[2], ['отчество']] = new_middle_name
                    if new_organization != "":
                        db.loc[db['название организации'] == row[3], ['название организации']] = new_organization
                    if new_work_phone != "":
                        db.loc[db['телефон рабочий'] == row[4], ['телефон рабочий']] = new_work_phone
                    if new_personal_phone != "":   
                        db.loc[db['телефон личный (сотовый)'] == row[5], ['телефон личный (сотовый)']] = new_personal_phone    #"".join([fig for fig in new_personal_phone if fig in "0123456789"])
                    if input("Для выхода из редактировния следующих НАЙДЕННЫХ записей нажмите * \n") == "*":
                        break
        print()
        comm = input("Чтобы выйти из режима редактирования  введите * \n ,"
                     " чтобы продолжить редактирование, нажмите любой другой символ \n")

    db.to_csv("data/телеф.справочник.txt", index=False, header=False)
    return db

if __name__ == "__main__":
    menu(db)


