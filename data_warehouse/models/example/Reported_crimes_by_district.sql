{{ config(materialized='table') }}

with source_data as (

select count(*), district 
from city_source_data
group by district

)

select *
from source_data