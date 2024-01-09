# Curency variable in tkinter.

from tkinter import *
from curency_constants import *

# Using Language
TK_CUR_LANG = TR_LANG_TEXT


class CurencyVar(Variable):
    """Value holder for float variables."""
    _default = 0.0

    def __init__(self, master=None, value=None, name=None):
        """Construct a float variable.

        MASTER can be given as master widget.
        VALUE is an optional value (defaults to 0.0)
        NAME is an optional Tcl name (defaults to PY_VARnum).

        If NAME matches an existing variable and VALUE is omitted
        then the existing value is retained.
        """
        Variable.__init__(self, master, value, name)

        self._round = 2
        self._rnd_value = 0
        self._left = 0
        self._right = 0
        self._st = TK_CUR_LANG[4]

    def _set_LR(self):
        self._rnd_value = round(self.get(), self._round)
        s_rnd = str(self._rnd_value)
        if "." in s_rnd:
            l_rnd = s_rnd.split(".")
        else:
            l_rnd = [s_rnd, "0"]
        self._left, self._right = int(l_rnd[0]), int(l_rnd[1])
        if self._round == 2 and self._right < 10: self._right *= 10

    def get(self):
        """Return the value of the variable as a float."""
        return self._tk.getdouble(self._tk.globalgetvar(self._name))

    def get_round(self) -> float:
        """Return the round of the variable as a float."""
        self._set_LR()
        return self._rnd_value

    def get_in_comma(self) -> str:
        """Return the variable as a floating point string with a comma."""
        self._set_LR()
        txt = ""
        t_st = str(self._left)
        t_st = t_st[::-1]
        lng = len(t_st)
        for i, char in enumerate(t_st):
            j = i + 1
            txt = char + txt
            if j % 3 == 0 and j < lng and i > 0:
                txt = "," + txt
        if self._right > 0:
            txt = txt + "." + str(self._right) + " " + self._st[0]
        else:
            txt = txt + ".00 " + self._st[0]
        return txt

    def get_text(self) -> str:
        """Return the pronunciation of the variable as string."""
        self._set_LR()
        thousands = TK_CUR_LANG[3]
        txt = ""
        s_left = self._smash(str(self._left))
        s_left.reverse()
        for i, item in enumerate(s_left):
            temp = ""
            if item != '000':
                t_temp = thousands[i]
            else:
                t_temp = ''

            if item == "001" and i == 1:
                temp = thousands[i]
            else:
                temp = (self._cent_text(int(item[0])) + self._dec_text(int(item[1:])) + t_temp)
            txt = temp + txt
        txt = txt + " " + self._st[0] + " "
        if self._right > 0:
            txt += self._dec_text(self._right) + " " + self._st[1]
        return txt

    def _tens(self, deca: int) -> str:
        tens = TK_CUR_LANG[1]
        return tens[deca]

    def _ones(self, ones: int) -> str:
        l_ones = TK_CUR_LANG[0]
        return l_ones[ones]

    def _cent_text(self, cnt: int) -> str:
        txt = ""
        if cnt > 1:
            txt = self._ones(cnt) + TK_CUR_LANG[2][0]
        elif cnt == 1:
            txt = TK_CUR_LANG[2][0]

        return txt

    def _dec_text(self, dec: int) -> str:
        ones = int(dec % 10)
        tens = int(dec / 10)
        return f"{self._tens(tens)}{self._ones(ones)}"

    def _smash(self, st: str) -> list:
        lst = []
        lng = len(st)
        dv = int(lng / 3)
        dk = int(lng % 3)
        stt = st[:dk]
        if lng > 3:
            if len(stt) == 2:
                stt = "0" + stt
                lst.append(stt)
            elif len(stt) == 1:
                stt = "00" + stt
                lst.append(stt)
            for d in range(dv):
                start = d * 3 + dk
                stop = start + 3
                stt = st[start:stop]
                lst.append(stt)

        else:
            if lng == 2:
                st = "0" + st
            elif lng == 1:
                st = "00" + st
            lst.append(st)
        return lst

    # test


if __name__ == '__main__':
    from tkinter import ttk

    root = Tk()

    x = CurencyVar()
    y = CurencyVar()
    z = x

    x.set(1000.567)
    y.set(123456789123456.135)

    print("\nx:", x.get(), "->", x.get_in_comma(), "->", x.get_text())
    print("y:", y.get(), "->", y.get_in_comma(), "->", y.get_text())
    print(x == z)
    print("z:", z.get_in_comma(), z.get_text())
