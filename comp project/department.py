import csv
import matplotlib.pyplot as plt

def department_add():
    with open("department.csv","a",newline="") as obj:
        wobj=csv.writer(obj)
        while True:
            id=input("Enter Department ID ")
            name=input("Enter Department Name ")
            data=[id,name," "]
            wobj.writerow(data)
            while True:
                bname=input("Enter batch ")
                marks=int(input("Enter average % marks of the batch "))
                record=[bname,str(marks)]
                wobj.writerow(record)
                ch = input("exit to exit, any other key to continue ")
                if ch == "exit":
                    break
            ch=input("exit to exit, any other key to continue ")
            if ch=="exit":
                break

def display_batches():
    with open("department.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==1:
                print(i)

def batch_performance():
    with open("department.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==2:
                print(i)

def line_plot():
    bname=[]
    marks=[]
    with open("department.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==2:
                bname.append(i[0])
                marks.append(int(i[1]))
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
