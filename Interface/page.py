import tkinter as tk


class Page(tk.Frame):
    page_path = "Error"

    def __init__(self, parent, controller, page_path):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # top menu widgets
        menu_frame = tk.Frame(self)
        menu_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        page_status = tk.Label(menu_frame, text=page_path)
        page_status.pack(side=tk.LEFT)
        exit_button = tk.Button(menu_frame,
                                text='✕',
                                command=self.quit)
        exit_button.pack(side=tk.RIGHT)

    def update_content(self):
        pass
