import sqlalchemy as sqa

from pprint import pprint
# pip install psycopg2

username = "Ming"
password = ""
db_name = "dvdrental"
# connection string to postgres
DATABASE_URI = f"postgres+psycopg2://{username}@localhost:5432/{db_name}"

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

actor = sqa.Table('actor', metadata, autoload = True, autoload_with = engine)

query =sqa.select([actor]).where(actor.columns.first_name == 'Penelope')
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(query)
pprint(actor.columns.keys())
pprint(result_set)

