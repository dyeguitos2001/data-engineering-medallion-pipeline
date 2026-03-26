from .utils.logging_config import setup_logger

logger = setup_logger()

def validate_silver(df) -> None:
    logger.info("Running Silver quality checks")
    if df["order_id"].isna().any():
        raise ValueError("Quality check failed: null order_id found")
    if (df["quantity"] <= 0).any():
        raise ValueError("Quality check failed: quantity must be greater than zero")
    if (df["unit_price"] < 0).any():
        raise ValueError("Quality check failed: unit_price cannot be negative")
    if df["order_date"].isna().any():
        raise ValueError("Quality check failed: invalid order_date found")
    logger.info("Silver quality checks passed")
