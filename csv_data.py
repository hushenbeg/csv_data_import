import csv
import psycopg2

conn = psycopg2.connect(
    user = "xxxxx",
    password = "xxxx",
    host = "xx.xxx.xxx.xxx",
    port = "5432",
    database = ""
)

cur = conn.cursor()

with open('/home/husenbeg/Downloads/Financial_Sample.csv', 'r') as f:

    reader = csv.reader(f)

    next(reader) # Skip the header row.

    for row in reader:

        print('-------row--------', row)

        postgres_insert_query = """INSERT INTO FINANCIAL_SAMPLE(
                        "segment", "country", "product", 
                        "discount_band", "units_sold", "manufacturing","sale_price",
                        "gross_sales", "discounts", "sales", "cogs", "profit",
                        "date", "month_number", "month_name", "year") VALUES (%s,%s,%s,%s,%s,%s,
                        %s,%s,%s, %s,%s,%s,%s,%s,%s,%s)"""

        cur.execute(
            postgres_insert_query,
            row
        )

conn.commit()
