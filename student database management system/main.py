import student
import course
import batch
import department
import examination

print(
    "Enter 1 to add a new student entry ""\n"
    "Enter 2 to display an already existing student entry ""\n"
    "Enter 3 to edit an already existing student entry ""\n"
    "Enter 4 to delete an already existing student entry ""\n"
    "Enter 5 to generate report card of a student ""\n"
    "Enter 6 to create a new course ""\n"
    "Enter 7 to view the student performance of a course ""\n"
    "Enter 8 to show histogram of course statistics ""\n"
    "Enter 9 to create a new batch ""\n"
    "Enter 10 to view the students in a batch ""\n"
    "Enter 11 to view the courses taught in a batch ""\n"
    "Enter 12 to view the student performance of a batch ""\n"
    "Enter 13 to show pie chart of % of all students ""\n"
    "Enter 14 to create a new department ""\n"
    "Enter 15 to view all the batches in a department ""\n"
    "Enter 16 to view the performance of all batches in a department ""\n"
    "Enter 17 to show line plot of department statistics ""\n"
    "Enter 18 to create a new examination record ""\n"
    "Enter 19 to view performance of students in an examination ""\n"
    "Enter 20 to show scatter plot of examination statistics ""\n"
    )

while True:
    ch=int(input("Enter your choice "))
    if ch == 1:
        student.student_add()
    elif ch == 2:
        student.student_display()
    elif ch == 3:
        student.student_update()
    elif ch == 4:
        student.student_delete()
    elif ch == 5:
        student.report_card()
    elif ch == 6:
        course.course_add()
    elif ch == 7:
        course.course_stats()
    elif ch == 8:
        course.histogram()
    elif ch == 9:
        batch.batch_add()
    elif ch == 10:
        batch.display_students()
    elif ch == 11:
        batch.display_courses()
    elif ch == 12:
        batch.batch_performance()
    elif ch == 13:
        batch.pie_chart()
    elif ch == 14:
        department.department_add()
    elif ch == 15:
        department.display_batches()
    elif ch == 16:
        department.batch_performance()
    elif ch == 17:
        department.line_plot()
    elif ch == 18:
        examination.examination_add()
    elif ch == 19:
        examination.student_performance()
    elif ch == 20:
        examination.scatter_plot()
    ch2=input("exit to exit any other key to continue ")
    if ch2 == "exit":
        break

