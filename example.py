# The test of tk_curency module

from tkinter import *
from tkinter import ttk
from curency import *


if __name__ == '__main__':

    def set_text(event):
        try:
            x_lbt_rnd.configure(text=x.get_in_comma())
            x_lbl_txt.configure(text=x.get_text())
        except:
            pass


    root = Tk()

    x = CurencyVar()
    y = CurencyVar()
    z = x

    x.set(1000.567)
    y.set(123456789123456.135)

    x_ent = ttk.Entry(root, textvariable=x)
    x_lbl = ttk.Label(root, textvariable=x)

    x_lbt_rnd = ttk.Label(root, text=x.get_in_comma())
    x_lbl_txt = ttk.Label(root, text=x.get_text())

    y_lbl = ttk.Label(root, text=y.get_in_comma())
    y_lbl_txt = ttk.Label(root, text=y.get_text())

    root.bind('<Key>', set_text)

    x_ent.pack()
    x_lbl.pack()
    x_lbt_rnd.pack()
    x_lbl_txt.pack()
    y_lbl.pack()
    y_lbl_txt.pack()

    root.mainloop()