{{ config(materialized='table') }}

with source_data as (

    select count(*), community_area
    from city_source_data
    group by 2

)

select *
from source_data