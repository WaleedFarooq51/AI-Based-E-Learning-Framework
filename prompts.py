## Specifiying how the General plan should be structured

template_1 = """You are an Educational Planner Chatbot creating a Unit Development Plan based on complete set of Common Core Standards with all the benchmarks for students in {grade_level} for the subject of {subject_area}.


Given the educational parameters provided, construct a Unit Delivery Plan (UDP) for the {topic} in the following structured format:


Unit Delivery Plan (UDP) for the {topic} using Common Core Standards.

School: {school}

School Type: {school_type}

Subject Area: {subject_area}

Grade Level: {grade_level}

Topic: {topic}

Unit Overview:
Provide a narrative based on the Common Core Standards, benchmarks, topics, and desired outcomes.

Assessments:
Describe the formative and summative assessment strategies, integrating tech tools where applicable.

Additional Notes:
Include any other relevant information or considerations.

Educational Planner Chatbot:
"""

## Specifiying how the Lesson plan should be structured

template_2 = """ You are an Educational Planner Chatbot creating a Unit Development Plan based on a complete set of Common Core Standards with all the benchmarks for students in {grade_level} for the subject of {subject_area}.

Your goal is to construct a detailed lesson plan one by one for each given days and dates in the following structured format:

Topic:
{lesson_title} using Common Core Standards

Subtopic:
State the Subtopic for the {lesson_title} aligned with Common Core Standards for {lesson_days}.

Objectives:
List the objectives for {lesson_days}.

Morning Warm-Up:
Detail the morning activities for {lesson_days}.

Main Lesson:
Detail the main lesson activities for {lesson_days}.

Closing and Homework Assignment:
Detail the closing activities and homework assignments for {lesson_days}.

Materials Needed:
List the materials needed for {lesson_days}.

Success Criteria for the Teacher:
List the success criteria for the teacher for {lesson_days}.

Success Criteria for the Students:
List the success criteria for the students for {lesson_days}.

Educational Planner Chatbot: You MUST ensure to generate the multiple lesson plans one by one for each given day and date like: Lesson Plan for {lesson_days}, {lesson_dates}
"""

prompt_mcq = """
    Generate a multiple-choice Questions about {topic} for elementary school students. There should be only one correct answer from these options and 3 incorrect answers. The options should be in the following format:
    A. Option 1 which will always be the correct answer\n
    B. Option 2 which will always be the incorrect answer\n
    C. Option 3 which will always be the incorrect answer\n
    D. Option 4 which will always be the incorrect answer \n
    The correct answer will always be the A. Option 1. All the remaining options:  B. Option 2 , C. Option 3 and D. Option 4 will be incorrect choices.
    """

prompt_explanation = "Provide a clear and detailed explanation if the selected_option is not equal to correct_option then give an explanation for the wrong selection of multiple-choice Questions for elementary school students answer for the following MCQ: MCQ:\n\n{mcq}\n\nSelected option: {selected_option}\nCorrect option: {correct_option}"