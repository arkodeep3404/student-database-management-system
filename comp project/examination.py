import csv
import matplotlib.pyplot as plt

def examination_add():
    with open("examination.csv","a",newline="") as obj:
        wobj=csv.writer(obj)
        while True:
            cname=input("Enter Course Name ")
            sroll = input("Enter Student Roll Number ")
            bname = input("Enter Batch Name ")
            marks = int(input("Enter marks out of 100 "))
            record = [cname, sroll, bname, str(marks)]
            wobj.writerow(record)
            ch = input("exit to exit, any other key to continue ")
            if ch == "exit":
                break

def student_performance():
    cname=input("Enter Course Name ")
    with open("examination.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if i[0] == cname:
                print(i[3])

def scatter_plot():
    batch=[]
    marks=[]
    with open("examination.csv","r") as obj:
        robj=csv.reader(obj)
        for i in robj:
            batch.append(i[2])
            marks.append(int(i[3]))
    print(batch)
    print(marks)
    plt.scatter(marks,batch,color="r")
    plt.title("MARKS OBTAINED IN DIFFERENT COURSES BY VARIOUS BATCHES")
    plt.xlabel("MARKS")
    plt.ylabel("BATCHES")
    plt.show()

#examination_add()
#student_performance()
#catter_plot()

