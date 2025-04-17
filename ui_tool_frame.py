"""
module: ui_tool_frame.py

purpose: provide custom tkinter widget classes for a Frame with a row of
         widgets.

comments: adapted from rf_custom_ui.py, to use different child widgets.

author: Russell Folks

history:
-------
09-21-2024  creation
10-16-2024  Committed to GitHub repository ui_RF.
04-17-2025  Add create_spinbox(). Modify some lambdas to same format as
            custom classes in other modules.
"""
"""
"""

import tkinter as tk
from tkinter import ttk

class ToolFrame(ttk.Frame):
    """
    ToolFrame : Defines a Frame, containing a row of widgets.

    Extends: ttk.Frame

    Attributes
    ----------
    label_name: str
        text of the Label.

    Methods
    -------
    create_widgets:
        add widget children to the Frame.
    """
    def __init__(self, parent, 
                       cb_values=['1', '2', '3'],
                       display_name='',
                       name='',
                       var=None,
                       callb=None,
                       posn=None,
                       stick='w'
                 ):
        """
        Inits a ToolFrame object.

        Parameters
        ----------
        cb_values : list
            values passed through to a Combobox.
        var : str
            variable name.
        post : function
            callback for the ComboboxSelected event.
        posn : list
            row and column for gridding child objects.
        display_name : str
            used to construct the text of the Label.
        name : str
            name attribute of the Combobox.

        Methods
        -------
        create_widgets:
            Creates and displays the widgets.
        props:
            Returns the parameter list for an instance of the class.
        """
        super().__init__(parent)
        
        self.cb_values = cb_values
        self.var = var
        self.callb = callb
        self.posn = posn
        self.display_name = display_name
        self.name = name
        self.stick = stick

        self.sep = ': '

        # self.label_name = self.display_name[0].upper() + self.display_name[1:] + self.sep
        # self.label_name = self.display_name.title() + self.sep

        self.create_widgets()
        self.grid(row=self.posn[0], column=self.posn[1], padx=5, pady=10, sticky=self.stick)

    def create_widgets(self):
        # self.lab = ttk.Label(self,
        #                 text=self.label_name)

        # could add a postcommand attribute, which executes before the callb.
        self.cb = ttk.Combobox(self,
                          height=3,
                          width=10,
                          exportselection=False,
                          state='readonly',
                          name=self.name,
                          values=self.cb_values,
                          textvariable=self.var
                          )
        self.cb.bind('<<ComboboxSelected>>', self.callb)        
        self.cb.current(0)

        cb_textvar = tk.StringVar()
        entry = ttk.Entry(self, width=7, textvariable=cb_textvar)

        button_subt = ttk.Button(self,
                                text='-',
                                width=1,
                                # command=lambda rf=self:
                                #                remove_selection_row(rf))
                                 command=lambda rf=self,
                                                w=windows: remove_selection_row(rf, w))

        button_add = ttk.Button(nextrowframe,
                                text='+',
                                width=1,
                                command=add_selection_row())
                                # command=lambda: add_cb_textvar_row(windows))


        self.lab.pack(side='left')#, fill='x')
        self.cb.pack(side='left')#, fill='x')

        # self.grid(row=self.posn[0], column=self.posn[1], padx=5, pady=10, sticky=self.stick)

    def create_spinbox(self):
        sb = ttk.Spinbox(self,
                         width=3,
                         from_=1,
                         to=10,
                         values=self.cb_values,
                         wrap=True,
                         textvariable=self.var,
                         command=self.callb
        )
        return sb
