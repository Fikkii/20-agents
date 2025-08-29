from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

load_dotenv()

@CrewBase
class  SeoOptimizerCrew():
    """MarkDownValidatorCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def keyword_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['keyword_researcher'],
            verbose=True
        )

    @agent
    def seo_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_writer'],
            verbose=True
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['keyword_research_task'],
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['seo_writing_task'],
        )

    @task
    def editing_task(self) -> Task:
        return Task(
            config=self.tasks_config['editing_task'],
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
        "draft_content": "What is the best way forward for Nigerians, with their money hungry politicians and diverse language. Unity looks like a good word but hard to accomplish due to tribalism"
    }
    result =  SeoOptimizerCrew().crew().kickoff(inputs=inputs)
    print(str(result))
