import csv
import matplotlib.pyplot as plt

def batch_add():
    with open("batch.csv", "a",newline="") as obj:
        wobj=csv.writer(obj)
        while True:
            bid=input("Enter Batch ID ")
            bname=input("Enter Batch Name ")
            dname = input("Enter Department ID ")
            cname=input("Enter Course ID ")
            sid = input("Enter Student ID ")
            record=[bid,bname,dname,cname,sid]
            wobj.writerow(record)
            ch = input("exit to exit, any other key to continue ")
            if ch == "exit":
                break

def display_students():
    bid=input("Enter Batch ID ")
    with open("batch.csv", "r") as obj1:
        with open("student.csv", "r") as obj2:
            obj1.seek(0)
            robj1 = csv.reader(obj1)
            for i in robj1:
                obj2.seek(0)
                robj2 = csv.reader(obj2)
                for j in robj2:
                    if i[0] == bid and i[4] == j[0]:
                        print(j[1])


def display_courses():
    bid = input("Enter Batch ID ")
    with open("batch.csv", "r") as obj1:
       with open("course.csv", "r") as obj2:
            obj1.seek(0)
            robj1 = csv.reader(obj1)
            for i in robj1:
                obj2.seek(0)
                robj2 = csv.reader(obj2)
                for j in robj2:
                    if i[0] == bid and i[3] == j[0]:
                        print(j[1])


def batch_performance():
    bid = input("Enter Batch ID ")
    with open("batch.csv", "r") as obj1:
        with open("student.csv", "r") as obj2:
            with open("course.csv", "r") as obj3:
                obj1.seek(0)
                robj1 = csv.reader(obj1)
                for i in robj1:
                    #print(i)
                    obj2.seek(0)
                    robj2 = csv.reader(obj2)
                    for j in robj2:
                        #print(j)
                        obj3.seek(0)
                        robj3 = csv.reader(obj3)
                        for k in robj3:
                            #print(k)
                            if i[0] == bid and i[0] == j[3] and j[0] == k[2]:
                                print("ROLL", j[2], " ", "NAME", j[1], " ", "% MARKS", k[3])


def pie_chart():
    name=[]
    marks=[]
    with open("course.csv", "r") as obj1:
        with open("student.csv", "r") as obj2:
            obj1.seek(0)
            robj1 = csv.reader(obj1)
            for i in robj1:
                obj2.seek(0)
                robj2 = csv.reader(obj2)
                for j in robj2:
                    if i[2] == j[0]:
                        name.append(j[1])
                        marks.append(int(i[3]))
    print(name)
    print(marks)
    plt.pie(marks,labels=name)
    plt.title("% MARKS DISTRIBUTION")
    plt.show()

#batch_add()
#display_students()
#display_courses()
#batch_performance()
#pie_chart()
