import duckdb
con = duckdb.connect("dev.duckdb")
con.execute("create schema if not exists raw")
con.execute("""
create or replace table raw.customers as
select i as customer_id,
       'Customer ' || i as full_name,
       (['Lebanon','UAE','France','Russia'])[1 + (i % 4)] as country,
       date '2025-01-01' + (i % 300)::int as signup_date
from range(1, 201) t(i)
""")
con.execute("""
create or replace table raw.orders as
select i as order_id,
       1 + (i * 7 % 200) as customer_id,
       date '2025-06-01' + (i % 120)::int as order_date,
       round(10 + (i * 37 % 490) + (i % 10) / 10.0, 2) as amount,
       (['completed','completed','completed','returned','cancelled'])[1 + (i % 5)] as status
from range(1, 2001) t(i)
""")
print(con.execute("select count(*) from raw.orders").fetchone())
