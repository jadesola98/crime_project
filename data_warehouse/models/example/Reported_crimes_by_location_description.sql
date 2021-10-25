{{ config
    (materialized='table')
}}

with crime_data as (
    select * from {{ source('public','city_source_data') }}
),
 
final as (

    select count(*), location_description
    from crime_data
    group by 2

)

select * from final