"""
module: ui_multi_select.py

purpose: provide expandable widget UI for selecting options.

comments: based on multi_select.py in project pandas_02

author: Russell Folks

history:
-------
09-20-2024  creation
09-20-2024  Change some variable names to be more generic. 
              filter_spec_fr --> main_list_fr
              filt_rows      --> item_rows
09-25-2024  Add shortcut keys to add or subtrct a widget row.
10-04-2024  In create_selection_row(), parameter defaults to None.
            Add opt_fxn as an optional function from the calling module.
10-16-2024  Committed to GitHub repository ui_RF.
"""
import tkinter as tk
from tkinter import ttk
import sys
# new note
this = sys.modules['__main__']

this.do_debug = False

def create_selection_row(windows: dict = None) -> object:
    """Add a new row of widgets for making a selection-from-list.

    uses variables from the calling module:
        main_list_fr
        data_columns
    """
    # print(f'in multi_select/create_slection_row, data_columns is:\n{this.data_columns}')
    nextrowframe = ttk.Frame(this.main_list_fr, border=2)

    var = tk.StringVar()
    filt_cb = ttk.Combobox(nextrowframe, height=3, width=7,
                           exportselection=False,
                           state="readonly",
                           textvariable=var,
                           values=this.data_columns)

    cb_textvar = tk.StringVar()
    entry = ttk.Entry(nextrowframe, width=20, textvariable=cb_textvar)

    button_subt = ttk.Button(nextrowframe,
                             text='-',
                             width=1,
                             command=lambda rf=nextrowframe,
                                            w={}: remove_selection_row(rf, w))
    button_subt.bind('-', lambda ev, rf=nextrowframe,
                                 w={}: remove_selection_row(rf, w, ev))

    button_add = ttk.Button(nextrowframe,
                            text='+',
                            width=1,
                            command=lambda w={}: add_selection_row(w))
    button_add.bind('<Return>', add_selection_row)
    
    filt_cb.grid(row=0, column=0)
    entry.grid(row=0, column=1)
    button_subt.grid(row=0, column=2)
    button_add.grid(row=0, column=3)

    return nextrowframe


def add_selection_row(windows: dict) -> None:
    """Add a row of widgets to define a selection-from-list.
    
    uses variables from the calling module:
        item_rows
    """
    rows_gridded = [r for r in this.item_rows if len(r.grid_info().items()) > 0]
    num_gridded = len(rows_gridded)

    # relevant if using a pandas dataset
    # if num_gridded == len(this.data_columns):
    #     return

    newrow = create_selection_row(windows)
    this.item_rows.append(newrow)
    newrow.grid(row=num_gridded, column=0, sticky='nw')

    for row in rows_gridded:
        row.winfo_children()[3].grid_remove()

    if this.do_debug:
        print(f'in function: {sys._getframe().f_code.co_name}')
        print(f'...called by: {sys._getframe().f_back.f_code.co_name}')
        print(f'adding row')
        print(f'   {num_gridded} rows on grid:')
        for r in rows_gridded:
            print(f'   {r}')

        print(f'   ...new row {newrow} at row: {num_gridded}')
        print()


def remove_selection_row(rowframe: object, windows: dict, ev=None) -> None:
# def remove_selection_row2(ev, rowframe: object, windows: dict) -> None:
    """Remove a row of widgets specifying a selection-from-list.
    
    Data is automatically re-filtered by the remaining criteria.
    uses variables from the calling module:
        item_rows
        data_1: passed to my_fxn
    """
    # print(f'in remove_selection_row, rowframe is {type(rowframe)}')
    if rowframe not in this.item_rows:
        return
    
    rows_gridded = [r for r in this.item_rows if len(r.grid_info().items()) > 0]
    num_gridded = len(rows_gridded)

    # don't remove the only row
    if num_gridded == 1:
        return
    
    # clear filter for the row
    rowframe.winfo_children()[0].set('')
    rowframe.winfo_children()[1].delete(0, tk.END)

    rowframe.grid_forget()
    this.item_rows.remove(rowframe)
    
    for index, r in enumerate(this.item_rows):
        r.grid_forget()
        r.grid(row=index, column=0, sticky='nw')
    
    rows_now_gridded = [r for r in this.item_rows if len(r.grid_info().items()) > 0]
    rows_now_gridded[-1].winfo_children()[3].grid(row=0, column=3, sticky='nw')

    if this.do_debug:
        print(f'in function: {sys._getframe().f_code.co_name}')
        print(f'...called by: {sys._getframe().f_back.f_code.co_name}')
        print(f'removing row (item_rows: {len(item_rows)})')
        print(f'   {num_gridded} rows on grid:')
        for r in rows_gridded:
            print(f'   {r}')
        # print(f'   removing row {rem["row"]}')
        num_now_gridded = len(rows_now_gridded)
        print(f'   {num_now_gridded} rows now on grid: ')
        for index, r in enumerate(rows_now_gridded):
            print(f'   {r}')
        print()

    # Extra work resulting from the data selection.
    if this.my_fxn is not None:
        this.my_fxn(this.data_1, windows, rows_gridded)

    # An optional function from the calling module
    if this.opt_fxn is not None:
        this.opt_fxn()