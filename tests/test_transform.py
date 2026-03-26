import pandas as pd
from src.transform import transform_to_silver

def test_transform_to_silver_creates_revenue_and_filters_invalid_rows():
    df = pd.DataFrame(
        {
            "order_id": [1, 2, 2, 3],
            "order_date": ["2026-01-01", "2026-01-02", "2026-01-02", None],
            "customer_id": [10, 11, 11, 12],
            "product": ["Notebook", "Mouse", "Mouse", "Teclado"],
            "category": ["tech", "tech", "tech", "tech"],
            "region": ["sudeste", "sul", "sul", "norte"],
            "quantity": [1, 2, 2, 1],
            "unit_price": [3500, 80, 80, 120],
            "order_status": ["completed", "pending", "pending", "completed"],
        }
    )
    silver = transform_to_silver(df)
    assert len(silver) == 2
    assert "revenue" in silver.columns
    assert silver["revenue"].sum() == 3660
