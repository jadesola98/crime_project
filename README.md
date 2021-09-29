# crime_project

This project is designed to pull data of reported crime incidents in Chicago from the Chicago data portal using the API, perform some transformation and store the output in a data warehouse.



# Tools

## 1.Sodapy
Sodapy is the official python api for socrata

# 2.Airbyte
Airbyte is an open-source data integration engine that helps consolidate data into data warehouses.

# 3.DBT(data build tool)
dbt allows for transformation of data in data warehouses.It does the T in ELT (Extract, Load, Transform) processes – it doesn’t extract or load data, but it’s extremely good at transforming data that’s already loaded in the warehouse.

# 4.Postgres
stores the raw and transformed data.
