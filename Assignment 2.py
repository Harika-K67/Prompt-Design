
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



generic_prompt = "Can ypu review this resume in a few sentences?"


role_based_prompt = (
    "You are a hiring manager reviewing a resume for a junior data scientist position. Evaluate whether the resume clearly communicates the candidate’s background and if their experiences seem aligned with what’s typically expected for this kind of role. Consider whether their past projects or work reflect any tangible outcomes or results. Summarize your overall impression in 5 sentences."
)

resume_text = """
Name: Max Rodriguez
Email: max.rodriguez@example.com
Phone: (233) 604-5301
LinkedIn: linkedin.com/in/max-rodriguez
GitHub: github.com/maxrodriguez

Professional Summary:
A driven and experienced Junior Data Scientist committed to unlocking the value of data with modern analytical models, machine learning, and data visualization. Seeking to leverage expertise in SQL, R, Python, and Tableau to develop dynamic dashboards, create quality data sets, and accurately predict outcomes. Aiming to utilize knowledge and experience to quickly become a valuable asset to the organization.

Work Experience:

Junior Data Scientist
Sci-Data
March 2024 – Present
- Developed predictive models to forecast customer behavior, resulting in a 15% increase in customer retention.
- Collaborated with cross-functional teams to design and implement data-driven solutions, improving operational efficiency by 10%.
- Created interactive dashboards using Tableau to visualize key performance indicators for stakeholders.

Data Analyst Intern
Data Insights Inc.
June 2023 – February 2024
- Conducted exploratory data analysis to identify trends and patterns, aiding in strategic decision-making.
- Assisted in the development of automated reporting tools, reducing manual reporting time by 30%.
- Participated in data cleaning and preprocessing activities to ensure data quality and integrity.

Education:
Bachelor of Science in Statistics
University of Data Science
Graduated: May 2023

Skills:
- Programming Languages: Python, R, SQL
- Data Visualization: Tableau, Matplotlib, Seaborn
- Machine Learning: Scikit-learn, TensorFlow
- Data Manipulation: Pandas, NumPy
- Statistical Analysis
- Data Cleaning and Preprocessing

Certifications:
- Certified Data Scientist – Data Science Council of America (DASCA)
- Tableau Desktop Specialist
"""




# Generic response
print("\n--- Generic Prompt ---")
response_generic = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": f"{generic_prompt}\n\n{resume_text}"}
    ]
)
print(response_generic.choices[0].message.content)

# Role-based response
print("\n--- Role-Based Prompt ---")
response_role = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": f"{role_based_prompt}\n\n{resume_text}"}
    ]
)
print(response_role.choices[0].message.content)