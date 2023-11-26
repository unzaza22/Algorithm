class Word:
    def __init__(self, english, thai, word_type):
        self.english = english
        self.thai = thai
        self.word_type = word_type

    def __str__(self):
        return f"{self.english} ({self.word_type}): {self.thai}"

initial_words = [
    Word("apple", "แอปเปิ้ล", "noun"),
    Word("banana", "กล้วย", "noun"),
    Word("run", "วิ่ง", "verb"),
    Word("hello", "สวัสดี", "interjection"),
    Word("book", "หนังสือ", "noun"),
    Word("beautiful", "สวย", "adjective"),
    Word("fast", "เร็ว", "adjective"),
    Word("peace", "สันติภาพ", "noun"),
    Word("hope", "ความหวัง", "noun"),
    Word("joy", "ความสุข", "noun"),
    Word("friend", "เพื่อน", "noun"),
    Word("love", "ความรัก", "noun"),
    Word("eat", "กิน", "verb"),
    Word("walk", "เดิน", "verb"),
    Word("write", "เขียน", "verb"),
    Word("study", "เรียน", "verb"),
    Word("play", "เล่น", "verb"),
    Word("warm", "อบอุ่น", "adjective"),
    Word("cold", "หนาว", "adjective"),
    Word("happy", "มีความสุข", "adjective"),
    # เพิ่มคำศัพท์อื่นๆ ตามนี้
]

# สร้าง Dictionary และเพิ่มคำศัพท์เหล่านี้
dictionary = {}
for word in initial_words:
    dictionary[word.english] = word

def add_word(dictionary, word):
    if word.english not in dictionary:
        dictionary[word.english] = word
        print("Word added successfully.")
    else:
        print("Word already exists.")

def find_word(dictionary, english):
    return dictionary.get(english, "Word not found.")

def update_word(dictionary, english, new_thai=None, new_word_type=None):
    if english in dictionary:
        if new_thai:
            dictionary[english].thai = new_thai
        if new_word_type:
            dictionary[english].word_type = new_word_type
        print("Word updated successfully.")
    else:
        print("Word not found.")

def delete_word(dictionary, english):
    if english in dictionary:
        del dictionary[english]
        print("Word deleted successfully.")
    else:
        print("Word not found.")

def display_dictionary(dictionary):
    if dictionary:
        # ใช้ฟังก์ชัน sorted() เพื่อเรียงลำดับคำศัพท์
        sorted_words = sorted(dictionary.keys())
        for word_key in sorted_words:
            print(dictionary[word_key])
    else:
        print("The dictionary is empty.")


while True:
    print("\nDictionary CRUD App")
    print("1. Add a new word")
    print("2. Find a word")
    print("3. Update a word")
    print("4. Delete a word")
    print("5. Display all words")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        eng = input("Enter English word: ")
        thai = input("Enter Thai translation: ")
        word_type = input("Enter word type: ")
        add_word(dictionary, Word(eng, thai, word_type))

    elif choice == "2":
        eng = input("Enter English word to find: ")
        print(find_word(dictionary, eng))

    elif choice == "3":
        eng = input("Enter English word to update: ")
        new_thai = input("Enter new Thai translation (press enter to skip): ")
        new_word_type = input("Enter new word type (press enter to skip): ")
        update_word(dictionary, eng, new_thai, new_word_type)

    elif choice == "4":
        eng = input("Enter English word to delete: ")
        delete_word(dictionary, eng)

    elif choice == "5":
        display_dictionary(dictionary)

    elif choice == "6":
        break
