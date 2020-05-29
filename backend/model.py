import sqlalchemy


metadata = sqlalchemy.MetaData()
items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), index=True, nullable=False),
    sqlalchemy.Column("price", sqlalchemy.Float, nullable=False, default=0),
    sqlalchemy.Column("image", sqlalchemy.String(128), nullable=True),
)