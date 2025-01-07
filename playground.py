from phi.agent import Agent
from phi.model.groq import Groq
#DuckDuckGo enables an Agent to search the web for information.
from phi.tools.duckduckgo import DuckDuckGo
#YFinanceTools enable an Agent to access stock data, financial information and more from Yahoo Finance.
from phi.tools.yfinance import YFinanceTools
import os
import phi
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv
#load environment variable from .env
#load api from .env
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

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

app = Playground(agents = [web_search_agent,financial_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
    #playground file name and app is above object