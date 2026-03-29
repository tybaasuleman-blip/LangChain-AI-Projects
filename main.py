from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0.3
)

response = llm.invoke("Hello Gemini, are you working?")
print(response.content)
from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="You are a software engineer who only answers software-related queries."),
    HumanMessage(content="Who are you?")
]

ai_msg = llm.invoke(messages)

print(ai_msg.content)
from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="You are a software engineer who only answers software-related queries."),
    HumanMessage(content="Who are you?"),
    HumanMessage(content="What programming languages do you work with?")
]

ai_msg = llm.invoke(messages)
print(ai_msg.content)
from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="You are a software engineer who only answers software-related queries."),
    HumanMessage(content="Who are you?"),
    HumanMessage(content="What programming languages do you work with?")
]

ai_msg = llm.invoke(messages)

print(ai_msg.content[0]["text"] if isinstance(ai_msg.content, list) else ai_msg.content)
