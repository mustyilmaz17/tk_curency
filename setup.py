import setuptools

long_description = """

Curency variable in tkinter. 


## Installation

```python
python -m pip install tk_curency
```

## Simple Usage
Instead of using long, complicated ttk style classes, you can use simple keywords with the "bootstyle" parameter.

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



## Links
-   
- **GitHub:** https://github.com/users/mustyilmaz17/projects/3
"""

setuptools.setup(
    name="tk_curency",
    version="0.0.1",
    author="Mustafa YILMAZ",
    author_email="mustyilmaz17@gmail.com",
    description="Curency variable in tkinter. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/users/mustyilmaz17/projects/3",
    keywords="python tkinter curency variable",
    packages=setuptools.find_packages(),
    install_requires=["tkinter"],
    python_requires=">=3.7",
)
