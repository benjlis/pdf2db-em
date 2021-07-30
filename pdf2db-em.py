import aiosql
import psycopg2
import os
import pdfemail         # right now it's a symbolic link to pdf2mbox

PDFDIR = os.getenv('PDFDIR')
conn = psycopg2.connect("")
queries = aiosql.from_path("pdf2db-em.sql", "psycopg2")

pdfs = queries.get_dc19pdf_list(conn)
for p in pdfs:
    print(p[1])

#
pdf_list = os.listdir(PDFDIR)
print(pdf_list)
