import os
import psycopg2

if os.environ.get('DATABASE_URL'):
    postgres_url = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(postgres_url, sslmode='require')
# If using local database
else:
    conn = psycopg2.connect(user="postgres",
                            password="admin",
                            database="stocks_analysis")

conn.autocommit = True
db = conn.cursor()

db.execute("CREATE table IF NOT EXISTS wallstreetbets ("
           "ticker VARCHAR (10), "
           "one_day_score FLOAT, "
           "recent FLOAT, "
           "previous FLOAT, "
           "change VARCHAR (10), "
           "rockets FLOAT, "
           "positive FLOAT, "
           "negative FLOAT, "
           "price VARCHAR (10), "
           "one_day_change_percent VARCHAR (10),"
           "fifty_day_change_percent VARCHAR (10), "
           "volume VARCHAR (10), "
           "mkt_cap VARCHAR (25), "
           "floating_shares VARCHAR (10), "
           "beta VARCHAR (10), "
           "short_per_float VARCHAR (10), "
           "industry VARCHAR (100), "
           "prev_close VARCHAR (10), "
           "open VARCHAR (10), "
           "day_low VARCHAR (10), "
           "day_high VARCHAR (10), "
           "target VARCHAR (10), "
           "recommend VARCHAR (20), "
           "date_updated VARCHAR (20), "
           "subreddit VARCHAR (25) )")

f = open(r'table_records1.csv', 'r')
db.copy_from(f, 'wallstreetbets', sep=',')
f.close()
