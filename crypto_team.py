from typing import List, Dict
from pydantic import BaseModel, Field
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

# Define structured output models
class ResearchPlan(BaseModel):
    topic: str = Field(..., description="Main topic for research")
    key_areas: List[str] = Field(..., description="Key areas to research")
    data_points_needed: List[str] = Field(..., description="Specific data points to gather")
    market_aspects: List[str] = Field(..., description="Market aspects to analyze")

class ResearchFindings(BaseModel):
    topic: str = Field(..., description="Research topic")
    market_data: Dict = Field(..., description="Market-related data and statistics")
    key_insights: List[str] = Field(..., description="Key insights from research")
    sources: List[str] = Field(..., description="Sources of information")

class BlogStructure(BaseModel):
    title: str = Field(..., description="Engaging blog title")
    summary: str = Field(..., description="Brief executive summary")
    sections: List[Dict[str, str]] = Field(..., description="Blog sections with headings and content")
    key_takeaways: List[str] = Field(..., description="Key takeaways for readers")
    references: List[str] = Field(..., description="References and sources")

# Create specialized agents
planner_agent = Agent(
    name="Planning Agent",
    role="Research planner and strategist",
    model=OpenAIChat(id="gpt-3.5-turbo"),  # Using 3.5 for cost efficiency in planning
    instructions=[
        "Create structured research plans for crypto topics",
        "Break down complex topics into manageable research areas",
        "Focus on cost-effective research strategies",
        "Identify key data points needed for comprehensive analysis"
    ],
    show_tool_calls=True,
    markdown=True,
)

research_agent = Agent(
    name="Research Agent",
    role="Data gatherer and analyst",
    model=OpenAIChat(id="gpt-4o"),  # Using GPT-4 for accurate research and analysis
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
    show_tool_calls=True,
    markdown=True,
)

writer_agent = Agent(
    name="Writer Agent",
    role="Content creator and editor",
    model=OpenAIChat(id="gpt-3.5-turbo"),  # Using 3.5 for cost efficiency in writing
    instructions=[
        "Create engaging and informative content",
        "Structure content for readability",
        "Include relevant data and insights",
        "Maintain professional tone and clarity"
    ],
    show_tool_calls=True,
    markdown=True,
)

# Combine agents into a team
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
    markdown=True,
)

if __name__ == "__main__":
    # Example usage
    crypto_team.print_response(
        "Create a comprehensive analysis of Ethereum's Layer 2 scaling solutions, "
        "focusing on recent developments and market impact. Include technical aspects "
        "and investment implications.",
        stream=True
    ) 