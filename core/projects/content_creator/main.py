from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

load_dotenv()

@CrewBase
class ContentCreatorCrew():
    """MarkDownValidatorCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator'],
            allow_delegation=False,
            verbose=True
        )

    @task
    def brainstorm_content(self) -> Task:
        return Task(
            config=self.tasks_config['brainstorm_content'],
            agent=self.content_creator()
        )

    @task
    def write_blog_post(self) -> Task:
        return Task(
            config=self.tasks_config['write_blog_post'],
            agent=self.content_creator(),
        )

    @task
    def social_media_copy(self) -> Task:
        return Task(
            config=self.tasks_config['social_media_copy'],
            agent=self.content_creator()
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
    result = ContentCreatorCrew().crew().kickoff(inputs={"topic": "Nigeria Economy and how it affects africa as a whole"})
    print(str(result))
