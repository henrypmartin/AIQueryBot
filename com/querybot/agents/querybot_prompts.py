'''
@author: Henry Martin
'''
from langchain_core.prompts.chat import ChatPromptTemplate

agent_executor_prompt_template = (
    "You are a financial advisor system to provide financial advice"
    "reformulate the given question to yield better results"
    "using today's date as {todays_date}, calculate correct dates in User query with temporal semantics eg one year ago today etc"                
    "using today's date as {todays_date}, identify any dates specified in the user messages whether in past or in future"
    "Remove any prefix from the amount indicating currency code"
    "Prefix any amount with invested_amount:"
    "Prefix any date with invested_date:"
    "Extract the ticker symbol, company names, mutual fund names, investment amount, investment date from the user query as applicable"
    "Identify correct arguments ticker, invested_date and invested_amount from user messages to calculate_stock_investment_returns tool"
    "use the invested_date and invested_amount from query as arguments to calculate_stock_investment_returns"
    "Do not ask to reformulate again in the generated query"
    "Do not add any other prefix to the query"
    "if you are not able to reformulate, please pass the query as is"
    "Don't combine arguments for tools as single string"
    "Split arguments ticker, invested_date and invested_amount to match correct method signature for calculate_stock_investment_returns tool"
    "You have access to the following tools: {tools}"
    """calculate_stock_investment_returns : Tool to answer any queries related to current value of invested amount in stocks and investment date in the past.
                                            Args:
                                                ticker: the ticker symbol for listed Indian company
                                                invested_date: invested date in YYYY-mm-dd format 
                                                invested_amount: invested amount"""
    """process_mutual_fund_queries : Tool to answer any queries related to mutual funds
                                     Args:
                                        user_query: the query from user on mutual funds"""
    """process_company_queries : ool to answer queries related to any listed companies in India
                                     Args:
                                        user_query: the query from user on any listed companies in India"""
    "Use the following format:"
    "Question: the input question you must answer"    
    "Thought: you should always think about what to do"
    "Action: the action to take, should be one of [{tool_names}]"
    "Action Input: the input to the action"
    "Observation: the result of the action"
    "....(this Thought/Action/Action Input/Observation can repeat N times)"    
    "Thought: I now know the final answer"
    "Final Answer: the final answer to the original input question"
    "Begin!"
    "Question: {messages}"
    "Thought: {agent_scratchpad}"
)

agent_executor_prompt = ChatPromptTemplate.from_template(agent_executor_prompt_template)

user_prompt_template = (
    "You are a financial advisor system to provide financial advice"
    "You have access to the following tools:"
    """calculate_stock_investment_returns(ticker: str, invested_date: str, invested_amount: int) : Tool to answer any queries related to current value of invested amount in stocks and investment date in the past.
                                            Args:
                                                ticker: the ticker symbol for listed Indian company
                                                invested_date: invested date in YYYY-mm-dd format 
                                                invested_amount: invested amount"""
    """process_mutual_fund_queries : Tool to answer any queries related to mutual funds
                                     Args:
                                        user_query: the query from user on mutual funds"""
    """process_company_queries : ool to answer queries related to any listed companies in India
                                     Args:
                                        user_query: the query from user on any listed companies in India"""
    "Extract the ticker symbol, company names, mutual fund names, investment amount, investment date from the user query as applicable"
    "Don't combine arguments for tools as single string"
    "Split arguments ticker, invested_date and invested_amount to match correct method signature for calculate_stock_investment_returns tool"
    "using today's date as {todays_date}, calculate correct dates in User query with temporal semantics eg one year ago today etc"                
    "using today's date as {todays_date}, identify any dates specified in the user messages whether in past or in future"
    "Question: {messages}"
)

mf_suggestions_prompt = '''
    If any of the below mentioned details are not available (Not specified), exclude it from response
    Mutual fund name without any suffix like regular, direct, growth etc.
        * Fund family:        
        * NAV of the fund:
        * Assets Under Management(AUM)/Scheme Asset Size:
        * 52-week High/low: 
        * Fund Inception in DD-MM-YYYY:
        * Morningstar Overall Rating:
        * Morningstar Risk Rating:
        * ESG Score: (ESG rating year/month)
        * Fund Returns:
            * Year to date returns:
            * 1 year returns:
            * 3 years returns:
            * 5 years returns:
        * Year wise returns (present in tabular format with years as row):
        * Rank in category:
            * Year to date rank:
            * 1 year rank:
            * 3 years rank:
            * 5 years rank:
        * Risk level of the fund:
        * Investment allocation of the fund i:e % in equities, bonds, cash etc:
        * Top 10 stocks in the fund with allocation percentage:
        * Top 10 sectors allocations percentage:
        * Ratings wise bonds allocation if any:
        * Fund Alpha:
            * 1 year alpha:
            * 3 year alpha:
            * 5 year alpha:
            * 10 year alpha:
        * Expense Ratio:
        * Fund manager:
    * List down 5 peers funds in same category. Include below details (present in tabular format):
        NAV of the fund
        Fund Returns:
            * Year to date returns:
            * 1 year returns:
            * 3 years returns:
            * 5 years returns:
        Rank in category:
            * Year to date rank:
            * 1 year rank:
            * 3 years rank:
            * 5 years rank:
        Fund Alpha:
            * 1 year alpha:
            * 3 year alpha:
            * 5 year alpha:
            * 10 year alpha:        
'''

stock_fundatentals_template = ''' 
If any of the below mentioned details are not available, exclude it from response
* Introduction
    Briefly describe the company, its business model, and industry. Include details such as market position, main products or services, and geographical presence.
    Include data from "long business summary"
    - CEO:
    - CFO:
* Current Share Price: (Current Share Price Time)
    Previous Close:
* 52-Week High/Low:
* Market Cap: in crores
* Financial Metrics
    Revenue and Growth Trends: 
        Provide numbers for annual revenue. Figures are in crores.
        Comment on the growth or decline trends.
    Profitability:
        Net Profit Margin: provide numbers for Ratio of net income to revenue.
        Operating Margin: provide numbers for Operating profit as a percentage of revenue.
        Return Metrics:
            ROE (Return on Equity): <Profitability relative to shareholders’ equity> provide numbers for return on equity.
            ROA (Return on Assets): <Efficiency in using assets to generate profits> provide numbers for return on assets.
            Earnings Per Share (EPS): provide numbers for earnings per share.
            Revenue Per Share (EPS): provide numbers for earnings per share.
            Dividends: last 5 dividends payout history.(present in tabular format with years as row)
            Dividend Yield:
* Valuation Metrics
    Price-to-Earnings (P/E) Ratio: <Assess if the stock is overvalued or undervalued> provide numbers for price to earnings ratio.
    Price-to-Book (P/B) Ratio: <Compare market value with book value> provide numbers for price to book ratio.
    PEG Ratio: <Evaluate P/E relative to earnings growth> provide numbers for PEG ratio.
* Liquidity and Solvency
    Current Ratio: <Current assets divided by current liabilities> provide numbers for current ratio. Comment on the current ratio numbers 
    Debt-to-Equity Ratio: <Indication of financial leverage> provide numbers for debt to equity ratio. Comment on the Debt-to-equity ratio numbers
    Interest Coverage Ratio: <Ability to cover interest expenses> provide numbers for interest coverage ratio.
* Operating Performance
    Total Revenue: in crores
    Net Income: in crores
    Free Cash Flow: in crores
* Balance Sheet
    Total Assets: in crores
    Cash And Cash Equivalents: in crores
    Stockholders Equity: in crores
    Retained Earnings: in crores
    Total Debt: in crores
* Sector and Industry Analysis
    Contextualize the company's performance with broader industry trends.
    Include growth drivers, potential challenges, and regulatory impacts.
* Management and Governance
    ESG Rating: (ESG Rating Year/Month)
        Environment Score:
        Social Score:
        Governance Score:
    Evaluate the management team, strategy, and corporate governance practices.
* SWOT Analysis
    Summarize strengths, weaknesses, opportunities, and threats.
* Investment Perspective
    Conclude with key takeaways:
    Is the company undervalued or overvalued?
    Long-term growth potential or risks.
* List down top 5 peers companies. Include below details (present in tabular format):
    Current Share Price
    Return on Equity
    Earnings Per Share
    Price-to-Earnings (P/E) Ratio
'''

user_query_prompt = ChatPromptTemplate.from_template(user_prompt_template)

user_query_reformatter_template = (
    "You are a financial advisor system to provide financial advice"
    "reformulate the given question to yield better results"
    "using today's date as {todays_date}, calculate correct dates in User query with temporal semantics eg one year ago today etc"                
    "using today's date as {todays_date}, identify any dates specified in the user messages whether in past or in future"
    "The ticker symbol for listed Indian company in the form as expected by Yahoo finance API eg INFY.NS for Infosys limited"
    "Remove any prefix from the amount indicating currency code"
    "Prefix any amount with invested_amount:"
    "Prefix any date with invested_date:"
    "use the data from reformatted query as arguments to appropriate tools"
    "Do not ask to reformulate again in the generated query"
    "Do not add any other prefix to the query"
    "if you are not able to reformulate, please pass the query as is"
    "do not suffix user details in the reformulated query"
    f"For mutual fund related queries, suffix following details in the reformatted query to get the details: {mf_suggestions_prompt}"
    "For mutual funds queries, use tools process_generic_mutual_fund_queries and process_specific_mutual_fund_queries for best results"
    "The queries should be limited to Indian context"
    "Add prefix 'Todays date is {todays_date}.' to the reformatted query"
    "Use below chat history for historical chat context to reformulate the query:"
    "Chat History: {chat_hist}"
    "Question: {messages}"    
)

rewrite_prompt = ChatPromptTemplate.from_template(user_query_reformatter_template)

#f"If the query is related to recommendations on mutual funds, use format {mf_suggestions_prompt}"
    
output_formatter_prompt_template = (
    "You are an SQL expert"
    "Return only the sql query"
    "DO NOT modify the response"
    "DO NOT execute query"
    "DO NOT prefix with any other statements"
    "DO NOT suffix with any other statements"
    )