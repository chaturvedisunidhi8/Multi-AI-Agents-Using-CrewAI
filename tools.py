##for tools  visit documentation crewai >> tools >> you have to choose youtube channel search tool
##for using this tool pip install 'crewai[tools]' (we have already done this step)
##you can get tools code from its chatbot
from crewai_tools import YoutubeVideoSearchTool
yt_tool= YoutubeVideoSearchTool(youtube_channel_handle='@krishnaik06')  ## initialize this variable in agent.py

## you can use several tools































