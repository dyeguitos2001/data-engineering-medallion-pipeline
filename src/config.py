from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

RAW_FILE = RAW_DIR / "orders.csv"
BRONZE_FILE = BRONZE_DIR / "orders_bronze.csv"
SILVER_FILE = SILVER_DIR / "orders_silver.csv"
GOLD_FILE = GOLD_DIR / "sales_summary_gold.csv"
