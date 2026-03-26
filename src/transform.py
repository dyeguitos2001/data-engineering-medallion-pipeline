import pandas as pd
from .utils.logging_config import setup_logger

logger = setup_logger()

REQUIRED_COLUMNS = [
    "order_id", "order_date", "customer_id", "product",
    "category", "region", "quantity", "unit_price", "order_status"
]

def transform_to_silver(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting Silver transformation")
    df = df.copy()
    df.columns = [col.strip().lower() for col in df.columns]

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    df["product"] = df["product"].astype(str).str.strip()
    df["category"] = df["category"].astype(str).str.strip().str.title()
    df["region"] = df["region"].astype(str).str.strip().str.title()
    df["order_status"] = df["order_status"].astype(str).str.strip().str.lower()

    df = df.drop_duplicates(subset=["order_id"])
    df = df.dropna(subset=["order_id", "order_date", "quantity", "unit_price"])
    df = df[(df["quantity"] > 0) & (df["unit_price"] >= 0)]

    df["revenue"] = df["quantity"] * df["unit_price"]
    df["order_year"] = df["order_date"].dt.year
    df["order_month"] = df["order_date"].dt.month
    df["is_completed"] = df["order_status"].eq("completed")

    logger.info("Silver transformation finished with %s rows", len(df))
    return df

def build_gold(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Building Gold analytical layer")
    gold = (
        df.groupby([df["order_date"].dt.date.rename("order_day"), "region", "category"], dropna=False)
        .agg(
            total_orders=("order_id", "nunique"),
            total_quantity=("quantity", "sum"),
            revenue=("revenue", "sum"),
            completed_orders=("is_completed", "sum"),
        )
        .reset_index()
    )
    gold["avg_ticket"] = gold["revenue"] / gold["total_orders"]
    logger.info("Gold layer finished with %s rows", len(gold))
    return gold
