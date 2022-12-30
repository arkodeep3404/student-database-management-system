import csv
import matplotlib.pyplot as plt

def course_add():
    with open("course.csv", "a",newline="") as obj:
        wobj=csv.writer(obj)
        while True:
            id=input("Enter Course ID ")
            name=input("Enter Course Name ")
            data=[id,name]
            wobj.writerow(data)
            while True:
                sname=input("Enter Student Name ")
                sroll=int(input("Enter Roll Number "))
                smarks=int(input("Enter Marks "))
                record=[sname,str(sroll),str(smarks)]
                wobj.writerow(record)
                ch = input("exit to exit, any other key to continue ")
                if ch == "exit":
                    break
            ch=input("exit to exit, any other key to continue ")
            if ch=="exit":
                break

def display_courses():
    with open("course.csv", "r") as obj:
        obj.seek(0)
        robj=csv.reader(obj)
        for i in robj:
            print(i)

def histogram():
    l=[]
    with open("course.csv","r") as obj:
        robj=csv.reader(obj)
        for i in robj:
            if len(i)==3:
                l.append(int(i[2]))
        print(l)
    k=[0,10,20,30,40,50,60,70,80,90,100]
    plt.hist(l,bins=k,rwidth=0.8)
    plt.xlabel("GRADES")
    plt.ylabel("NUMBER OF STUDENTS")
    plt.title("COURSE STATISTICS")
    plt.xticks(k)
    plt.show()

#course_add()
#display_courses()
#histogram()
