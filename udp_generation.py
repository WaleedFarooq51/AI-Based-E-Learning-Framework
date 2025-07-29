from general_udp import GENERAL_UDP
from day_udp import DAY_UDP
from mcq_generation import MCQ_Gen


class UDP_Generation:
    def __init__(self, school_name, school_type, grade_level, subject, topic_name, days, dates):
        self.gen_udp= GENERAL_UDP(school_name, school_type, grade_level, subject, topic_name, days, dates)
        self.day_udp= DAY_UDP(self.gen_udp)
        self.mcq_gen= MCQ_Gen(self.day_udp)
    
    def execution(self):

        self.gen_udp.general_udp()
        self.day_udp.day_udp()

        self.day_udp.extract_subtopics()
        self.day_udp.get_day_subtopic()

        ## Number of MCQs to be generated
        mcq_number= int(input("Enter the Number of MCQs to be generated: "))

        self.mcq_gen.input_answer(mcq_number)

## Taking input from the Teacher
print("Enter the Details: ")
school_name= input("School: ")
school_type= input("School Type: Elementary/Secondary: ")
grade_level= input("Grade: ")
subject= input("Subject: ")
topic_name= input("Topic: ")
days= input("Enter the Days: ")
dates= input("Enter the Dates: ")

## Creating object of class
udp_generation= UDP_Generation(school_name, school_type, grade_level, subject, topic_name, days, dates)

udp_generation.execution()

    

        
    