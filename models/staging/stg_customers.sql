select
    customer_id,
    full_name,
    country,
    signup_date
from {{ source('raw', 'customers') }}
