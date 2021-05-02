import os
import tkinter as tk
from tkinter import filedialog
import chart_lyrics_fixer


class GUI(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        self.make_widgets()
        self.file_path = ''
        self.output_folder_name = ''
        self.status = ''

    def make_widgets(self):
        self.winfo_toplevel().title('ChartLyricsFixer')

        self.choose_file_text = tk.Label(self, text='Input file')
        self.choose_file_text.grid(row=1, column=1, sticky='w')
        self.file_path_box = tk.Entry(self, state='disabled')
        self.file_path_box.grid(row=1, column=2)
        self.choose_file_button = tk.Button(self, text='Browse', command=self.choose_file)
        self.choose_file_button.grid(row=1, column=3)

        self.start_button = tk.Button(self, text='Fix lyrics', command=self.fix_lyrics)
        self.start_button.grid(row=3, column=2, stick='we')

    def choose_file(self):
        self.file_path_box.configure(state='normal')
        self.file_path_box.delete(0, tk.END)
        self.file_path = filedialog.askopenfilename(parent=root, filetypes=[('Charts', '.chart')])
        self.file_path_box.insert(0, self.file_path)
        self.file_path_box.configure(state='disabled')
        self.file_name = os.path.basename(self.file_path)

    def fix_lyrics(self):
        chart_lyrics_fixer.lyricise_file(self.file_path)
        print('Complete')


if __name__ == '__main__':
    root = tk.Tk()
    GUI(root)
    root.iconbitmap('icon.ico')
    root.mainloop()
