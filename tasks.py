##we have to create two tasks
## you can get task from crewai website

from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer

##Researcher tasks
researcher_task=Task(
    description=("Research relevant Youtube videos content on the given {topic} from the specified youtube channel"),
expected_output="  A list with 10 bullet points of the most relevant information about {topic}",
tools=[yt_tool],
agent=blog_researcher,)

##writing task with language model configuration
write_task=Task(
    description=("Research relevant Youtube videos content on the given {topic} from the specified youtube channel"),
expected_output="  A list with 10 bullet points of the most relevant information about {topic}",
tools=[yt_tool],
agent=blog_writer,
async_execution=False,  ## async_exe... means both the agents will be working parallalely 
output_file='new-blog-post.md'    ##example of output optimization
)













