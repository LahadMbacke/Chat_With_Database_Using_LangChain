import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
import psycopg2


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
host = os.getenv("host")
port = os.getenv("port")
dbname = os.getenv("dbname")
username = os.getenv("username")
password = os.getenv("password")

prompt = """En se basant sur ce schema , ecrit un requte sql pour repondre la question d'un utilisatuer {schema}.
Question : {question}"""

template = ChatPromptTemplate.from_template(prompt)
# print(template.format(schema="Student",question="Quels sont les etudiants mineurs"))

uri_pg = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"


db = SQLDatabase.from_uri(uri_pg)

def get_table(db):
    return db.get_table_info()


