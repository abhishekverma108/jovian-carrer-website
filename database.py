import sqlalchemy
print(sqlalchemy.__version__)
from sqlalchemy import create_engine,text
connectinstring="mysql+mysqlconnector://s97cuzyinv4tyhg8v95v:pscale_pw_dOMuGewERfOEHoAuijKAMKkS2j8oMwBXThN7Q1fgpqz@aws.connect.psdb.cloud/joviancarrer"

engine = create_engine(connectinstring,
 echo=True)
  

    