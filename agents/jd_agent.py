import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Optional, List

load_dotenv()


# Structure of JD requirements
class JDRequirements(BaseModel):

    job_role: Optional[str] = None

    required_qualification: Optional[str] = None

    minimum_10th_percentage: Optional[float] = None

    minimum_12th_percentage: Optional[float] = None

    minimum_graduation_percentage: Optional[float] = None

    required_technical_skills: List[str] = Field(default_factory=list)

    required_experience: Optional[str] = None


class JDAgent:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.6-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

        # Tell Gemini to return our Pydantic structure
        self.structured_llm = self.llm.with_structured_output(
            JDRequirements
        )

    def analyze(self, context):

        prompt = f"""
You are a Job Description Analysis Agent.

Analyze the following Job Description information.

Extract ONLY information explicitly mentioned in the JD.

Rules:

1. Extract the job role.
2. Extract required educational qualification.
3. Extract minimum 10th percentage if mentioned.
4. Extract minimum 12th percentage if mentioned.
5. Extract minimum graduation percentage if mentioned.
6. Extract mandatory technical skills.
7. Extract required experience.
8. Do NOT invent any information.
9. If a field is not mentioned, return null.
10. Do NOT treat "Good to Have" skills as mandatory skills.

JD INFORMATION:

{context}
"""

        response = self.structured_llm.invoke(prompt)

        return response