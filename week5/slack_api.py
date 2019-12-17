import sqlalchemy as sqa
from pprint import pprint
import json

username = "Ming"
password = ""
db_name = "test"
# connection string to postgres
DATABASE_URI = f"postgres+psycopg2://{username}@localhost:5432/{db_name}"
# "/mysql://"
file_path = '/Users/Ming/Documents/CodingNomads/python-onsite/week_05/more_APIs/slack_resources.json'

engine = sqa.create_engine(DATABASE_URI, echo=True)
connection = engine.connect()
metadata = sqa.MetaData()

# Create table: slack

# ts = sqa.Table('slack', metadata,
#      sqa.Column('id', sqa.Integer, autoincrement=True, primary_key=True),
#      sqa.Column('comments', sqa.String(1000)),
#      sqa.Column('date_added', sqa.DateTime),
#      sqa.Column('description', sqa.String(1000)),
#      sqa.Column('link', sqa.String(1000), nullable=False),
#      sqa.Column('rating', sqa.Integer),
#      sqa.Column('read', sqa.Boolean),
#      sqa.Column('starred', sqa.Boolean),
#                    )
# metadata.create_all(engine)

# load the file from slack_resources.json
with open(file_path, 'r') as f:
    file = json.load(f)

# for post in file:
#     pprint(post)

ts = sqa.Table('slack', metadata, autoload=True, autoload_with=engine)
query = sqa.insert(ts)
result_proxy = connection(query, file)

# insert into table: slack
# result = connection.execut()

#     {
#         "comments": "There are comments.",
#         "date_added": "2019-03-19 03:56:32",
#         "description": "LMGTFY",
#         "link": "https://lmgtfy.com/",
#         "rating": 0,
#         "read": true,
#         "starred": true
#     },{}]