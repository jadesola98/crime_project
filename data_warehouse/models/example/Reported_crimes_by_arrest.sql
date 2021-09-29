{{ config(materialized='table') }}

with source_data as (

select count(*), arrest 
from city_source_data
group by arrest

)

select *
from source_data