from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QMessageBox, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QTextDocument, QPalette, QColor
from sys import*
from random import randint

app = QApplication([])
# Главное окно
window = QMainWindow()
window.setWindowTitle("Тайм Менеджемент")
window.setGeometry(100, 100, 500, 300)
window.setFixedSize(500,300)
#Сохранение шрифта
#try:
#    with open("шрифт.txt","r") as file:
#        color_values = file.split(" ")
#        red = int(color_values[0])
#        green = int(color_values[1])
#        blue = int(color_values[2])
#        palette.setColor(QPalette.Background, QColor(red, green, blue))
#        window.setPalette(palette)
#        settings.setPalette(palette)
#except:
#    None

# Кнопка "Начать работу"
def start_work():
    start_button.hide()
    button_settings_on.show()
    button_schedule.show()
    button_activities.show()
    button_analyzer.show()

start_button = QPushButton("Начать работу", window) 
start_button.setGeometry(200, 100, 100, 40)
start_button.clicked.connect(start_work)

# Палитра
palette = window.palette()
palette.setColor(QPalette.Background, QColor(150,150,150))
window.setPalette(palette)

# Меню настроек
settings = QWidget()
settings.setWindowTitle("Настройки")
settings.setFixedSize(300, 200)
settings.setPalette(palette)

button_settings_off = QPushButton("Закрыть настройки", settings)
button_settings_off.setGeometry(90, 150, 125, 40)

# Функция, меняющая цвет фона
def palette_check():
    color_text = color_line.text()
    if color_text:
        try:
            with open("шрифт.txt","w") as file:
                file.write(color_text)
        except:
            None
    else:
        None

def change_background_color():
    color_text = color_line.text()
    if color_text:
        try:
            color_values = color_text.split(" ")
            red = int(color_values[0])
            green = int(color_values[1])
            blue = int(color_values[2])
            palette.setColor(QPalette.Background, QColor(red, green, blue))
            window.setPalette(palette)
            settings.setPalette(palette)
#            notes.setPalette(palette)
            QMessageBox.information(window, "Успех", "Цвет фона успешно изменен")
            palette_check()
        except ValueError:
            QMessageBox.critical(window, "Ошибка", "Некорректный формат цвета")
    else:
        QMessageBox.warning(window, "Предупреждение", "Поле ввода цвета пустое")
    color_line.clear()

color_accept = QPushButton("Установить цвет фона", settings)
color_accept.setGeometry(90, 60, 125, 40)
color_accept.clicked.connect(change_background_color)

color_label = QLabel("Введите цвет (R G B):", settings)
color_label.setGeometry(90, 00, 125, 50)

color_line = QLineEdit(settings)
color_line.setGeometry(90, 37, 120, 20)

# Помощь
# Функция для отображения окна справки
def show_help_dialog():
    help_text = "RGB код представляет собой цвет в виде комбинации красного, зеленого и синего. Вводите код без запятых через пробел, например: 255 0 0 для красного цвета."
    QMessageBox.information(settings, "Справка", help_text)

help_button = QPushButton("Помощь", settings)
help_button.setGeometry(90, 100, 125, 40)
help_button.clicked.connect(show_help_dialog)

def button_close_settings():
    settings.close()
    button_settings_on.show()

button_settings_off.clicked.connect(button_close_settings)

def button_start_settings():
    #button_settings_on.hide()
    settings.show()

# Кнопка настроек
button_settings_on = QPushButton("Настройки", window)
button_settings_on.setGeometry(380, 20, 100, 40)
button_settings_on.clicked.connect(button_start_settings)
button_settings_on.hide()

# Кнопка "Моё расписание"
button_schedule = QPushButton("Моё расписание", window)
button_schedule.setGeometry(80, 100, 100, 70)
button_schedule.hide()
# Кнопка "Чем заняться"
def activities_menu():
    button_activities.hide()
    button_analyzer.hide()
    button_schedule.hide()
    activities_menu_off.show()
    rest_label.show()
    rest_label2.show()
    what_to_do.show()

def close_activities_menu():
    button_activities.show()
    button_analyzer.show()
    button_schedule.show() 
    activities_menu_off.hide()
#    notes.hide()
    rest_label.hide()
    rest_label2.hide()
    what_to_do.hide()

activities_menu_off = QPushButton("Выйти в меню",window)
activities_menu_off.setGeometry(20, 230, 100, 40)
activities_menu_off.hide()
activities_menu_off.clicked.connect(close_activities_menu)

button_activities = QPushButton("Чем заняться", window)
button_activities.setGeometry(200, 100, 100, 70)
button_activities.hide()
button_activities.clicked.connect(activities_menu)

rest_label = QLabel("Как насчёт",window)
rest_label.setGeometry(190, 125, 70, 20)
rest_label.hide()

random_list = "XXXXXXXXXXX"

rest_label2 = QLabel(random_list, window)
rest_label2.setGeometry(250, 125, 150, 20)
rest_label2.hide()

def what_to_do_generate():
    rest_label2.hide()
    rand = randint(0, len(rest_list)-1)
    rest_label2.setText(rest_list[rand])
    rest_label2.show()

what_to_do = QPushButton("Узнать чем \n заняться",window)
what_to_do.setGeometry(20, 120, 100, 40)
what_to_do.hide()
what_to_do.clicked.connect(what_to_do_generate)
rest_list = ["позаниматься общественной деятельностью?", "посмотреть фильм/сериал?", "почитать?","поиграть во что-нибудь?", "поспать?","позаниматься спортом?","погулять?", "пообщаться с друзьями?","послушать музыку?","порисовать?","убраться в комнате?","что-нибудь поесть?","что-нибудь приготовить?","послушать музыку?"]


# Кнопка "Заметки"
#def notes_menu():
#    notes.show()
#    notes_menu_off.show()
#    add_notes_button.show()
#    del_notes_button.show()
#
#notes = QWidget()
#notes.setWindowTitle("Заметки")
#notes.setFixedSize(400, 600)
#notes.setPalette(palette)
#notes.hide()


from tkinter import *
from tkinter.messagebox import showerror, askyesno, showinfo
import sqlite3
from pathlib import Path

file = Path('notes.db')
file.touch(exist_ok=True)

db = sqlite3.connect("notes.db")
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS notes (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT,
    content TEXT
);
""")
db.commit()

root = Tk()
root.title("Заметки")
root.geometry("300x500")

def note(*args, update_func=None):
    if args:
        cur.execute("SELECT id, name, content FROM notes WHERE id = ?", args)
        id, name, content = cur.fetchone()

    window = Toplevel()
    if args:
        window.title(name)
    else:
        window.title("Новая заметка")
    window.geometry("400x500")

    def save(*_):
        nonlocal entry, text, update_func, window, args

        if not entry.get():
            showerror("Ошибка", "Укажите название заметки")
        elif not text.get("0.0", END).strip():
            showerror("Ошибка", "Укажите содержимое заметки")
        else:
            if args:
                cur.execute("UPDATE notes SET name = ?, content = ? WHERE id = ?", (entry.get(), text.get("0.0", END), id))
            else:
                cur.execute("INSERT INTO notes (name, content) VALUES (?, ?)", (entry.get(), text.get("0.0", END)))
            db.commit()
            update_func()
            window.destroy()

    def cancel(*args):
        window.destroy()

    Label(window, text="Название:").place(relheight=0.05, relx=0.05, rely=0.05, relwidth=0.2)
    Label(window, text="Содержимое:").place(relheight=0.05, relwidth=0.2, relx=0.4, rely=0.15)

    entry = Entry(window)
    entry.place(relheight=0.05, relx=0.3, rely=0.05, relwidth=0.65)

    text = Text(window, wrap=WORD)
    text.place(relwidth=0.9, relx=0.05, rely=0.25, relheight=0.6)

    if args:
        entry.insert(0, name)
        text.insert("0.0", content)

    button_save = Button(window, text="Сохранить", relief=SOLID, command=save)
    button_save.place(relheight=0.05, relwidth=0.3, rely=0.9, relx=0.05)
    window.bind("<Control-s>", save)

    button_cancel = Button(window, text="Отмена", relief=SOLID, command=cancel)
    button_cancel.place(relheight=0.05, relwidth=0.3, rely=0.9, relx=0.65)
    window.bind("<Escape>", cancel)

def delete(*args, update_func=None):
    global notes, notes_listbox

    select_note = notes[notes_listbox.curselection()[0]]

    result = askyesno(title=f"Удаление заметки \"{select_note[1]}\"",
                      message=f"Вы уверены, что хотите удалить заметку \"{select_note[1]}\"")

    if result:
        cur.execute("DELETE FROM notes WHERE id = ?", (select_note[0],))
        db.commit()

        showinfo("Заметка удалена", message=f"Заметка {select_note[1]} удалена навсегда")

        update_func()
        on_select()

def update():
    global notes, notes_var

    cur.execute("SELECT id, name FROM notes")
    notes = cur.fetchall()
    notes_var.set([note[1] for note in notes])


def get_index():
    global notes_listbox

    return notes_listbox.curselection()[0]


def on_select(*args):
    global button_edit, button_delete, notes_listbox

    if notes_listbox.curselection():
        button_edit.config(state=NORMAL)
        button_delete.config(state=NORMAL)
    else:
        button_edit.config(state=DISABLED)
        button_delete.config(state=DISABLED)

cur.execute("SELECT id, name FROM notes")
notes = cur.fetchall()

notes_var = Variable(value=[note[1] for note in notes])
notes_listbox = Listbox(root, listvariable=notes_var, selectmode=SINGLE)
notes_listbox.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)
notes_listbox.bind("<<ListboxSelect>>", on_select)
notes_listbox.bind("<Return>", lambda *args: note(notes[get_index()][0], update_func=update))
notes_listbox.bind("<Double-Button-1>", lambda *args: note(notes[get_index()][0], update_func=update))
notes_listbox.bind("<Delete>", lambda *args: delete(update_func=update))

button_edit = Button(root, text="Изменить", relief=SOLID, state=DISABLED, command=lambda : note(notes[get_index()][0], update_func=update))
button_edit.place(relheight=0.05, relwidth=0.3, rely=0.9, relx=0.05)

button_add = Button(root, text="Добавить", relief=SOLID, command=lambda : note(update_func=update))
button_add.place(relheight=0.05, relwidth=0.2, rely=0.9, relx=0.4)

button_delete = Button(root, text="Удалить", relief=SOLID, state=DISABLED, command=lambda : delete(update_func=update))
button_delete.place(relheight=0.05, relwidth=0.3, rely=0.9, relx=0.65)

def start_notes():  
    root.mainloop()

button_analyzer = QPushButton("Заметки", window)
button_analyzer.setGeometry(320, 100, 100, 70)
button_analyzer.hide()
button_analyzer.clicked.connect(start_notes)
#
#
#def close_notes_menu():
#    button_activities.show()
#    button_analyzer.show()
#    button_schedule.show() 
#    activities_menu_off.hide()
#    notes.hide()
#    rest_label.hide()
#    rest_label2.hide()
#    what_to_do.hide()
#
#y = 100
#notes_label = QLabel(None, notes)
#notes_label.setGeometry(20, y, 150, 20)
#
#def add_notes(y):
#    notes_list.append(note_line.text())
#    notes_label.setGeometry(20, , 150, 20)
#    for i in notes_list:
#        notes_label.setText(i)
#        notes_label.setGeometry(20, y, 150, 20)
#        
#
#add_notes_button = QPushButton("Добавить заметку",notes)
#add_notes_button.setGeometry(20, 30, 120, 40)
#add_notes_button.hide()
#add_notes_button.clicked.connect(add_notes)
#
#notes_list = []
#
#def del_notes():
#    None
#
#del_notes_button = QPushButton("Удалить заметку",notes)
#del_notes_button.setGeometry(270, 30, 120, 40)
#del_notes_button.hide()
#del_notes_button.clicked.connect(del_notes)
#
#notes_menu_off = QPushButton("Выйти в меню",notes)
#notes_menu_off.setGeometry(20, 540, 100, 40)
#notes_menu_off.hide()
#notes_menu_off.clicked.connect(close_notes_menu)
#
#note_line = QLineEdit(notes)
#note_line.setGeometry(22, 70, 117, 20)
#note_line.show()

# Кнопка "Выйти"
def exit_program():
    app.exit()

button_exit = QPushButton("Завершить \n работу", window)
button_exit.setGeometry(380, 230, 100, 40)
button_exit.clicked.connect(exit_program)

# Ввод задач
window.show()
app.exec_()