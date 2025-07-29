"""## **General_UDP**"""

from prompts import template_1
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os


class GENERAL_UDP:
    def __init__(self, school_name="ABC", school_type="Primary", grade_level="1", subject="XYZ", topic_name="Alpha", days="X", dates="Y"):
        self.school_name= school_name
        self.school_type= school_type
        self.grade_level= grade_level
        self.subject= subject
        self.topic_name= topic_name
        self.days= days
        self.dates= dates 

        # Load environment variables from the .env file
        load_dotenv()

        # Retrieve API keys from the environment variables
        self.openai_api_key= os.getenv("OPENAI_API_KEY")

    def general_udp(self):

        global general_plan

        prompt = PromptTemplate(template= template_1, input_variables=["topic", "school", "school_type", "grade_level", "subject_area"])                #Initializing prompt
        
        llm= ChatOpenAI(temperature= 0, openai_api_key= self.openai_api_key, model_name="gpt-3.5-turbo-16k")

        llm_chain = prompt | llm                                  
                            
        result= llm_chain.invoke({ "school": self.school_name, "school_type": self.school_type, "grade_level": self.grade_level, "subject_area": self.subject, "topic": self.topic_name}, return_only_outputs=True)

        general_plan= result.content                              #Generating response

        print(general_plan)
        print("-----------------------------------------------------------------------------")

        