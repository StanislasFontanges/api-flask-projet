from sqlalchemy import create_engine, text

db_string = "postgresql://root:root@localhost:5432/store"

engine = create_engine(db_string)
connection = engine.connect()

create_user_table_query ="""
CREATE TABLE IF NOT EXISTS users (
    ID          SERIAL PRIMARY KEY,
    firstname   TEXT,
    lastename   TEXT,
    age         INT,
    email       CHAR(50),
    job         CHAR(50)
);
"""

create_application_table_query ="""
CREATE TABLE IF NOT EXISTS applications (
    ID                  SERIAL PRIMARY KEY,
    appname             TEXT,
    username            TEXT,
    last_connection     DATE,
    user_id             INT references users(ID)
);
"""

#connection.execute(text("CREATE TABLE IF NOT EXISTS films(title text, director text, year text)"))
#connection.execute("INSERT INTO films(titke, director, year)VALUES ('Doctor Strange, Scott Derrickson','2016')")
connection.execute(text(create_user_table_query))
connection.execute(text(create_application_table_query))

connection.commit()

connection.close()
