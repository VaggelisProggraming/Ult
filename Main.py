"""
This is the language from the operating system 'BluelineOS'
that doesn't mean 'BluelineOS' is written in Ult
see it on github 
"""

from tkinter import *
import os
class output() :
    def text(string) : 
        print(">>>" + string)
    def type(string) :
        input(string)
    class run() :
        def cmd(string) :
            os.system(f"cmd /c {string}")


class Window() :
    """
    this is the function that has everything to make a window
    """
    class New() :
        """
        creates a new window
        """
        def make() :
            """
            this is creating a new window
            """
            Win = Tk()
        def Run() :
            mainloop()
    class Add() :
        """
        adds
        """
        def text(string, color, bg) :
            Label(text=string, foreground=color, background=bg).pack()
        def input() :
            Entry().pack()

