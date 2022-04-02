import tkinter as tk
from typing import List


def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculator')
    root.iconbitmap('images/img_calculator.ico')
    root.config(padx=10, pady=10, background='#FFF')
    root.resizable(False, False)
    return root


def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text='Sem conta ainda',
        anchor='e', justify='right',  # anchor referente ao label. justify referente ao texto
        background='#FFF'
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label


def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify='right', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#CCC'
    )
    display.bind('<Control-a>', _display_control_a)
    return display


def _display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'


def make_buttons(root) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['9', '8', '7', '+', 'C'],
        ['6', '5', '4', '-', '/'],
        ['3', '2', '1', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]

    buttons: List[List[tk.Button]] = []

    for row, row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(root, text=col_value)
            btn.grid(row=row, column=col_index, sticky='news', padx=5, pady=5)
            btn.config(
                font=('Helvetica', 15, 'normal'),
                pady=40, width=1, background='#F1F2F3', bd=0,
                cursor='hand2', highlightthickness=0,
                highlightcolor='#CCC', activebackground='#CCC',
                highlightbackground='#CCC'
            )
            button_row.append(btn)
        buttons.append(button_row)

    return buttons
