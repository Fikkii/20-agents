from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

load_dotenv()

@CrewBase
class ResumeCreatorCrew():
    """Job Application Tailoring Crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # --- Agents ---
    @agent
    def job_description_analyzer(self) -> Agent:
        return Agent(config=self.agents_config['job_description_analyzer'], verbose=True)

    @agent
    def resume_tailor(self) -> Agent:
        return Agent(config=self.agents_config['resume_tailor'], verbose=True)

    @agent
    def cover_letter_writer(self) -> Agent:
        return Agent(config=self.agents_config['cover_letter_writer'], verbose=True)

    @agent
    def reviewer(self) -> Agent:
        return Agent(config=self.agents_config['reviewer'], verbose=True)

    # --- Tasks ---
    @task
    def job_analysis_task(self) -> Task:
        return Task(config=self.tasks_config['job_analysis_task'])

    @task
    def resume_task(self) -> Task:
        return Task(config=self.tasks_config['resume_task'])

    @task
    def cover_letter_task(self) -> Task:
        return Task(config=self.tasks_config['cover_letter_task'])

    @task
    def review_task(self) -> Task:
        return Task(config=self.tasks_config['review_task'])

    # --- Crew ---
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )


if __name__ == "__main__":
    inputs = {
        "job_description": """
        We are seeking a Data Analyst with experience in SQL, Python, and Tableau.
        The ideal candidate has 3+ years of analytics experience, strong
        communication skills, and the ability to work with cross-functional teams.
        """,
        "resume": """
        John Doe
        - Skills: Excel, PowerPoint, SQL basics
        - Experience: Marketing intern (2020-2021), Data assistant (2021-2022)
        - Education: BSc in Statistics
        """
    }

    result = ResumeCreatorCrew().crew().kickoff(inputs=inputs)

    print("\n=== Final Application Package ===\n")
    print(str(result))

