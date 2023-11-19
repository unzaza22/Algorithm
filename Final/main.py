import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class DictionaryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dictionary GUI")
        self.geometry("600x400")

        # Initialize the dictionary with some words
        self.dictionary = {
            'Hello': {'Thai': 'สวัสดี', 'Part of speech': 'Interjection'},
            'Book': {'Thai': 'หนังสือ', 'Part of speech': 'Noun'},
            'Run': {'Thai': 'วิ่ง', 'Part of speech': 'Verb'},
            'Beautiful': {'Thai': 'สวยงาม', 'Part of speech': 'Adjective'},
            'Fast': {'Thai': 'เร็ว', 'Part of speech': 'Adjective'},
            'Peace': {'Thai': 'สันติภาพ', 'Part of speech': 'Noun'},
            'Hope': {'Thai': 'ความหวัง', 'Part of speech': 'Noun'},
            'Joy': {'Thai': 'ความสุข', 'Part of speech': 'Noun'},
            'Friend': {'Thai': 'เพื่อน', 'Part of speech': 'Noun'},
            'Love': {'Thai': 'รัก', 'Part of speech': 'Noun'},
            'Eat': {'Thai': 'กิน', 'Part of speech': 'Verb'},
            'Walk': {'Thai': 'เดิน', 'Part of speech': 'Verb'},
            'Write': {'Thai': 'เขียน', 'Part of speech': 'Verb'},
            'Study': {'Thai': 'เรียน', 'Part of speech': 'Verb'},
            'Play': {'Thai': 'เล่น', 'Part of speech': 'Verb'},
            'Warm': {'Thai': 'อบอุ่น', 'Part of speech': 'Adjective'},
            'Cold': {'Thai': 'หนาว', 'Part of speech': 'Adjective'},
            'Happy': {'Thai': 'มีความสุข', 'Part of speech': 'Adjective'},
            'Sad': {'Thai': 'เศร้า', 'Part of speech': 'Adjective'},
            'Tall': {'Thai': 'สูง', 'Part of speech': 'Adjective'},
            # ... Add the rest of your words here
        }
        self.sort_dictionary()  # เรียกใช้เมื่อโปรแกรมเริ่มทำงาน

        # Treeview widget
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("Thai", "Part of speech")
        self.tree.column("#0", width=120, minwidth=25)
        self.tree.column("Thai", width=160, minwidth=25)
        self.tree.column("Part of speech", width=120, minwidth=25)

        self.tree.heading("#0", text="English", anchor=tk.W)
        self.tree.heading("Thai", text="Thai Translation", anchor=tk.W)
        self.tree.heading("Part of speech", text="Part of Speech", anchor=tk.W)

        # Inserting the dictionary items into the Treeview
        for eng_word, details in sorted(self.dictionary.items()):
            self.tree.insert("", tk.END, text=eng_word, values=(details['Thai'], details['Part of speech']))

        # Place the Treeview in the window
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add 'Add Word' button
        self.add_word_button = ttk.Button(self, text="Add Word", command=self.add_word)
        self.add_word_button.pack(side=tk.LEFT, anchor=tk.W, padx=10, pady=10)

        # Add 'Delete Word' button
        self.delete_word_button = ttk.Button(self, text="Delete Word", command=self.delete_word)
        self.delete_word_button.pack(side=tk.LEFT, anchor=tk.W, padx=10, pady=0)

        # Add 'Edit Word' button
        self.edit_word_button = ttk.Button(self, text="Edit Word", command=self.edit_word)
        self.edit_word_button.pack(side=tk.LEFT, anchor=tk.W, padx=10, pady=0)

        search_frame = tk.Frame(self)
        search_frame.pack(side=tk.RIGHT, fill=tk.X, padx=10)

        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 10))

        self.search_button = ttk.Button(search_frame, text="Search", command=self.search_words)
        self.search_button.pack(side=tk.RIGHT)

        self.refresh_treeview()

    def refresh_treeview(self):
        # Clear the treeview
        for i in self.tree.get_children():
            self.tree.delete(i)
        # Inserting the updated dictionary items into the Treeview
        for eng_word, details in self.dictionary.items():
            self.tree.insert("", tk.END, text=eng_word, values=(details['Thai'], details['Part of speech']))

    def add_word(self):
        # Open a dialog to enter the English word
        english_word = simpledialog.askstring("Add Word", "Enter the English word:", parent=self)
        if english_word:
            # Check if the word already exists in the dictionary
            if english_word in self.dictionary:
                tk.messagebox.showerror("Error", "Word already exists!")
                return

            # Open dialogs to enter the Thai translation and part of speech
            thai_translation = simpledialog.askstring("Add Word", "Enter the Thai translation:", parent=self)
            part_of_speech = simpledialog.askstring("Add Word", "Enter the part of speech:", parent=self)

            if thai_translation and part_of_speech:
                # Add the new word to the dictionary
                self.dictionary[english_word] = {
                    'Thai': thai_translation,
                    'Part of speech': part_of_speech
                }
                # Update the treeview
                self.refresh_treeview()
            else:
                tk.messagebox.showerror("Error", "Invalid input. Please enter all information.")
        self.sort_dictionary()

    def delete_word(self):
        selected_item = self.tree.selection()  # Get the selected item
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a word to delete.")
            return
        word_to_delete = self.tree.item(selected_item)["text"]
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete the word '{word_to_delete}'?")
        if confirm:
            # Delete from the dictionary
            del self.dictionary[word_to_delete]
            # Delete from the Treeview
            self.tree.delete(selected_item)
            # You can refresh the Treeview or update the dictionary as needed here
            self.refresh_treeview()
        self.sort_dictionary()

    def edit_word(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a word to edit.")
            return
        word_to_edit = self.tree.item(selected_item)["text"]
        details = self.dictionary[word_to_edit]

        # Open a new dialog window to edit the word
        new_word = simpledialog.askstring("Edit Word", "Enter the new English word:", initialvalue=word_to_edit)
        if new_word is not None and new_word != "":
            new_translation = simpledialog.askstring("Edit Translation", "Enter the new Thai translation:",
                                                     initialvalue=details['Thai'])
            new_part_of_speech = simpledialog.askstring("Edit Part of Speech", "Enter the new part of speech:",
                                                        initialvalue=details['Part of speech'])

            # Check if the word was actually changed to avoid unnecessary updates
            if new_word != word_to_edit or new_translation != details['Thai'] or new_part_of_speech != details[
                'Part of speech']:
                # Update the dictionary
                self.dictionary[new_word] = {'Thai': new_translation, 'Part of speech': new_part_of_speech}
                if new_word != word_to_edit:
                    # If the word has been changed, delete the old entry
                    del self.dictionary[word_to_edit]

                # Update the Treeview
                self.tree.item(selected_item, text=new_word, values=(new_translation, new_part_of_speech))
                # Optional: You can refresh the Treeview here if necessary
                self.refresh_treeview()

    def search_words(self):
        search_term = self.search_entry.get().strip()
        # Clear the treeview
        for i in self.tree.get_children():
            self.tree.delete(i)
        # Go through the dictionary and insert the search results
        for eng_word, details in self.dictionary.items():
            if search_term.lower() in eng_word.lower():
                self.tree.insert("", tk.END, text=eng_word, values=(details['Thai'], details['Part of speech']))

    def sort_dictionary(self):
        try:
            # Ensure the dictionary exists and is a dictionary
            if hasattr(self, 'dictionary') and isinstance(self.dictionary, dict):
                # Perform the sorting
                sorted_dict = dict(sorted(self.dictionary.items(), key=lambda item: item[0]))
                self.dictionary = sorted_dict
                self.refresh_treeview()  # Update the TreeView after sorting
            else:
                print("Dictionary is not initialized or is not a dictionary.")
        except Exception as e:
            print(f"An error occurred while sorting the dictionary: {e}")


if __name__ == "__main__":
    app = DictionaryApp()
    app.mainloop()
