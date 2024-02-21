import pyodbc
import configparser
import tkinter as tk
from tkinter import simpledialog, PhotoImage
import pandas as pd
from pandastable import Table
import json
import sys
import customtkinter
import threading

config = configparser.ConfigParser()
config.read('config/config.ini')

width_config = int(config["GEOMETRIA"]["ANCHO"])
heigth_config = int(config["GEOMETRIA"]["ALTO"])


ReloadSpeed = int(config["CONFIG"]["ACT_TIME"])

server = str(config["DB"]["DBSERVER"])
database = str(config["DB"]["DBNAME"])
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')

lang_codes = {'Ingles': 'en', 'Español': 'es', 'Português': 'pt'}
theme_codes = {'Light': 'white', 'Dark': '#2d2d2d', 'lightblue': 'lightblue'}
LastTableShown = None
LastSize = None
threads = []

class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, text, accept, decline):
        self.text = text
        self.accept = accept
        self.decline = decline
        super().__init__(parent)

    def body(self, master):
        tk.Label(master, text=self.text).grid(row=0)
        self.geometry("300x70")

    def buttonbox(self):
        box = tk.Frame(self)

        tk.Button(box, text=self.accept, width=10, command=self.yes, default="active").pack(side="left", padx=5, pady=5)
        tk.Button(box, text=self.decline, width=10, command=self.no).pack(side="left", padx=5, pady=5)

        self.bind("<Return>", self.yes)
        self.bind("<Escape>", self.no)

        box.pack()

    def yes(self, event=None):
        self.ok()
        close_window_act()

    def no(self, event=None):
        self.cancel()

def calculate_font():
    root.update_idletasks()
    if root.winfo_width() > 1090:
        update_button_alarm.configure(font=("Arial", ((((root.winfo_width()//10)-(root.winfo_width()//12))*0.75)-2)))
        update_button_event.configure(font=("Arial", ((((root.winfo_width()//10)-(root.winfo_width()//12))*0.75)-2)))
        lang_select.configure(font=("Arial", (root.winfo_width()//10)-(root.winfo_width()//11)+3))
        theme_select.configure(font=("Arial", (root.winfo_width()//10)-(root.winfo_width()//11)+3))
    else:
        update_button_alarm.configure(font=("Arial", 12))
        update_button_event.configure(font=("Arial", 12))
        lang_select.configure(font=("Arial", 12))
        theme_select.configure(font=("Arial", 12))
    
    fullscreen_button.place(x=root.winfo_width()-49, rely=0)
    

def start_move(event):
    global x, y, LastSize
    x = event.x
    y = event.y
    if str(root.geometry()) == "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()):
        root.geometry(LastSize)
        root.update_idletasks()

def stop_move(event):
    global x, y
    x = None
    y = None

def do_move(event):
    delta_x = event.x - x
    delta_y = event.y - y
    new_pos = "+{}+{}".format(root.winfo_x() + delta_x, root.winfo_y() + delta_y)
    root.geometry(new_pos)
    calculate_font()

def start_resize(event):
    global width, height, x, y
    width = root.winfo_width()
    height = root.winfo_height()
    x = event.x
    y = event.y
    calculate_font()

def stop_resize(event):
    global width, height, x, y
    width = None
    height = None
    x = None
    y = None
    calculate_font()

def do_resize(event):
    global width, height, x, y
    delta_x = event.x - x
    delta_y = event.y - y
    new_size = "{}x{}".format(width + delta_x, height + delta_y)
    root.geometry(new_size)
    calculate_font()


#Close program
def close_window():
    root.protocol("WM_DELETE_WINDOW", close_window)
    CustomDialog(root, language['Ask_Exit'], language['Acc_Exit'], language['Dec_Exit'])

def close_window_act():
    for thread in threads:
        thread.cancel()
    sys.exit()
    
def maximize_window(event=None):
    global LastSize
    LastSize = root.geometry()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    calculate_font()
    

def load_language(lang):
    with open(f'languages/{lang}.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def change_language(event):
    global language, LastTableShown
    lang = lang_codes[lang_select.get()]
    language = load_language(lang)
    root.title(language['title'])
    update_button_alarm['text'] = language['refresh_alarms']
    update_button_event['text'] = language['refresh_events']
    if LastTableShown == 'alarm':
        read_db_alarm()
    elif LastTableShown == 'event':
        read_db_event()

def change_theme(event):
    global LastTableShown
    theme = theme_codes[theme_select.get()]
    value_list = list(theme_codes.values())
    if theme == value_list[0]:
        root.config(bg=theme)
        FullFrame.config(bg=theme)
        TopFrame.config(bg=theme)
        FootFrame.config(bg=theme)
        update_button_alarm.configure(fg_color='#0179d8', hover_color='#0179d8', text_color='white')
        update_button_event.configure(fg_color='#0179d8', hover_color='#0179d8', text_color='white')
        theme_select.configure(fg_color='#0179d8', border_color='#0179d8', text_color='white')
        lang_select.configure(fg_color='#0179d8', border_color='#0179d8', text_color='white')
    elif theme == value_list[1]:
        root.config(bg=theme)
        FullFrame.config(bg=theme)
        TopFrame.config(bg=theme)
        FootFrame.config(bg=theme)
        update_button_alarm.configure(fg_color='#bb86fc', hover_color='#bb86fc', text_color='black')
        update_button_event.configure(fg_color='#bb86fc', hover_color='#bb86fc', text_color='black')
        theme_select.configure(fg_color='#bb86fc', border_color='#bb86fc', text_color='black')
        lang_select.configure(fg_color='#bb86fc', border_color='#bb86fc', text_color='black')
    elif theme == value_list[2]:
        root.config(bg=theme)
        FullFrame.config(bg=theme)
        TopFrame.config(bg=theme)
        FootFrame.config(bg=theme)
        update_button_alarm.configure(fg_color='#D35B58', hover_color='#D35B58', text_color='white')
        update_button_event.configure(fg_color='#D35B58', hover_color='#D35B58', text_color='white')
        theme_select.configure(fg_color='#D35B58', border_color='#D35B58', text_color='white')
        lang_select.configure(fg_color='#D35B58', border_color='#D35B58', text_color='white')
        
    if LastTableShown == 'alarm':
        read_db_alarm()
    elif LastTableShown == 'event':
        read_db_event()
        
def check_auto_update():
    if auto_update.get():
        read_db_event()
    thread = threading.Timer(ReloadSpeed, check_auto_update)
    thread.start()
    threads.append(thread)

def read_db_alarm():
    global LastTableShown
    cursor = conn.cursor()
    cursor.execute("SELECT Al_Start_Time, Al_Message, Al_Ack_Time  FROM ALARMHISTORY") 
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columns)
    df.rename(columns={
        'Al_Start_Time': language['Al_Start_Time'],
        'Al_Message': language['Al_Message'],
        'Al_Ack_Time': language['Al_Ack_Time'],
    }, inplace=True)  
    df = df.infer_objects()  
    pd.set_option('future.no_silent_downcasting', True)
    table = Table(DbViewerFrame, width=width_config-(width_config//3), dataframe=df, showtoolbar=True, showstatusbar=True, maxcellwidth=1000)
    table.show()
    table.columnwidths[df.columns[0]] = 280
    table.columnwidths[df.columns[1]] = 410
    table.columnwidths[df.columns[2]] = 250
    table.redrawVisible()
    LastTableShown = 'alarm'

def read_db_event():
    global LastTableShown
    cursor = conn.cursor()
    cursor.execute("SELECT Ev_Time, Ev_User, Ev_Message, Ev_Station  FROM EVENTHISTORY") 
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columns)
    df.rename(columns={
        'Ev_Time': language['Ev_Time'],
        'Ev_User': language['Ev_User'],
        'Ev_Message': language['Ev_Message'],
        'Ev_Station': language['Ev_Station']
    }, inplace=True)
    df = df.infer_objects()
    pd.set_option('future.no_silent_downcasting', True)
    table = Table(DbViewerFrame, width=width_config-(width_config//5), dataframe=df, showtoolbar=True, showstatusbar=True, maxcellwidth=1000)
    table.show()
    table.columnwidths[df.columns[0]] = 280
    table.columnwidths[df.columns[1]] = 110
    table.columnwidths[df.columns[3]] = 195
    table.redrawVisible()
    LastTableShown = 'event'
    return table

#Default language
language = load_language('pt') 

root = tk.Tk()
root.title(language['title'])
root.config(bg=theme_codes['lightblue'])
root.overrideredirect(True)
root.geometry(f"{width_config}x{heigth_config}")
root.resizable(True, True)
root.update_idletasks()

FullFrame = tk.Frame(root, bg=theme_codes['lightblue'])
FullFrame.pack(fill='both', expand=True)
HIGHTopFrame = tk.Frame(FullFrame, height=21, bg='lightgrey')
HIGHTopFrame.pack(fill=tk.X)
TopFrame = tk.Frame(FullFrame, bg=theme_codes['lightblue'])
TopFrame.pack(padx=10, pady=20)
DbViewerFrame = tk.Frame(FullFrame, bg='#f0f0f0')
DbViewerFrame.pack(padx=10)
FootFrame = tk.Frame(FullFrame, bg=theme_codes['lightblue'])
FootFrame.pack(padx=10, pady=10)


#Mover pantalla
HIGHTopFrame.bind("<ButtonPress-1>", start_move)
HIGHTopFrame.bind("<ButtonRelease-1>", stop_move)
HIGHTopFrame.bind("<B1-Motion>", do_move)
#Resize Screen
root.bind("<ButtonPress-3>", start_resize)
root.bind("<ButtonRelease-3>", stop_resize)
root.bind("<B3-Motion>", do_resize)

#Image Sources
x_photo = PhotoImage(file=("resources/x_button.png"))
y_photo = PhotoImage(file=("resources/y_button.png"))

#Muestra los eventos por defecto
read_db_event()

auto_update = tk.BooleanVar()
auto_update.set(False)

close_button = tk.Button(FullFrame, bg='lightgrey', image=x_photo, borderwidth=0, highlightthickness=0,  command=close_window)
close_button.place(relx=1, rely=0, anchor='ne')

fullscreen_button = tk.Button(FullFrame, bg='lightgrey', image=y_photo, borderwidth=0, highlightthickness=0,  command=maximize_window)
fullscreen_button.place(x=root.winfo_width()-49, rely=0, anchor='ne')


update_button_alarm = customtkinter.CTkButton(FootFrame, text=language['refresh_alarms'], command=read_db_alarm, fg_color="#D35B58", hover_color="#D35B58")
update_button_alarm.grid(row=1, column=1, padx=5, pady=5)

update_button_event = customtkinter.CTkButton(FootFrame, text=language['refresh_events'], command=read_db_event, fg_color="#D35B58", hover_color="#D35B58")
update_button_event.grid(row=1, column=2, padx=5, pady=5)

lang_select = customtkinter.CTkComboBox(TopFrame, values=list(lang_codes.keys()), fg_color="#D35B58", border_color="#D35B58", command=change_language)
lang_select.set('Português')
lang_select.grid(row=1, column=1, padx=10, pady=5)

theme_select = customtkinter.CTkComboBox(TopFrame, values=list(theme_codes.keys()), fg_color="#D35B58", border_color="#D35B58", command= change_theme)
theme_select.set('lightblue')
theme_select.grid(row=1, column=2, padx=10, pady=5)

check_button = tk.Checkbutton(TopFrame, text=language['Update_Text'], variable=auto_update)
check_button.grid(row=1, column=3, padx=10, pady=5)

check_auto_update()
calculate_font()
root.mainloop()
