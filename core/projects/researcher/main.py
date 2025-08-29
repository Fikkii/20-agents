from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

load_dotenv()

@CrewBase
class ResearcherCrew():
    """MarkDownValidatorCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],
            verbose=True
        )

    @agent
    def outline_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['outline_creator'],
            verbose=True
        )

    @agent
    def reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['reviewer'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
        )

    @task
    def editing_task(self) -> Task:
        return Task(
            config=self.tasks_config['editing_task'],
        )

    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_task'],
        )
    @task
    def outline_task(self) -> Task:
        return Task(
            config=self.tasks_config['outline_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarkDownValidatorCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

if __name__ == "__main__":
    inputs = {
        "topic": "Nigeria Economy and how it affects africa as a whole",
        "research_notes": "Nigeria once boasted to be the giant of africa and still maintain it's strength as one of the top africa country's",
        "project_outline": "This project focus on what role nigeria plays in the economy of africa",
        "project_draft": "None"
    }
    result = ResearcherCrew().crew().kickoff(inputs=inputs)
    print(str(result))
