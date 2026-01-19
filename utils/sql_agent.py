from langchain_community.agent_toolkits import SQLDatabaseToolkit


from utils.db import get_db
from utils.llm import get_llm

db = get_db()
llm = get_llm()

toolkit = SQLDatabaseToolkit(
    db=db,
    llm=llm
)

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

def ask_db(question: str) -> str:
    """
    Takes an English question, generates SQL,
    executes it, and returns a natural language answer.
    """
    result = agent.invoke({"input": question})
    return result["output"]
