from sqlalchemy import create_engine, text

db_string = "postgresql://root:root@localhost:5432/store"

engine = create_engine(db_string)
connection = engine.connect()

create_table_query ="""
CREATE TABLE IF NOT EXISTS files (
    title text,
    director text,
    year text
);
"""
#connection.execute(text("CREATE TABLE IF NOT EXISTS films(title text, director text, year text)"))
#connection.execute("INSERT INTO films(titke, director, year)VALUES ('Doctor Strange, Scott Derrickson','2016')")
connection.execute(text(create_table_query))
connection.commit()

connection.close()
