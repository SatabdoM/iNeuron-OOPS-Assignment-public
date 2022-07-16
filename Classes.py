import logging 
logging.basicConfig(filename="IneuronLogs",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')

class student:
        def __init__(self,student_name,course_enrolled,mode,number_of_courses,affiliates,internship,jobs,offered_salary):
                self.student_name=student_name
                self.course_enrolled=course_enrolled
                self.mode=mode
                self.number_of_courses=number_of_courses
                self.affiliates=affiliates
                self.intership=internship
                self._jobs=jobs
                self.__salary=offered_salary
        
        def print_details(self):
            try:
                logging.info(f"Name:{self.student_name}")
                logging.info(f"Course enrolled:{self.course_enrolled}")
                logging.info(f"Internships:{self.intership}")
                logging.info(f"Jobs Offers:{self._jobs}")
            except Exception as e:
                logging.exception(e)
                
            
        #ENCAPSULATION
        def changed_salary(self,new_salary):
            try:
                self.__salary=new_salary
                logging.info(f"Salary changed to {self.__salary}LPA")
            except Exception as e:
                logging.exception(e)
                
        def job(self):
            try:
                if(self.intership>=2):
                    logging.info("You are eligible for a job")
                else:
                    logging.info("You are not eligible")
            except Exception as e:
                logging.exception(e)
            
 #INHERITANCE           
class achievers(student):
    def achievement(self):
        try:
            if(self._jobs==1):
                logging.info(f"{self.student_name} is in the list of achievers")
        except Exception as e:
                logging.exception(e)
            
#ABSTRACTION 
class Hall_Of_Fame(student):
    def achievement(self):
        try:
            if(self._student__salary>=10):
                logging.info(f"{self.student_name} is in the Hall of Fame")
        except Exception as e:
                logging.exception(e)
            
#METHOD OVERWRITING       
class jobs(student):
    def job(self):
        try:
            if(self.intership>=1):
                logging.info(f"{self.student_name} is eligible for a job")
            else:
                logging.info(f"{self.student_name} is not eligible for a job")
        except Exception as e:
                logging.exception(e)


 #POLYMORPHISM   
def ineuron_graduate(a):
    try:
        a.achievement()
    except Exception as e:
                logging.exception(e)




# student1=achievers("Satabdo Majumder","FSDS","Online","1","NONE",1,1,24)
# student1.changed_salary(25)


# student2=Hall_Of_Fame("Satabdo Majumder","FSDS","Online","1","NONE",1,1,24)

# ineuron_graduate(student2)

# student1=jobs("Satabdo Majumder","FSDS","Online","1","NONE",1,1,24)
# student1.job()



        
           