from sqlalchemy import create_engine
from sqlalchemy.sql import text
from constants import SQL_DIR, TABLE_NAMES 
from cfg import DB_CONNSTR
import logging

engine = create_engine (DB_CONNSTR) 
log = logging.getLogger()

def create_tables():  
    """Create db tables"""
    with engine.connect() as con:
        for file in TABLE_NAMES:
            log.info("Creating table {file}")
            with open (SQL_DIR/f"{file}.sql") as f: 
                query = text(f.read()) 
                
            con.execute(text(f"DROP TABLE IF EXISTS {file}"))
            con.execute(query)
            
            
if __name__ == "__main__":
    create_tables()