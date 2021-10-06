import pandas as pd
import config
from sodapy import Socrata

client = Socrata("data.cityofchicago.org",
                 config.api_key,
                 config.username,
                config.password)

#print(client)
results = client.get("ijzp-q8t2", limit=5000)

#print(type(results))
#print(results)

df = pd.DataFrame.from_records(results)

print(df)

#migrate from dataframe to database
from sqlalchemy import create_engine
engine = create_engine(config.database_credentials)
df.to_sql('city_source_data', engine)