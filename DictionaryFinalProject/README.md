# ไฟล์ที่ส่ง Final คือ DictionaryBST
# class Word
class นี้มีไว้เก็บคำศัพท์ เพื่อส่งข้อมูลคำศัพท์

english = คำศัพท์ภาษาอังกฤษ

thai = คำแปล

word_type = ประเภทของคำศัพท์

# class TreeNode
class นี้สร้างไว้เพื่อกำหนด key ของคำศัพท์และอยู่ Node ทางซ้ายหรือทางขวา

# class BinarySearchTree
class นี้จะเป็นตัว algorithm ในการทำงานของ BST

**insert** จะตรวจสอบว่า root เป้น None ไหม ถ้าใช้ insert จะสร้าง Node ขึ้นมา แต่ถ้า root ไม่เป็น None insert จะเปรียบเทียบค่าของ Node ว่ามีค่า key **น้อยกว่า(<)** หรือ **มากกว่า(>)** ถ้า **น้อยกว่า(<)** จะเอาไว้ทางซ้าย **มากกว่า(>)** เอาไว้ทางขวาของ Node

**search** จะค้นหา Node ที่มี **น้อยกว่า(<)** ก่อนเสมอ เลยทำให้ algorithm ค้นหา Node ไปทางด้านซ้ายก่อนเสมอ เป็นที่มาของทฤษฏี O(n)

**in_order_traversal** ถ้า node ไหน root ไม่เป็น None หรือก็คือ node ตำแหน่งสุดท้าย การทำงานก็จะไม่หยุดหรือก็คือ แสดงคำศัพท์ทั้งหมด

**delete** จะค้นหา Node ที่ต้องลบ ถ้าค่าของ Node **น้อยกว่า(<)** จะค้นหาทางซ้าย ถ้า **มากกว่า(>)** จะค้นหาในทางขวาเป็น O(n) เหมือนกันแต่ด้วยมีการกำหนดค่าของ Node ที่ชัดเจนเลยทำงานได้ดี

**next** จะค้นหาค่าที่ **มากกว่า(>)** ค่าของตัวเอง แต่น้อยที่สุดของ Node เพื่อค้นหาค่าของ key ที่อยู่ถัดไปจาก key ที่ต้องการ

**previous** จะค่าหาค่าที่ **น้อยกว่า(<)** ค่าของตัวเอง แต่มากที่สุดของ Node เพื่อค้นหาค่าของ key ที่อยู่ก่อนหน้าจาก key ที่ต้องการ

## คำศัพท์เริ่มต้นของ program
apple (noun): แอปเปิ้ล

banana (noun): กล้วย

beautiful (adjective): สวย

book (noun): หนังสือ

cold (adjective): หนาว

eat (verb): กิน

fast (adjective): เร็ว

friend (noun): เพื่อน

happy (adjective): มีความสุข

hello (interjection): สวัสดี

hope (noun): ความหวัง

joy (noun): ความสุข

love (noun): ความรัก

peace (noun): สันติภาพ

play (verb): เล่น

run (verb): วิ่ง

study (verb): เรียน

walk (verb): เดิน

warm (adjective): อบอุ่น

write (verb): เขียน

## คำสั่ง command-line
กด 1. Add a new word : เพิ่มคำศัพท์

กด 2. Find a word : ค้นหาคำศัพท์

กด 3. Update a word : แก้ไขคำศัพท์

กด 4. Delete a word : ลบคำศัพท์

กด 5. Display all words : แสดงคำศัพท์ทั้งหมด

กด 6. Find next word : ค้นหาคำศัพที่อยู่ถัดไป เช่น คำศัพท์ถัดไปของ hello คือ hope

กด 7. Find previous word : ค้าหาคำศัพท์ที่อยู่ก่อนหน้า เช่น คำศัพท์ที่อยู่ก่อนหน้า hello คือ happy

กด 8. Exit : ออกจาก command-line

### Hash Table
เนื่องด้วย algorithm hash table การทำงานเป็น O(1) ไม่มีการจัดเรียง data ที่ดีพอจึงไม่สามารถทำ next และ previous ได้ ซึ่่งถ้าจะทำต้องสร้าง key เพื่อรองรับแบบ BST ก็ใช้ BST เลยน่าจะดีกว่า

### Binary Search Tree
เนื่องด้วย BST มีการจัดเรียงลำดับของ data ด้วย key และ word(คำศัพท์) เพื่อเปรียบเทียบค่าของตัวอักษรและตัวเลขแล้วบันทึก data ในลักษณะต้นไม้ มากกว่าบันทึกไปที่ node ขวา และน้อยกว่าบันทึกไปที่ node ซ้าย แต่ด้วยการทำงานของ BST เป็น O(n) ในการใช้งาน function เช่น search มีแนวโน้มที่จะมากกว่า hash table
