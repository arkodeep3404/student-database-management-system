import csv
import matplotlib.pyplot as plt

def department_add():
    with open("department.csv","a",newline="") as obj:
        wobj=csv.writer(obj)
        while True:
            did=input("Enter Department ID ")
            dname=input("Enter Department Name ")
            bid=input("Enter Batch ID ")
            record=[did,dname,bid]
            wobj.writerow(record)
            ch=input("exit to exit, any other key to continue ")
            if ch=="exit":
                break

def display_batches():
    did = input("Enter Department ID ")
    with open("department.csv", "r") as obj1:
        with open("batch.csv", "r") as obj2:
            obj1.seek(0)
            robj1 = csv.reader(obj1)
            for i in robj1:
                obj2.seek(0)
                robj2 = csv.reader(obj2)
                for j in robj2:
                    if i[0] == did and i[2] == j[0]:
                        print(j[1])

def batch_performance():
    did = input("Enter Department ID ")
    with open("department.csv", "r") as obj1:
        with open("batch.csv", "r") as obj2:
            with open("course.csv", "r") as obj3:
                obj1.seek(0)
                robj1 = csv.reader(obj1)
                for i in robj1:
                    # print(i)
                    obj2.seek(0)
                    robj2 = csv.reader(obj2)
                    for j in robj2:
                        # print(j)
                        obj3.seek(0)
                        robj3 = csv.reader(obj3)
                        for k in robj3:
                            # print(k)
                            if i[0] == did and i[2] == j[0] and j[4] == k[2]:
                                print(k[3])

def line_plot():
    bname=[]
    marks=[]
    with open("batch.csv", "r") as obj1:
        with open("course.csv", "r") as obj2:
            obj1.seek(0)
            robj1 = csv.reader(obj1)
            for i in robj1:
                obj2.seek(0)
                robj2 = csv.reader(obj2)
                for j in robj2:
                    if i[3] == j[0]:
                        bname.append(i[1])
                        marks.append(int(j[3]))
    print(bname)
    print(marks)
    plt.plot(bname,marks,marker="o")
    plt.xlabel("BATCH NAME")
    plt.ylabel("% MARKS")
    plt.title("% MARKS DISTRIBUTION FOR EACH BATCH")
    plt.show()

#department_add()
#display_batches()
#batch_performance()
#line_plot()
