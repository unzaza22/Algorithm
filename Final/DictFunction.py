class DictFunction:

    def __init__(self, vocab_dict):
        self.vocab_dict = vocab_dict

    def addWord(self):
        english_word = input("Enter the English word: ")
        if english_word in self.vocab_dict:
            print(f"The word '{english_word}' is already in the dictionary.")
        else:
            thai_translation = input("Enter the Thai translation: ")
            part_of_speech = input("Enter the part of speech: ")
            self.vocab_dict[english_word] = {
                'thai': thai_translation,
                'part_of_speech': part_of_speech
            }
            print(f"The word '{english_word}' was added to the dictionary.")

    def removeWord(self):
        english_word = input("Enter the English word to remove: ")
        if english_word in self.vocab_dict:
            del self.vocab_dict[english_word]
            print(f"The word '{english_word}' has been removed from the dictionary.")
        else:
            print(f"The word '{english_word}' was not found in the dictionary.")

    def searchWord(self):
        english_word = input("Enter the English word to search: ")
        if english_word in self.vocab_dict:
            thai_translation = self.vocab_dict[english_word]['thai']
            part_of_speech = self.vocab_dict[english_word]['part_of_speech']
            print(f"Word: {english_word}")
            print(f"Translation: {thai_translation}")
            print(f"Part of Speech: {part_of_speech}")
        else:
            print(f"The word '{english_word}' was not found in the dictionary.")

    def editWord(self):
        english_word = input("Enter the English word to edit: ")
        if english_word in self.vocab_dict:
            new_thai_translation = input("Enter the new Thai translation: ")
            new_part_of_speech = input("Enter the new part of speech: ")
            self.vocab_dict[english_word] = {
                'thai': new_thai_translation,
                'part_of_speech': new_part_of_speech
            }
            print(f"The word '{english_word}' has been updated in the dictionary.")
        else:
            print(f"The word '{english_word}' was not found in the dictionary.")