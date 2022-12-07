import tkinter as tk

from Interface.page_home import PageHome
from Interface.page_fst import PageFST
from Interface.page_hash_table import PageHashTable
from Interface.page_levenshtein import PageLevenshtein

from FSTInterpreter.fst import FST
from HashTable.hash_table import txt2hashtable


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args,  **kwargs)
        self.geometry("380x530")
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        fst = FST("fst.json")
        (hash_dict, hash_list) = txt2hashtable("dictionary.txt")

        self.frames = {}

        for F in (PageHome, PageFST, PageHashTable, PageLevenshtein):
            page_name = F.__name__
            
            if page_name == PageHashTable.__name__:
                frame = F(parent=self.container, controller=self, dict=hash_dict, list=hash_list)    
            elif page_name == PageHome.__name__:
                frame = F(parent=self.container, controller=self)
            else: frame = F(parent=self.container, controller=self, fst=fst)

            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageHome")

    def show_frame(self, page_name, update=False):
        '''Show a frame for the given page name'''
        self.frames[page_name].update_content()
        self.frames[page_name].tkraise()


# if __name__ == "__main__":
#     app = App()
#     app.title("Auto Complete Program")
#     app.mainloop()
