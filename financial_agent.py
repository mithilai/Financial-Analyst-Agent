from phi.agent import Agent
from phi.model.groq import Groq
#DuckDuckGo enables an Agent to search the web for information.
from phi.tools.duckduckgo import DuckDuckGo
#YFinanceTools enable an Agent to access stock data, financial information and more from Yahoo Finance.
from phi.tools.yfinance import YFinanceTools


#websearch agent
web_search_agent = Agent(
    name="Web Search agent",
    role="Search the web for the information",
    model= Groq(id="llama-3.3-70b-specdec"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    markdown= True
)

#financial agent
financial_agent = Agent(
    name="Financial AI agent",
    model= Groq(id="llama-3.3-70b-specdec"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)

#
multi_ai_agent=Agent(
    team=[web_search_agent,financial_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)
