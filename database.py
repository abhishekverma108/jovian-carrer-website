import sqlalchemy
import os
print(sqlalchemy.__version__)
from sqlalchemy import create_engine,text
connectinstring=os.environ["CONNECTION_STRING"]


engine = create_engine(connectinstring,
 echo=True)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs=[]
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

    