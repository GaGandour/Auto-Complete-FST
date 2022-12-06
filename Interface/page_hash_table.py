import tkinter as tk
from Interface.page import Page


class PageHashTable(Page):
    page_path = "Menu > Autocomplete Hash Table"

    def __init__(self, parent, controller):
        super().__init__(parent, controller, PageHashTable.page_path)
        self.controller = controller

        # main content widgets
        
        # action buttons widgets
        