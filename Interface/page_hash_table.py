import tkinter as tk
from Interface.page import Page




        # main content widgets
        
        # action buttons widgets
        
import tkinter as tk
from Interface.page import Page
from HashTable.hash_table import dict_constains_word


class PageHashTable(Page):
    page_path = "Menu > Autocomplete Hash Table"

    def __init__(self, parent, controller, dict, list):
        super().__init__(parent, controller, PageHashTable.page_path)
        self.controller = controller
        self.dict = dict
        self.list = list
        self.data = dict_constains_word(dict, list, "", 10)
        
        # input frame and content
        input_frame = tk.LabelFrame(self, width=340, height=100, text="Entrada Autocomplete Hash Table")
        input_frame.pack(pady=(10, 0))
        input_frame.pack_propagate(0)
        
        input_label = tk.Label(input_frame, width=30, text="Palavra a ser pesquisada :", anchor='w')
        input_label.pack(side=tk.TOP)
        self.input_entry = tk.Entry(input_frame, width=30)
        self.input_entry.insert(0, "")
        self.input_entry.pack(side=tk.TOP, pady = (10,0))
        self.input_entry.bind("<KeyRelease>", self.check)

        # output frame and content
        output_frame = tk.LabelFrame(self, width=340, height=270, text="Saída Autocomplete Hash Table")
        output_frame.pack(pady=(10, 0))
        output_frame.pack_propagate(0)

        self.output_subframe = tk.Frame(output_frame)
        self.output_subframe.pack(pady=(20, 0))

        # action buttons widgets
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=(20, 0))
        button1 = tk.Button(buttons_frame, text='Retornar para o menu', command=lambda: controller.show_frame("PageHome"))
        button1.pack()


    def check(self, e):
        typed = self.input_entry.get()
        self.data = dict_constains_word(self.dict, self.list, typed, 10)
        self.update_content()


    def erase_old_words(self):
        for widget in self.output_subframe.winfo_children():
            widget.destroy()


    def write_curr_words(self):
        listbox = tk.Listbox(self.output_subframe, activestyle=tk.NONE, width= 30)
        listbox.pack(side=tk.LEFT, padx=(10, 10))
        for word in self.data:
            listbox.insert(tk.END, word)


    def update_content(self):
        self.erase_old_words()
        self.write_curr_words()
