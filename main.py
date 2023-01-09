import tkinter as tk
import os


class NotesApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Notes App")

        self.text = tk.Text(self.window)
        self.text.pack()

        menubar = tk.Menu(self.window)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.save_note)
        filemenu.add_command(label="Clear", command=self.clear_note)
        menubar.add_cascade(label="File", menu=filemenu)
        self.window.config(menu=menubar)

    def run(self):
        self.window.mainloop()

    def save_note(self):
        note = self.text.get("1.0", "end-1c")
        with open("notes.txt", "a") as f:
            f.write(note)
        self.text.delete("1.0", "end")

    def clear_note(self):
        self.text.delete("1.0", "end")


app = NotesApp()
app.run()
