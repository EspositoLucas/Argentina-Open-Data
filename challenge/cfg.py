from decouple import AutoConfig 
from constants import ROOT_DIR
from dotenv import load_dotenv
import os

config = AutoConfig(search_path=ROOT_DIR)

load_dotenv("C:/Users/esposito/workspace/Datos/Ingenieria de Datos/Codin Eric/Challenge Data Analytics/.env")

DB_CONNSTR = os.getenv('DB_CONNSTR') 
MUSEO_URL = os.getenv('MUSEO_URL')
CINES_URL = os.getenv('CINES_URL')
ESPACIOS_URL = os.getenv('ESPACIOS_URL')

# DB_CONNSTR = config("DB_CONNSTR")
# MUSEO_URL = config("MUSEO_URL")
# CINES_URL = config("CINES_URL") 
# ESPACIOS_URL = config("ESPACIOS_URL")

museo_ds = {
    "name": "museo", 
    "url": MUSEO_URL,
}

cines_ds = {
    "name": "cines",
    "url": CINES_URL,
}

espacios_ds = {
    "name": "bibliotecas_populares", 
    "url": ESPACIOS_URL,
}