#!/usr/bin/env python
# coding: utf-8

# ### Models Integration With OpenAI, Google Gemini and GROQ

# In[1]:


import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


# In[7]:


from langchain.chat_models import init_chat_model
model=init_chat_model("gpt-4.1")
model


# In[8]:


## invoke the model
response=model.invoke("Hello How are you?")
response


# In[11]:


### ChatOpenAI

from langchain_openai import ChatOpenAI
model=ChatOpenAI(model="gpt-4.1")
response=model.invoke("Hello How are you?")
response


# In[9]:


response.content


# ### Google Gemini Model Integration
# 
# 

# In[15]:


import os
from langchain.chat_models import init_chat_model

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

model = init_chat_model("google_genai:gemini-2.5-flash")
response = model.invoke("Why do parrots talk?")
response.content


# In[12]:


import os
from langchain_google_genai import ChatGoogleGenerativeAI



model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
response = model.invoke("Why do parrots talk?")
response


# ### GROQ MODEL Integration

# In[13]:


import os
from langchain.chat_models import init_chat_model

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = init_chat_model("groq:qwen/qwen3-32b")
response = model.invoke("Why do parrots talk?")
response


# In[14]:


import os
from langchain_groq import ChatGroq



model = ChatGroq(model="qwen/qwen3-32b")
response = model.invoke("Why do parrots talk?")
response


# ### Streaming And Batch
# 
# ### Streaming
# Most models can stream their output content while it is being generated. By displaying output progressively, streaming significantly improves user experience, particularly for longer responses.
# Calling stream() returns an iterator that yields output chunks as they are produced. You can use a loop to process each chunk in real-time:

# In[16]:


model.invoke("Write me a 200 words paragraph on Artificial Intelligence")


# In[19]:


for chunk in model.stream("Write me a 200 words paragraph on Artificial Intelligence"):
    print(chunk.text, end="|", flush=True)


# In[22]:


model.invoke("Why do parrots have colorful feathers?")


# In[20]:


for chunk in model.stream("Why do parrots have colorful feathers?"):
    print(chunk.text, end="|", flush=True)


# 
# #### Batch
# Batching a collection of independent requests to a model can significantly improve performance and reduce costs, as the processing can be done in parallel:

# In[23]:


responses = model.batch([
    "Why do parrots have colorful feathers?",
    "How do airplanes fly?",
    "What is quantum computing?"
])
for response in responses:
    print(response)


# In[24]:


model.batch(
    ["Why do parrots have colorful feathers?",
    "How do airplanes fly?",
    "What is quantum computing?"],
    config={
        'max_concurrency': 5,  # Limit to 5 parallel calls
    }
)

