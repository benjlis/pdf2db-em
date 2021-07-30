import aiosql
import psycopg2

conn = psycopg2.connect("")
queries = aiosql.from_path("pdf2db-em.sql", "psycopg2")

pdfs = queries.dc19pdf_list(conn)
for p in pdfs:
    print(p)
