class EligibilityAgent:

    def __init__(self, students):
        self.students = students

    def check_eligibility(self, requirements):

        eligible_students = []

        required_skills = requirements.required_technical_skills

        for _, student in self.students.iterrows():

            student_skills = [
                skill.strip().lower()
                for skill in student["Skills"].split(",")
            ]

            matched = True

            for required_skill in required_skills:

                if required_skill.lower() not in student_skills:
                    matched = False
                    break

            if matched:
                eligible_students.append(student)

        return eligible_students