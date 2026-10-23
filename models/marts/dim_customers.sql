with orders as (
    select * from {{ ref('stg_orders') }}
    where status = 'completed'
),
customer_orders as (
    select
        customer_id,
        count(*)         as order_count,
        sum(amount)      as lifetime_value,
        min(order_date)  as first_order_date
    from orders
    group by customer_id
)
select
    c.customer_id,
    c.full_name,
    c.country,
    c.signup_date,
    coalesce(o.order_count, 0)     as order_count,
    coalesce(o.lifetime_value, 0)  as lifetime_value,
    o.first_order_date
from {{ ref('stg_customers') }} c
left join customer_orders o using (customer_id)
