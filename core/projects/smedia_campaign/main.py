from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

load_dotenv()

@CrewBase
class SmediaCampaignCrew():
    """Social Media Campaign Crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # --- Agents ---
    @agent
    def trend_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_researcher'],
            verbose=True
        )

    @agent
    def copywriter(self) -> Agent:
        return Agent(
            config=self.agents_config['copywriter'],
            verbose=True
        )

    @agent
    def designer(self) -> Agent:
        return Agent(
            config=self.agents_config['designer'],
            verbose=True
        )

    @agent
    def scheduler(self) -> Agent:
        return Agent(
            config=self.agents_config['scheduler'],
            verbose=True
        )

    # --- Tasks ---
    @task
    def trend_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['trend_research_task']
        )

    @task
    def copywriting_task(self) -> Task:
        return Task(
            config=self.tasks_config['copywriting_task']
        )

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task']
        )

    @task
    def scheduling_task(self) -> Task:
        return Task(
            config=self.tasks_config['scheduling_task']
        )

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
        "topic": "Launching a new AI-powered study app for students"
    }
    result = SmediaCampaignCrew().crew().kickoff(inputs=inputs)

    print("\n=== Final Campaign Plan ===\n")
    print(str(result))

