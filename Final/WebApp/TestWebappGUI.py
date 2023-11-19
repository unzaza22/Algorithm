from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# สมมุติว่าพจนานุกรมของคุณมีโครงสร้างตามที่แสดงในตัวอย่าง tkinter
dictionary = {
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
    # ... คำศัพท์อื่นๆ ...
}

@app.route('/')
def index():
    # เรียงลำดับพจนานุกรมและเอา 20 รายการแรก
    sorted_words = dict(sorted(dictionary.items())[:40])
    # เรนเดอร์เทมเพลต, ส่งคำศัพท์ที่เรียงลำดับไป
    return render_template('index.html', dictionary=sorted_words)


@app.route('/add_word', methods=['GET', 'POST'])
def add_word():
    if request.method == 'POST':
        english_word = request.form['english_word']
        # ... รับข้อมูลอื่นๆ ...

        if english_word not in dictionary:
            # เพิ่มคำศัพท์ลงในพจนานุกรม
            # ...
            flash('Word added successfully!', 'success')
        else:
            # แสดงข้อความแจ้งเตือนว่าคำศัพท์นั้นมีอยู่แล้ว
            flash('Error: That word already exists!', 'error')

        return redirect(url_for('index'))
    # ถ้าเป็น GET request, เพียงแค่แสดงหน้ากับแบบฟอร์ม
    return render_template('add_word.html')


if __name__ == '__main__':
    app.run(debug=True)
