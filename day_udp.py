"""## **Day_UDP**"""

from prompts import template_2
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import re


class DAY_UDP:
    def __init__(self, gen_udp):
        self.gen_udp= gen_udp
    
    def day_udp(self):

        global lesson_plan

        prompt= PromptTemplate(template= template_2, input_variables=["grade_level", "subject_area", "lesson_days", "lesson_title", "lesson_dates"])  #Initializing prompt
        
        llm= ChatOpenAI(temperature= 0, openai_api_key= self.gen_udp.openai_api_key, model_name="gpt-3.5-turbo-16k")

        llm_chain = prompt | llm

        result= llm_chain.invoke({"grade_level": self.gen_udp.grade_level, "subject_area":self.gen_udp.subject, "lesson_days": self.gen_udp.days, "lesson_title": self.gen_udp.topic_name, "lesson_dates": self.gen_udp.dates}, return_only_outputs=True)

        self.lesson_plan= result.content                               #Generating response

        print(self.lesson_plan)
        print("-----------------------------------------------------------------------------")

    ## Function that will extract the Subtopics from Lesson Plan
    def extract_subtopics(self):

        ## Initialize a list to store the extracted information
        self.subtopics_days_dates = []

        ## Split the lesson plan into sections for each day
        sections = self.lesson_plan.split("Lesson Plan for")

        ## Loop through the sections starting from index 1 to skip the first empty section
        for sec in sections[1:]:

            ## Initialize variables to store the subtopic, day, and date
            subtop = None
            day = None
            date = None

            ## Checking if there is a match for the subtopics pattern
            subtopic_match = re.search(r"Subtopic:\s*(.*?)\s*(?:\n|$)", sec, re.DOTALL)

            ## If there is a match return the subtopic
            if subtopic_match:
                subtop = subtopic_match.group(1).strip()

            ## Checking if there is a match for the days, dates pattern
            calendar_match = re.search(r"(\w+), ([A-Za-z]+ \d+)", sec)

            ## If there is a match return day,date
            if calendar_match:
                day = calendar_match.group(1).strip()
                date = calendar_match.group(2).strip()

            self.subtopics_days_dates.append((day, date, subtop))

        print("SubTopic, Days and Dates from Lesson Plan are as follows:")

        for day, date, subtop in self.subtopics_days_dates:
            print(f"Day: {day}, Date: {date}")
            print(f"Subtopic: {subtop}\n")

    ## Function that will extract the Subtopic for given Day by Teacher
    def get_day_subtopic(self):

        provided_day = input("Enter the Day: ")

        for day, date, subtopic in self.subtopics_days_dates:
            if day == provided_day:
                self.subtopic= subtopic
                print(f"Topic for {provided_day}: {self.subtopic}")
                print("-----------------------------------------------------------------------------")
                return self.subtopic
                            
            else:
                print(f"No topic found for {provided_day}")


    
        