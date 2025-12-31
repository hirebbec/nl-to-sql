from sqlalchemy import Table, Column, String, MetaData

metadata = MetaData(schema="information_schema")

columns_table = Table(
    "columns",
    metadata,
    Column("table_name", String),
    Column("column_name", String),
    Column("data_type", String),
)
