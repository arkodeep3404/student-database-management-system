import csv
import matplotlib.pyplot as plt

def examination_add():
    with open("examination.csv","a",newline="") as obj:
        wobj=csv.writer(obj)
        while True:
            cname=input("Enter Course Name ")
            while True:
                batch=input("Enter Batch name of the student ")
                roll=input("Enter Student Roll Number ")
                marks=int(input("Enter marks out of 100 obtained by the student "))
                record=[batch,cname,roll,str(marks)]
                wobj.writerow(record)
                ch = input("exit to exit, any other key to continue ")
                if ch == "exit":
                    break
            ch=input("exit to exit, any other key to continue ")
            if ch=="exit":
                break

def student_performance():
    with open("examination.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==2:
                print(i)

def scatter_plot():
    batch=[]
    marks=[]
    with open("examination.csv","r") as obj:
        robj=csv.reader(obj)
        for i in robj:
            batch.append(i[0])
            marks.append(int(i[3]))

    plt.scatter(marks,batch,color="r")
    plt.title("MARKS OBTAINED IN DIFFERENT COURSES BY VARIOUS BATCHES")
    plt.xlabel("MARKS")
    plt.ylabel("BATCHES")
    plt.show()

#examination_add()
#student_performance()
#scatter_plot()

