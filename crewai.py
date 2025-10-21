## here execution will start
from crewai import Crew, Process   # ✅ Correct import
# Import agents and tasks
from agents import blog_researcher, blog_writer
from tasks import researcher_task, write_task

## Create the Crew for sequential execution
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[researcher_task, write_task],
    process=Process.sequential,   # ✅ Correct usage
    memory=True,
    cache=True,
    max_rpm=100,
    verbose=True                  # ✅ use verbose instead of share_crew
)

## Start the task execution process
result = crew.kickoff(inputs={"topic": "AI VS ML VS DL VS Data Science"})
print(result)


#Note--- whenever we want to run any application with the help of multi ai agents we specipically require llm model
#so in the agent section of crewai we have to provide llm model configuration
##also llm section is available



