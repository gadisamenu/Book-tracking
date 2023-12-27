import os
from dotenv import load_dotenv

load_dotenv()

postgres_host = os.environ.get('POSTGRES_SERVER') if  os.environ.get('POSTGRES_SERVER',None)  else os.getenv("POSTGRES_SERVER")
postgres_user = os.environ.get('POSTGRES_USER') if  os.environ.get('POSTGRES_USER',None) else os.getenv("POSTGRES_USER")
postgres_password = os.environ.get('POSTGRES_PASSWORD') if  os.environ.get('POSTGRES_PASSWORD',None) else os.getenv("POSTGRES_PASSWORD")
postgres_db = os.environ.get('POSTGRES_DB') if  os.environ.get('POSTGRES_DB',None) else os.getenv("POSTGRES_DB")
postgres_port = os.environ.get('POSTGRES_PORT') if  os.environ.get('POSTGRES_PORT',None) else os.getenv("POSTGRES_PORT")