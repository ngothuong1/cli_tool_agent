from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

from tool import get_date, search
from config import MODEL_NAME, GEMINI_API_KEY


def build_agent():
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        temperature=0,
        google_api_key=GEMINI_API_KEY,
    )

    tools = [get_date, search]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",
             "Bạn là một AI assistant thông minh. "
             "Nếu câu hỏi liên quan đến ngày tháng, hãy dùng get_date. "
             "Nếu cần tìm kiếm thông tin, hãy dùng search."),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )

    agent = create_tool_calling_agent(llm, tools, prompt)

    executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return executor



 