from prompts import prompt_mcq, prompt_explanation
from general_udp import GENERAL_UDP
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import random


class MCQ_Gen:
    def __init__(self, day_udp):

        # Initialize Classes
        self.gen_udp= GENERAL_UDP()
        self.day_udp= day_udp

    ## Function to generate questions
    def generate_quiz(self):

        prompt = PromptTemplate(template= prompt_mcq, input_variables=["topic"])        #Initializing prompt
            
        llm= ChatOpenAI(temperature= 0, openai_api_key= self.gen_udp.openai_api_key, model_name="gpt-3.5-turbo-16k")

        llm_chain= prompt | llm 

        result= llm_chain.invoke({"topic": self.day_udp.subtopic}, return_only_outputs=True)

        generated_quiz= result.content                             #Generating response

        return generated_quiz
    
    ## Function to enter the answer
    def input_answer(self, mcq_number):
        
        for _ in range(mcq_number):
            generated_mcqs = self.generate_quiz()
            generated_mcqs_lines = generated_mcqs.split("\n")

            self.mcq = generated_mcqs_lines[0]
            options = generated_mcqs_lines[1:5]

            for i in range(0, len(options)):
                options[i] = options[i][3:]

            shuffled_options = random.sample(options, len(options))

            print(self.mcq)
            for idx, option in enumerate(shuffled_options):
                print(f"{idx+1}. {option}")

            answer = input("Select the correct option (1/2/3/4): ")

            correct_option_idx = shuffled_options.index(options[0])

            ##Check if answer is correct or not
            if int(answer) == correct_option_idx + 1:
                # results[self.day_udp.subtopic]["correct"] += 1
                print("Correct!\n")

            else:
                # results[self.day_udp.subtopic]["incorrect"] += 1
                print("Incorrect!\n")

                self.selected_option = shuffled_options[int(answer) - 1]
                self.correct_option = shuffled_options[correct_option_idx]

                generated_explanation = self.generate_explanation()
                print(generated_explanation)
                print("-----------------------------------------------------------------------------")
                
    ## Function to generate explanation
    def generate_explanation(self):
    
        prompt = PromptTemplate(template= prompt_explanation, input_variables=["mcq", "selected_option", "correct_option"])  #Initializing prompt
                
        llm= ChatOpenAI(temperature= 0, openai_api_key= self.gen_udp.openai_api_key, model_name="gpt-3.5-turbo-16k")

        llm_chain = prompt | llm 

        result= llm_chain.invoke({"mcq": self.mcq, "selected_option": self.selected_option, "correct_option":self.correct_option}, return_only_outputs=True)

        generated_explanation= result.content                              #Generating response

        return generated_explanation
