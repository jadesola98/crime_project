{{ config(materialized='table') }}

with source_data as (

    select count(*), Description
    from city_source_data
    group by 2

)

select *
from source_data