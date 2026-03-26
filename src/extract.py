from datetime import datetime
import pandas as pd
from .config import RAW_FILE, BRONZE_FILE
from .utils.logging_config import setup_logger

logger = setup_logger()

def extract_raw_data() -> pd.DataFrame:
    logger.info("Reading raw data from %s", RAW_FILE)
    df = pd.read_csv(RAW_FILE)
    df["ingestion_timestamp"] = datetime.utcnow().isoformat()
    logger.info("Raw dataset loaded with %s rows", len(df))
    return df

def write_bronze(df: pd.DataFrame) -> None:
    logger.info("Writing Bronze layer to %s", BRONZE_FILE)
    df.to_csv(BRONZE_FILE, index=False)
    logger.info("Bronze layer written successfully")
