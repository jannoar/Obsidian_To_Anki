#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilenames


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x300')
        self.first_dollar = True
        self.processed_text = ''
        self.processed_filename = 'flashcards_processed.md'
        self.files_to_be_processed = []
        self.processed_filenames = []

        self.button = ttk.Button(self, text='Click',
                                 command=self.get_filename)
        self.button.pack()

        self.edit_button = ttk.Button(self, text='Edit',
                                      command=self.edit_file)
        self.edit_button.pack()

    def get_filename(self):
        self.files_to_be_processed = askopenfilenames()
        for fn in self.files_to_be_processed:
            self.processed_filenames.append(fn[:-3] +
                                            '_processed.md')

        self.fileList = ttk.Label(self, text=f'{self.files_to_be_processed}')
        self.fileList.pack()

    def edit_file(self):
        for file in range(len(self.files_to_be_processed)):
            self.processed_text = ''
            with open(self.files_to_be_processed[file], 'r') as f:
                text = f.read()

                for i in range(len(text)):
                    if text[i] == '$' and (text[i-1]) != '\\':
                        if self.first_dollar is True:
                            self.processed_text += r'\('
                            self.first_dollar = False
                        else:
                            self.processed_text += r'\)'
                            self.first_dollar = True
                    else:
                        self.processed_text += text[i]

            with open(self.processed_filenames[file], 'w') as f:
                f.write(self.processed_text)


if __name__ == '__main__':
    app = App()
    app.mainloop()
