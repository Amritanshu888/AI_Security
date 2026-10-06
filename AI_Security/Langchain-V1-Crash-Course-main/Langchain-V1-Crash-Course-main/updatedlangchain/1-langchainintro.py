#!/usr/bin/env python
# coding: utf-8

# ### Langchain Version V1
# 
# ### Agents

# In[14]:


import langchain
langchain.__version__


# In[2]:


import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


# In[5]:


from langchain.agents import create_agent

def get_weather(city:str)-> str:
    """Get the weather for a city."""
    return f"The weather in {city} is sunny."

agent=create_agent(
    model="gpt-5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant."
)
agent


# In[8]:


### run the agent
response=agent.invoke({"messages":[{"role":"user","content":"What is the weather like in New York?"}]})


# In[12]:


response["messages"]


# In[13]:


agent.invoke({"messages":"What is the weather in New Yourk"})


# In[ ]:




