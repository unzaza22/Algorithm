import time
import random
import matplotlib.pyplot as plt

def bubbleSort(num_list):
  for outter in range(len(num_list)-1,0,-1):
    for i in range(outter):
      if num_list[i]>num_list[i+1]:
        temp = num_list[i]
        num_list[i] = num_list[i+1]
        num_list[i+1] = temp

def selectionSort(num_list):
  for fillslot in range(len(num_list)-1,0,-1):
    maxpos = 0
    for location in range(1,fillslot+1):
      if num_list[location]>num_list[maxpos]:
        maxpos = location

    temp = num_list[fillslot]
    num_list[fillslot] = num_list[maxpos]
    num_list[maxpos] = temp

def insertSort(num_list):
  for index in range(1,len(num_list)):

    currentvalue = num_list[index]
    position = index

    while position>0 and num_list[position-1]>currentvalue:
      num_list[position]=num_list[position-1]
      position = position-1

    num_list[position]=currentvalue

bubble_List = []
selection_List = []
insert_List = []

def bubble_Run():
    for Random in range(2000,10001,+2000):
        random_Sample = random.sample(range(1, Random+1), Random)
        total_List = []
        for x in range(10):
            start_time = time.time()
            bubbleSort(random_Sample)
            end_time = time.time()

            total_time = end_time-start_time
            total_List.append(total_time)

        bubble_List.append(min(total_List))

def selection_Run():
    for Random in range(2000,10001,+2000):
        random_Sample = random.sample(range(1, Random+1), Random)
        total_List = []
        for x in range(10):
            start_time = time.time()
            selectionSort(random_Sample)
            end_time = time.time()

            total_time = end_time-start_time
            total_List.append(total_time)

        selection_List.append(min(total_List))

def insert_Run():
    for Random in range(2000,10001,+2000):
        random_Sample = random.sample(range(1, Random+1), Random)
        total_List = []
        for x in range(10):
            start_time = time.time()
            insertSort(random_Sample)
            end_time = time.time()

            total_time = end_time-start_time
            total_List.append(total_time)

        insert_List.append(min(total_List))

bubble_Run()
selection_Run()
insert_Run()

print(bubble_List)
print(selection_List)
print(insert_List)

# ข้อมูล
x = [2000, 4000, 6000, 8000, 10000]
y1 = [bubble_List[0], bubble_List[1], bubble_List[2], bubble_List[3], bubble_List[4]]
y2 = [selection_List[0], selection_List[1], selection_List[2], selection_List[3], selection_List[4]]
y3 = [insert_List[0], insert_List[1], insert_List[2], insert_List[3], insert_List[4]]

# วาดเส้นกราฟ
plt.plot(x, y1, label='Bubble', color='r', marker='o')
plt.plot(x, y2, label='Selection', color='g', marker='x')
plt.plot(x, y3, label='Insert', color='b', marker='s')

# ตั้งชื่อแกน x, y และชื่อกราฟ
plt.xlabel('NumList')
plt.ylabel('Time/sec')
plt.title('Sorting Graph')

# แสดง legend
plt.legend()

# แสดงกราฟ
plt.show()