import sqlalchemy as sqa

from pprint import pprint
# pip install psycopg2, database driver

username = "Ming"
password = ""
db_name = "test"
# connection string to postgres
DATABASE_URI = f"postgres+psycopg2://{username}@localhost:5432/{db_name}"
# "/mysql://"

engine = sqa.create_engine(DATABASE_URI, echo = True)
connection = engine.connect()
metadata = sqa.MetaData()

#t_test = sqa.Table('test', metadata,
     # sqa.Column('id', sqa.Integer, autoincrement=True, primary_key=True),
     # sqa.Column('quote', sqa.String(255), nullable=False),
     # sqa.Column('year', sqa.Integer),
     # sqa.Column('is_great', sqa.Boolean, default=False))
#ins = t_test.insert().values(id='1', quote='I am going to quit next week', year='2019', is_great=True)
#ins = t_test.insert().values(quote='to be or not to be', year=1583)

t2 = sqa.Table('test', metadata, autoload=True, autoload_with=engine)
query = sqa.insert(t2)
new_records =[{'quote':'things change','year':2019},
{'quote':'think twice','year':2013}
]


s = sqa.select([t2.c.quote])

#metadata.create_all(engine)
conn = engine.connect()
# result=conn.execute(ins)
result=conn.execute(s)
pprint(result.text)

result_proxy = conn(query, new_records)