user = "stemisDev"
password = "1234"
host = "db"
port = "3306"
database = "STEMIS_teste"

DATABASE_URI = (
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4"
)
