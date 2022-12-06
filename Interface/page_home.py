import tkinter as tk
from page import Page


class PageHome(Page):
    page_path = "Menu"

    def __init__(self, parent, controller):
        super().__init__(parent, controller, PageHome.page_path)
        self.controller = controller

        # main content widgets
        text1 = tk.Label(self, text="Bem-vindo ao Autocomplete!")
        text1.pack()
        button1 = tk.Button(self,
                            width=30,
                            text="Autocomplete FST",
                            command=lambda: controller.show_frame("PageFST"))
        button1.pack(pady=(10, 0))
        # button2 = tk.Button(self,
        #                     width=30,
        #                     text="Autocomplete HashTable",
        #                     command=lambda: controller.show_frame("PageHashTable"))
        # button2.pack(pady=(10, 0))
