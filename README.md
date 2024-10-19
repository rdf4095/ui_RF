# ui_RF

PURPOSE
-------
Custom user interface classes and functions


DEPENDENCIES
------------
importlib.machinery (optional, if you don't copy this to your same folder
                     as your python code.)
tkinter             - may need to install, on linux


OPERATION
---------
It is recommended to put the ui_RF folder at the same level as the
folder that holds your python project code, then import using:

   from importlib.machinery import SourceFileLoader
   msel = SourceFileLoader("ui_multi_select", "../ui_RF/ui_multi_select.py").load_module()

Any alias is ok, 'msel' is an example, but remember to prefix objects or 
functions with 'msel.'

Classes in ui_tool_frame.py

   ToolFrame, an extension of ttk.Frame that includes a horizontal set of
   widgets: Combobox, Entry and 2 Buttons. Combobox is passed a set of values, and the Entry is for user-selected text. 
   Both widgets have variables for retrieving their values and passing them to your main routine. Rows (i.e. new ToolFrames) 
   can be added or removed using the Buttons labeled '+' and '-', respectively.

   ToolFrame supports introspection.

Functions in ui_multi_select.py

   add_selection_row
   remove_selection_row
   create_selection_row
