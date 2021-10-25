{{ config
    (materialized='table')
}}

with crime_data as (
    select * from {{ source('public','city_source_data') }}
),
 
final as (

    select count(*), community_area
    from crime_data
    group by 2

)

select * from final