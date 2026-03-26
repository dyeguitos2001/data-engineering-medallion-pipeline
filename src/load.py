import sqlite3
import pandas as pd
from .config import SILVER_FILE, GOLD_FILE
from .utils.logging_config import setup_logger

logger = setup_logger()

def write_silver(df: pd.DataFrame) -> None:
    logger.info("Writing Silver layer to %s", SILVER_FILE)
    df.to_csv(SILVER_FILE, index=False)
    logger.info("Silver layer written successfully")

def write_gold(df: pd.DataFrame) -> None:
    logger.info("Writing Gold layer to %s", GOLD_FILE)
    df.to_csv(GOLD_FILE, index=False)
    logger.info("Gold layer written successfully")

def run_example_sql_query() -> pd.DataFrame:
    logger.info("Running sample SQL query on Gold layer")
    gold_df = pd.read_csv(GOLD_FILE)
    conn = sqlite3.connect(":memory:")
    gold_df.to_sql("sales_summary_gold", conn, index=False, if_exists="replace")
    query = '''
        SELECT region, category, SUM(revenue) AS total_revenue, SUM(total_orders) AS total_orders
        FROM sales_summary_gold
        GROUP BY region, category
        ORDER BY total_revenue DESC
    '''
    result = pd.read_sql_query(query, conn)
    conn.close()
    logger.info("Sample SQL query executed successfully")
    return result
