student_name = input("Enter your name")
student_age = int(input("Enter your age"))
College = input("Enter your college name")
Branch = input("Enter your Branch name")

Subject1 = int(input("Enter marks for Subject 1"))
Subject2 = int(input("Enter marks for Subject 2"))
Subject3 = int(input("Enter marks for Subject 3"))
Subject4 = int(input("Enter marks for Subject 4"))
Subject5 = int(input("Enter marks for Subject 5"))

Total_marks =Subject1 + Subject2 + Subject3 + Subject4 + Subject5

Percentage = (Total_marks*100)/500

Average_marks = (Total_marks/5)

print("STUDENT REPORT")
print("Name: ",student_name)
print("Age:",student_age)
print("College:",College)
print("Branch:",Branch)
print("Total Marks:",Total_marks)
print("Percentage:",Percentage)
print("Average:",Average_marks)