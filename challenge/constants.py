from pathlib import Path

BASE_FILE_DIR = Path("/tmp") 
ROOT_DIR=Path().resolve().parent
SQL_DIR = ROOT_DIR / "challenge/sql"

RAW_TABLE_NAME = "raw"
CINE_INSIGHTS_TABLE_NAME = "cine_insights" 
SOURCE_SIZE_TABLE_NAME = "size_by_datasource" 
CATEGORY_COUNT_TABLE_NAME = "size_by_category" 
PROV_CAT_COUNT_TABLE_NAME = "size_by_prov_cat"

TABLE_NAMES = [
    RAW_TABLE_NAME,
    CINE_INSIGHTS_TABLE_NAME,
    SOURCE_SIZE_TABLE_NAME,
    CATEGORY_COUNT_TABLE_NAME,
    PROV_CAT_COUNT_TABLE_NAME,
]