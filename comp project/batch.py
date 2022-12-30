import csv
import matplotlib.pyplot as plt

def batch_add():
    with open("batch.csv", "a",newline="") as obj:
        wobj=csv.writer(obj)
        while True:
            id=input("Enter Batch ID ")
            bname=input("Enter Batch Name ")
            data=[id,bname]
            wobj.writerow(data)
            while True:
                dname = input("Enter Department Name ")
                record=[dname]
                wobj.writerow(record)
                while True:
                    clist=input("Enter course ")
                    record2 = [clist," "," "," "]
                    wobj.writerow(record2)
                    while True:
                        x=0
                        sname = input("Enter student name ")
                        sroll = int(input("Enter class roll "))
                        k=[int(i) for i in input("Enter marks out of 100 obtained in different subjects ").split()]
                        for j in k:
                            x=x+j
                        tmarks=x/len(k)
                        record3=[sname,str(sroll),str(tmarks)]
                        wobj.writerow(record3)
                        ch = input("exit to exit, any other key to continue ")
                        if ch == "exit":
                            break
                    ch = input("exit to exit, any other key to continue ")
                    if ch == "exit":
                        break
                ch = input("exit to exit, any other key to continue ")
                if ch == "exit":
                    break
            ch=input("exit to exit, any other key to continue ")
            if ch=="exit":
                break

def display_students():
    with open("batch.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==3:
                print(i)

def display_courses():
    with open("batch.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==4:
                print(i[0])

def pie_chart():
    name=[]
    marks=[]
    with open("batch.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==3:
                name.append(i[0])
                marks.append(i[2])
    plt.pie(marks,labels=name)
    plt.title("% MARKS DISTRIBUTION")
    plt.show()

#batch_add()
#display_students()
#display_courses()
#pie_chart()
