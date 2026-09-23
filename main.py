from ingestion.pdf_loader import PDFLoader
from ingestion.text_splitter import TextSplitter
from vectorstore.embeddings import Embedding
from vectorstore.retriever import Retriever
from agents.jd_agent import JDAgent
import pandas as pd

# 1. Load PDF
pdf = PDFLoader("Data/Python_Full_Stack_Developer_Fresher_JD.pdf")
documents = pdf.load()
# 2. Split PDF
splitter = TextSplitter(documents)
chunks = splitter.split()
# 3. Create Embeddings + FAISS
embedding = Embedding(chunks)
vectorstore = embedding.create_embeddings()
# 4. Create Retriever
retriever_obj = Retriever(vectorstore)

retriever = retriever_obj.get_retriever()
# 5. Retrieve relevant JD information
results = retriever.invoke(
    "What are the eligibility criteria and required skills for this job?"
)
print("\nRetrieved Documents:")

context = ""

for doc in results:

    print("-----------------------")
    print(doc.page_content)

    context += doc.page_content + "\n"


# 6. Agent 1 - JD Analysis
agent = JDAgent()

requirements = agent.analyze(context)

print("\n==============================")
print("JD ANALYSIS AGENT RESULT")
print("==============================")

print(requirements)

print("\nJob Role:")
print(requirements.job_role)

print("\nRequired Qualification:")
print(requirements.required_qualification)

print("\nMinimum 10th:")
print(requirements.minimum_10th_percentage)

print("\nMinimum 12th:")
print(requirements.minimum_12th_percentage)

print("\nMinimum Graduation:")
print(requirements.minimum_graduation_percentage)

print("\nRequired Skills:")
for skill in requirements.required_technical_skills:
    print("-", skill)

print("\nExperience:")
print(requirements.required_experience)

students = pd.read_excel("Data/student_data_100.xlsx")

print("\n==============================")
print("STUDENT DATA")
print("==============================")

print(students.head())
# 9. Agent 2 - Eligibility Agent

from agents.eligibility_agent import EligibilityAgent

eligibility_agent = EligibilityAgent(students)

eligible_students = eligibility_agent.check_eligibility(requirements)
# 10. Print eligible students

print("\n==============================")
print("ELIGIBLE STUDENTS")
print("==============================")

for student in eligible_students:

    
    print("Name:", student["Name"])
    print("Roll No:", student["Roll No"])
    print("10th:", student["10th Percent"])
    print("12th:", student["12th Percent"])
    print("Graduation:", student["Graduation Percent"])
    print("Skills:", student["Skills"])