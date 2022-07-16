from Classes import *


student1=student("Satabdo Majumder","FSDS","Online","1","NONE",1,1,24)
student1.print_details()

#ENCAPSULATION
student1.changed_salary(30)


#INHERITANCE POLYMORPHISM #ABSTRACTION
student2=achievers("Satabdo Majumder","FSDS","Online","1","NONE",1,1,24)
student3=Hall_Of_Fame("Satabdo Majumder","FSDS","Online","1","NONE",1,1,24)

ineuron_graduate(student2)
ineuron_graduate(student3)

#METHOD OVERRIDING
student4=jobs("Satabdo Majumder","FSDS","Online","1","NONE",1,1,24)
student4.job()



