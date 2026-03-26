from .extract import extract_raw_data, write_bronze
from .transform import transform_to_silver, build_gold
from .quality import validate_silver
from .load import write_silver, write_gold, run_example_sql_query
from .utils.logging_config import setup_logger

logger = setup_logger()

def run_pipeline() -> None:
    logger.info("Pipeline started")
    raw_df = extract_raw_data()
    write_bronze(raw_df)

    silver_df = transform_to_silver(raw_df)
    validate_silver(silver_df)
    write_silver(silver_df)

    gold_df = build_gold(silver_df)
    write_gold(gold_df)

    preview = run_example_sql_query()
    logger.info("Top SQL result preview:\n%s", preview.head().to_string(index=False))
    logger.info("Pipeline finished successfully")

if __name__ == "__main__":
    run_pipeline()
