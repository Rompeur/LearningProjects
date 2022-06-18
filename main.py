import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

class Pomodoro:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x400")
        self.root.title("Pomodoro Timer")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file='tomato.png'))

        self.root.mainloop() #runs the application forever




Pomodoro()

