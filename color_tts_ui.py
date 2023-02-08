from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox
from convert_color_codes import *


def choose_color():
    cc = colorchooser.askcolor(title="Choose color")
    rgb, hex = cc
    if not (rgb or hex):
        return
    r, g, b = rgb
    color_btn.config(text=f"r={r}, g={g}, b={b}, hex={hex}", bg=hex)

    gd = 9
    try:
        gd = grid_size.get() or gd
    except Exception as e:
        messagebox.showwarning("Error", f"Invalid grid size.\n{e}")

    if gd > 20:
        gd = 20
    gr = color_b_grid(hex, gd)
    grid(gr)


def grid(grid: list[str]):
    g = len(grid)

    global last_grid
    if g != last_grid:
        last_grid = g
        for row_lbl in grid_lbls:
            for lbl in row_lbl:
                lbl.destroy()
        grid_lbls.clear()

        rw = rh = 1 / g
        rx = ry = 0

        for row in grid:
            row_lbl = []
            for hex in row:
                lbl = Label(view, bg=hex, relief="groove")
                lbl.place(relx=rx, rely=ry, relw=rw, relh=rh)

                rx += rw
                if rx >= 1:
                    rx = 0
                    ry += rh
                if ry >= 1:
                    ry = 0

                row_lbl.append(lbl)

            grid_lbls.append(row_lbl)

    else:
        for lbls, row in zip(grid_lbls, grid):
            for lbl, hex in zip(lbls, row):
                lbl["bg"] = hex


last_grid = 0
grid_lbls = []


root = Tk()
root.title("Color Tints, Tones, Shades")
bh = 50

rw = 0.18
lbl = Label(root, text="Grid Size:", relief="groove")
lbl.place(relx=0, rely=0, relw=rw, h=bh)

grid_size = IntVar()
gs = ttk.Spinbox(root, from_=9, increment=1, to=10, textvariable=grid_size)
gw = 0.1
gs.place(relx=rw, rely=0, relw=rw + gw, h=bh)
rw += gw

color_btn = Button(root, text="Select color", command=choose_color)
color_btn.place(relx=rw, rely=0, relw=1 - rw, h=bh)

w, h = 670, 500
root.geometry(f"{w}x{h+bh}")

view = Frame(root, relief="groove", bg="red")
view.place(relx=0, y=bh, w=w, h=h)


root.mainloop()
