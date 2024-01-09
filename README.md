# tk_curency

Curency variable in tkinter.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tk_curency.

```bash
pip install tk_curency
```

## Usage

```python
from tkinter import *
from tkinter import ttk
from tk_curency import *

def main():

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

main()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)