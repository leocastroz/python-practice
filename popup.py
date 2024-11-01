#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox

def exibir_popup():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Aviso", "Este é um popup no Linux!")
    root.destroy()

exibir_popup()
