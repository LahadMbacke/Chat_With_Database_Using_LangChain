import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import psycopg2


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
host = os.getenv("host")
port = os.getenv("port")
dbname = os.getenv("dbname")
username = os.getenv("username")
password = os.getenv("password")


# 1 This step is to retrive the sql query 

# uri for connecting to database 
uri_pg = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"
db = SQLDatabase.from_uri(uri_pg)

def get_table(_):
     return  db.get_table_info()


template = """En se basant sur ce schema , ecrit un requte sql pour repondre la question d'un utilisatuer {table}.
Question : {question}"""

prompt = ChatPromptTemplate.from_template(template)


model = ChatOpenAI()

chain = (
    RunnablePassthrough.assign(table=get_table)
    | prompt
    | model
    | StrOutputParser()
)


# 1 This step is to translate the result's query in langauge natural
template_final = """
 Base sur cette table et la requte pour donner les resultats :
 {table}

 Question: :{question}
 Reponse: {reponse}
"""
prompt_final = ChatPromptTemplate.from_template(template_final)

def get_response(query):
    return db.run(query)

nlp_chain = (
     RunnablePassthrough.assign(query=chain).assign(table=get_table, reponse= lambda var : get_response(var["query"]))
     | prompt_final
     |model
     | StrOutputParser()
)


query = "Donne moi le nombre de client ?'"
resultats = nlp_chain.invoke({"question":query})
print(resultats)

