import tkinter as tk
from tkinter import messagebox
import json
import random


class WordMeaningApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Meaning Learning Tool")
        self.master.geometry("500x400")
        self.master.configure(bg='#f5f5f5')

        # Load words and meanings from JSON file
        with open('words_meanings.json', 'r') as file:
            self.words_meanings = json.load(file)

        # Shuffle the words to randomize order
        random.shuffle(self.words_meanings)

        self.filtered_words = self.words_meanings
        self.index = 0

        # Create main frame
        self.main_frame = tk.Frame(self.master, bg='#ffffff', padx=20, pady=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Create and pack the search bar
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.main_frame, textvariable=self.search_var, font=('Arial', 14))
        self.search_entry.pack(pady=10, fill=tk.X)
        self.search_entry.bind('<KeyRelease>', self.filter_words)

        # Create and pack the heading label
        self.heading = tk.Label(self.main_frame, text='', font=('Arial', 28, 'bold'), bg='#ffffff', fg='#333333')
        self.heading.pack(pady=20)

        # Create and pack the meaning label
        self.meaning = tk.Label(self.main_frame, text='', font=('Arial', 18), bg='#ffffff', fg='#555555',
                                wraplength=460)
        self.meaning.pack(pady=10)

        # Create and pack the next button
        self.next_button = tk.Button(self.main_frame, text='Next', command=self.next_word, font=('Arial', 14),
                                     bg='#4CAF50', fg='#ffffff', borderwidth=0, relief='flat', padx=20, pady=10)
        self.next_button.pack(pady=20)

        # Create and pack the progress label
        self.progress_label = tk.Label(self.main_frame, text='', font=('Arial', 12), bg='#ffffff', fg='#777777')
        self.progress_label.pack()

        # Display the first word and meaning
        self.display_word_meaning()

    def filter_words(self, event):
        query = self.search_var.get().lower()
        self.filtered_words = [word for word in self.words_meanings if query in word['word'].lower()]
        self.index = 0
        self.display_word_meaning()

    def display_word_meaning(self):
        # Check if there are more words to display
        if self.index < len(self.filtered_words):
            word = self.filtered_words[self.index]['word']
            meaning = self.filtered_words[self.index]['meaning']
            self.heading.config(text=word)
            self.meaning.config(text=meaning)
            self.progress_label.config(text=f'Word {self.index + 1} of {len(self.filtered_words)}')
        else:
            messagebox.showinfo('Info', 'No more words!')
            self.index = 0  # Optionally reset index to start over

    def next_word(self):
        # Move to the next word
        self.index += 1
        self.display_word_meaning()


if __name__ == '__main__':
    root = tk.Tk()
    app = WordMeaningApp(root)
    root.mainloop()
