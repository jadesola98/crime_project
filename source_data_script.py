import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofchicago.org",
                 "9GI35TGzZVKetBnn5VRnZiUax",
                 username="alayandeay@gmail.com",
                password="UpcwPk$s3W5@acG")

#print(client)
results = client.get("ijzp-q8t2", limit=5000)

#print(type(results))
#print(results)

df = pd.DataFrame.from_records(results)

print(df)

#migrate from dataframe to database
from sqlalchemy import create_engine
engine = create_engine('postgresql://mxzqmels:KY3Gj6B6yFPH1H4eSlmPtmpdwo6SJaJK@chunee.db.elephantsql.com:5432/mxzqmels')
df.to_sql('city_source_data', engine)