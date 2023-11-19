import tkinter as tk
from tkinter import messagebox, ttk


class DictApp():
    def __init__(self, root):
        self.root = root
        self.root.title('Dictionary Manager')

        # Dictionary to hold the vocabulary
        self.vocab_dict = {}

        # Widgets
        self.word_label = tk.Label(root, text='English Word:')
        self.word_entry = tk.Entry(root)
        self.translation_label = tk.Label(root, text='Thai Translation:')
        self.translation_entry = tk.Entry(root)
        self.part_of_speech_label = tk.Label(root, text='Part of Speech:')
        self.part_of_speech_entry = tk.Entry(root)
        self.add_button = tk.Button(root, text='Add Word', command=self.add_word)
        self.edit_button = tk.Button(root, text='Edit Word', command=self.edit_word)
        self.search_button = tk.Button(root, text='Search Word', command=self.search_word)
        self.remove_button = tk.Button(root, text='Remove Word', command=self.remove_word)

        # Listbox to display words
        self.words_listbox = tk.Listbox(root)
        self.refresh_word_list()

        # Layout for entry widgets
        self.word_label.grid(row=0, column=0, sticky='e')
        self.word_entry.grid(row=0, column=1)
        self.translation_label.grid(row=1, column=0, sticky='e')
        self.translation_entry.grid(row=1, column=1)
        self.part_of_speech_label.grid(row=2, column=0, sticky='e')
        self.part_of_speech_entry.grid(row=2, column=1)
        self.add_button.grid(row=3, column=0)
        self.edit_button.grid(row=3, column=1)
        self.search_button.grid(row=4, column=0)
        self.remove_button.grid(row=4, column=1)

    def add_word(self):
        word = self.word_entry.get()
        translation = self.translation_entry.get()
        part_of_speech = self.part_of_speech_entry.get()
        if word and translation and part_of_speech:
            self.vocab_dict[word] = {'thai': translation, 'part_of_speech': part_of_speech}
            messagebox.showinfo("Success", f"Added word '{word}' to dictionary.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "All fields are required.")

    def refresh_word_list(self):
        self.words_listbox.delete(0, tk.END)  # Clear the listbox
        for word in self.vocab_dict.keys():
            self.words_listbox.insert(tk.END, word)  # Insert new words

    def edit_word(self):
        # Similar to add_word but checks if the word is in the dictionary first
        pass

    def search_word(self):
        # Similar to edit_word but only displays the information
        pass

    def remove_word(self):
        # Similar to search_word but removes the word from the dictionary
        pass

    def clear_entries(self):
        self.word_entry.delete(0, tk.END)
        self.translation_entry.delete(0, tk.END)
        self.part_of_speech_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
app = DictApp(root)
root.mainloop()