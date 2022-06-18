import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

class Pomodoro:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x300")
        self.root.title("Pomodoro Timer")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file='tomato.png'))

        #simple style adding
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Ubuntu", 16))
        self.s.configure("TButton", font=("Ubuntu", 16))

        #creating a notebook, which allows us to select pages of contents by clicking on tabs
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

        #creating individual frames for each tab
        self.tab1 = ttk.Frame(self.tabs, width=700, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=700, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=700, height=100)

        #the timers are adjustable up to the preference of the user
        self.pomodoro_label = ttk.Label(self.tab1, text="35:00", font=("Ubuntu", 50))
        self.pomodoro_label.pack(pady=20)

        self.short_break_timer_label = ttk.Label(self.tab2, text="5:00", font=("Ubuntu", 50))
        self.short_break_timer_label.pack(pady=20)

        self.long_break_time_label = ttk.Label(self.tab3, text="15:00", font=("Ubuntu", 50))
        self.long_break_time_label.pack(pady=20)


        #creating and naming tabs
        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

        # runs the application forever
        self.root.mainloop()

    def start_timer_thread(self):
        pass

    def start_time(self):
        pass

    def reset(self):
        pass

    def skip_clock(self):
        pass

Pomodoro()

