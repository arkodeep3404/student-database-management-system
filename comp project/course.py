import csv
import matplotlib.pyplot as plt

def course_add():
    with open("course.csv", "a",newline="") as obj:
        wobj=csv.writer(obj)
        while True:
            d={}
            cid=input("Enter Course ID ")
            cname=input("Enter Course Name ")
            sid=input("Enter Student ID ")
            smarks=int(input("Enter Marks "))
            d.update({sid:smarks})
            for k,v in d.items():
                record=[cid,cname,k,v]
            wobj.writerow(record)
            ch = input("exit to exit, any other key to continue ")
            if ch == "exit":
                break

def course_stats():
    cname=input("Enter Course Name ")
    with open("course.csv", "r") as obj1:
        with open("student.csv", "r") as obj2:
            obj1.seek(0)
            robj1=csv.reader(obj1)
            for i in robj1:
                #print(i)
                obj2.seek(0)
                robj2 = csv.reader(obj2)
                for j in robj2:
                    #print(j)
                    if i[1]==cname and i[2]==j[0]:
                        print("ROLL",j[2]," ","NAME",j[1]," ","% MARKS",i[3])

def histogram():
    marks=[]
    with open("course.csv","r") as obj:
        robj=csv.reader(obj)
        for i in robj:
            marks.append(int(i[3]))
        print(marks)
    k=[0,10,20,30,40,50,60,70,80,90,100]
    plt.hist(marks,bins=k,rwidth=0.8)
    plt.xlabel("GRADES")
    plt.ylabel("NUMBER OF STUDENTS")
    plt.title("COURSE STATISTICS")
    plt.xticks(k)
    plt.show()

#course_add()
#course_stats()
#histogram()
