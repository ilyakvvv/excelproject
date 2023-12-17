from funcs import *

if __name__ == "__main__":
    file_names = ['1.xlsx', '2.xlsx', '3.xlsx']

    lastID = get_last_id_from_first_file(file_names[0])

    for name in file_names[1:]:
        lastID = numerate_rows_in_excel(name, lastID)


