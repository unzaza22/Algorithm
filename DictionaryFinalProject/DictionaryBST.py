class Word:
    def __init__(self, english, thai, word_type):
        self.english = english
        self.thai = thai
        self.word_type = word_type

    def __str__(self):
        return f"{self.english} ({self.word_type}): {self.thai}"

class TreeNode:
    def __init__(self, key, word):
        self.key = key
        self.word = word
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, word):
        if self.root is None:
            self.root = TreeNode(key, word)
        else:
            self._insert_recursively(self.root, key, word)

    def _insert_recursively(self, node, key, word):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key, word)
            else:
                self._insert_recursively(node.left, key, word)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key, word)
            else:
                self._insert_recursively(node.right, key, word)

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None or key == node.key:
            return node
        elif key < node.key:
            return self._search_recursively(node.left, key)
        else:
            return self._search_recursively(node.right, key)

    # Methods for in-order traversal to display all words
    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.word)
            self.in_order_traversal(node.right)

    def delete(self, key):
        self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursively(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursively(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            node.key = self._min_value_node(node.right).key
            node.word = self._min_value_node(node.right).word

            # Delete the inorder successor
            node.right = self._delete_recursively(node.right, node.key)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def next(self, key):
        current = self.search(key)
        if current is None:
            return None
        if current.right:
            return self._min_value_node(current.right).word
        else:
            successor = None
            ancestor = self.root
            while ancestor != current:
                if current.key < ancestor.key:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor.word if successor else None

    def _max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def previous(self, key):
        current = self.search(key)
        if current is None:
            return None
        if current.left:
            return self._max_value_node(current.left).word
        else:
            predecessor = None
            ancestor = self.root
            while ancestor != current:
                if current.key > ancestor.key:
                    predecessor = ancestor
                    ancestor = ancestor.right
                else:
                    ancestor = ancestor.left
            return predecessor.word if predecessor else None


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

# สร้างต้นไม้ค้นหาแบบไบนารี
bst = BinarySearchTree()
# แทนที่การใช้ dictionary, เพิ่มคำศัพท์ใน BST
for word in initial_words:
    bst.insert(word.english, word)

# ปรับแต่งฟังก์ชันต่างๆ ให้ใช้ BST
def add_word(bst, english, thai, word_type):
    if bst.search(english) is None:
        new_word = Word(english, thai, word_type)
        bst.insert(english, new_word)
        print("Word added successfully.")
    else:
        print("Word already exists.")

# ทดแทนฟังก์ชันอื่นๆ อย่างเช่น find_word, update_word, delete_word, display_dictionary
def find_word(bst, english):
    node = bst.search(english)
    if node is not None:
        return node.word
    else:
        return "Word not found."

def update_word(bst, english, new_thai=None, new_word_type=None):
    node = bst.search(english)
    if node is not None:
        if new_thai:
            node.word.thai = new_thai
        if new_word_type:
            node.word.word_type = new_word_type
        print("Word updated successfully.")
    else:
        print("Word not found.")


# ฟังก์ชัน delete_word สำหรับการลบคำศัพท์
def delete_word(bst, english):
    if bst.search(english) is not None:
        bst.delete(english)
        print("Word deleted successfully.")
    else:
        print("Word not found.")
# ...

# ใช้ in_order_traversal ในการแสดงคำศัพท์ทั้งหมด
def display_all_words(bst):
    bst.in_order_traversal(bst.root)

# ปรับปรุงลูปและการโต้ตอบกับผู้ใช้
while True:
    print("\nDictionary CRUD App")
    print("1. Add a new word")
    print("2. Find a word")
    print("3. Update a word")
    print("4. Delete a word")
    print("5. Display all words")
    print("6. Find next word")
    print("7. Find previous word")
    print("8. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        eng = input("Enter English word: ")
        thai = input("Enter Thai translation: ")
        word_type = input("Enter word type: ")
        add_word(bst, eng, thai, word_type)

    elif choice == "2":
        eng = input("Enter English word to find: ")
        print(find_word(bst, eng))

    elif choice == "3":
        eng = input("Enter English word to update: ")
        new_thai = input("Enter new Thai translation (press enter to skip): ")
        new_word_type = input("Enter new word type (press enter to skip): ")
        update_word(bst, eng, new_thai, new_word_type)

    elif choice == "4":
        eng = input("Enter English word to delete: ")
        delete_word(bst, eng)

    elif choice == "5":
        display_all_words(bst)

    elif choice == "6":
        eng = input("Enter English word to find the next: ")
        next_word = bst.next(eng)
        print(f"Next word: {next_word}" if next_word else "No next word found.")

    elif choice == "7":
        eng = input("Enter English word to find the previous: ")
        previous_word = bst.previous(eng)
        print(f"Previous word: {previous_word}" if previous_word else "No previous word found.")

    elif choice == "8":
        break
# ...

