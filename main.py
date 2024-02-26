import sqlite3
from prettytable import PrettyTable
from colored import Fore, Style

conn = sqlite3.connect(database='database.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS data(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age TEXT
)
""")

def insert_data(name,age):
    cursor.execute("INSERT INTO data (name,age) VALUES(?,?)",(name,age))
    conn.commit()

def select_data():
    cursor.execute("SELECT * FROM data")
    return cursor.fetchall()

def delete_data(id):
    cursor.execute("DELETE FROM data WHERE id=?",(id))
    conn.commit()

def update_data(id, new_name,new_age):
    cursor.execute("UPDATE data SET name=?, age=? WHERE id=?",(new_name,new_age,id))

def show_data_table():
    datas = select_data()
    table = PrettyTable()
    table.field_names = [f'{Fore.red}Id{Style.reset}',f'{Fore.yellow}Name{Style.reset}',f'{Fore.green}Age{Style.reset}']
    for data in datas:

        table.add_row([f'{Fore.red}{data[0]}{Style.reset}',f'{Fore.yellow}{data[1]}{Style.reset}',f'{Fore.green}{data[2]}{Style.reset}'])
    return table


def main():
    while True:
        print(f'1.Create')
        print(f'2.Show')
        print(f'3.Delete')
        print(f'4.Update')
        print(f'5.Exit')
        choice = input("Enter: ")
        if choice == '5':
            break
        elif choice == '1':
            name = input('Your name: ')
            age = input('Your age: ')
            insert_data(name,age)
        elif choice == '2':
            print(show_data_table())

        elif choice == '3':
            id = input("Please enter id: ")
            delete_data(id)
        elif choice == '4':
            id = input("Enter id: ")
            new_name = input("New name: ")
            new_age = input("New age:")
            update_data(id,new_name,new_age)
                

if __name__ == '__main__':
    main()