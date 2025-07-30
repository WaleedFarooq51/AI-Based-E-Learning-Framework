# AI-Based E-Learning System for Automated UDP and MCQ Generation

This project is an AI-driven E-Learning assistant that helps educators automate the generation of **Unit Delivery Plans (UDPs)** and **assessment content (MCQs)** based on simple input prompts. It leverages state-of-the-art language models to support lesson planning and evaluation in a structured and interactive manner.

---

## 📌 Features

- **General Unit Delivery Plan Generation**
  - Automatically generates a general teaching plan based on inputs like subject, topic, grade level, etc.

- **Day-wise Unit Delivery Plan (DAY UDP)**
  - Breaks down the general plan into daily subtopics with associated learning content.

- **MCQ Generation**
  - Creates multiple-choice questions (MCQs) with options and explanations from daily subtopics.

---

## 🚀 How It Works

1. **Teacher Input**
   - Inputs include: school name, school type, grade level, subject, main topic, number of days, and corresponding dates.

2. **General UDP Generation**
   - Uses the teacher inputs to generate a structured plan.

3. **Day-wise UDP Generation**
   - Prompts the user for the day and generates associated subtopics.

4. **MCQ Generator**
   - Based on selected subtopics, it generates MCQs with options and explanations.

---

## 🧪 How to Use

```bash
git clone https://github.com/your-username/ai-elearning-system.git
cd ai-elearning-system

# Install dependencies
- pip install -r requirements.txt

- Set your OpenAI API key in the .env file

# Execution
1. Run the python file: python udp_generation.py

2. Follow the prompts to enter the required details.

3. View the generated general plan, day-wise breakdown, and MCQs.
