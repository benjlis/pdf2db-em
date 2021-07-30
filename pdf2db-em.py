import aiosql
import psycopg2
import os

PDFDIR = os.getenv('PDFDIR')
conn = psycopg2.connect("")
queries = aiosql.from_path("pdf2db-em.sql", "psycopg2")

pdfs = queries.dc19pdf_list(conn)
for p in pdfs:
    print(p)

#
pdf_list = os.listdir(PDFDIR)
print(pdf_list)
