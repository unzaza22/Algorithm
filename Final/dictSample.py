from DictFunction import DictFunction


class dictSample(DictFunction):

    def __init__(self,vocab_dict):
        # สร้าง dictionary ของคำศัพท์
        super.__init__(vocab_dict)

    super.vocab_dict = {
        'Hello': {'thai': 'สวัสดี', 'part_of_speech': 'interjection'},
        'Book': {'thai': 'หนังสือ', 'part_of_speech': 'noun'},
        'Run': {'thai': 'วิ่ง', 'part_of_speech': 'verb'},
        'Beautiful': {'thai': 'สวยงาม', 'part_of_speech': 'adjective'},
        'Fast': {'thai': 'เร็ว', 'part_of_speech': 'adjective'},
        'Peace': {'thai': 'สันติภาพ', 'part_of_speech': 'noun'},
        'Hope': {'thai': 'ความหวัง', 'part_of_speech': 'noun'},
        'Joy': {'thai': 'ความสุข', 'part_of_speech': 'noun'},
        'Friend': {'thai': 'เพื่อน', 'part_of_speech': 'noun'},
        'Love': {'thai': 'รัก', 'part_of_speech': 'noun'},
        'Eat': {'thai': 'กิน', 'part_of_speech': 'verb'},
        'Walk': {'thai': 'เดิน', 'part_of_speech': 'verb'},
        'Write': {'thai': 'เขียน', 'part_of_speech': 'verb'},
        'Study': {'thai': 'เรียน', 'part_of_speech': 'verb'},
        'Play': {'thai': 'เล่น', 'part_of_speech': 'verb'},
        'Warm': {'thai': 'อบอุ่น', 'part_of_speech': 'adjective'},
        'Cold': {'thai': 'หนาว', 'part_of_speech': 'adjective'},
        'Happy': {'thai': 'มีความสุข', 'part_of_speech': 'adjective'},
        'Sad': {'thai': 'เศร้า', 'part_of_speech': 'adjective'},
        'Tall': {'thai': 'สูง', 'part_of_speech': 'adjective'}
        # ... และเพิ่มคำอื่นๆ ให้ครบ 20 คำ
    }

    # ตัวอย่างการเข้าถึงข้อมูล
    word = 'Hello'
    translation = super.vocab_dict[word]['thai']
    part_of_speech = super.vocab_dict[word]['part_of_speech']

    print(f"Word ({word}) แปลว่า ({translation}) เป็นประเภท ({part_of_speech}).")
