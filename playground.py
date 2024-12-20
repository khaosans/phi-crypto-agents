from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app
from typing import List, Dict
from pydantic import BaseModel, Field

# Original Web and Finance Agents
web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    storage=SqlAgentStorage(table_name="web_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    storage=SqlAgentStorage(table_name="finance_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Crypto Research Team Agents
planner_agent = Agent(
    name="Crypto Planning Agent",
    role="Research planner and strategist",
    model=OpenAIChat(id="gpt-3.5-turbo"),
    instructions=[
        "Create structured research plans for crypto topics",
        "Break down complex topics into manageable research areas",
        "Focus on cost-effective research strategies",
        "Identify key data points needed for comprehensive analysis"
    ],
    storage=SqlAgentStorage(table_name="crypto_planner", db_file="agents.db"),
    show_tool_calls=True,
    markdown=True,
)

research_agent = Agent(
    name="Crypto Research Agent",
    role="Data gatherer and analyst",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        DuckDuckGo(),
        YFinanceTools(stock_price=True, company_info=True, company_news=True)
    ],
    instructions=[
        "Gather comprehensive data based on research plan",
        "Focus on reliable and current sources",
        "Validate information across multiple sources",
        "Organize findings in a structured format"
    ],
    storage=SqlAgentStorage(table_name="crypto_researcher", db_file="agents.db"),
    show_tool_calls=True,
    markdown=True,
)

writer_agent = Agent(
    name="Crypto Writer Agent",
    role="Content creator and editor",
    model=OpenAIChat(id="gpt-3.5-turbo"),
    instructions=[
        "Create engaging and informative content",
        "Structure content for readability",
        "Include relevant data and insights",
        "Maintain professional tone and clarity"
    ],
    storage=SqlAgentStorage(table_name="crypto_writer", db_file="agents.db"),
    show_tool_calls=True,
    markdown=True,
)

crypto_team = Agent(
    name="Crypto Research Team",
    team=[planner_agent, research_agent, writer_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Coordinate between planning, research, and writing phases",
        "Ensure data accuracy and relevance",
        "Optimize for cost-effective research and content creation",
        "Produce comprehensive yet concise blog posts"
    ],
    storage=SqlAgentStorage(table_name="crypto_team", db_file="agents.db"),
    markdown=True,
)

# Create the playground with all agents
app = Playground(agents=[
    web_agent,
    finance_agent,
    planner_agent,
    research_agent,
    writer_agent,
    crypto_team
]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True) 