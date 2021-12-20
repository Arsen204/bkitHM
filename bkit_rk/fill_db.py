import psycopg2

db = psycopg2.connect(
    host="localhost",
    user="arsenvardumyan",
    dbname="rk_db"
)

c = db.cursor()

# c.execute('INSERT INTO "app_processor" (name, frequency) VALUES (%s, %s);',
#           ('AMD Ryzen 5 3600', 3.6))
#
# c.execute('INSERT INTO "app_processor" (name, frequency) VALUES (%s, %s);',
#           ('AMD Athlon 3000G', 3.5))
#
# c.execute('INSERT INTO "app_processor" (name, frequency) VALUES (%s, %s);',
#           ('INTEL Core i3 10100F', 3.6))
#
# c.execute('INSERT INTO "app_processor" (name, frequency) VALUES (%s, %s);',
#           ('INTEL Core i5 10400F', 2.9))
#
# c.execute('INSERT INTO "app_processor" (name, frequency) VALUES (%s, %s);',
#           ('AMD A6 9500', 3.5))
#
# db.commit()

c.execute('INSERT INTO "app_computer" (name, processor_id) VALUES (%s, %s);',
          ('Ноутбук ACER Nitro 5 AN515-45-R9UX', 1))

c.execute('INSERT INTO "app_computer" (name, processor_id) VALUES (%s, %s);',
          ('Компьютер ACER Aspire XC-895', 4))

c.execute('INSERT INTO "app_computer" (name, processor_id) VALUES (%s, %s);',
          ('Компьютер ACER Aspire XC-830', 2))

c.execute('INSERT INTO "app_computer" (name, processor_id) VALUES (%s, %s);',
          ('Ноутбук LENOVO IdeaPad S145-15API', 1))

c.execute('INSERT INTO "app_computer" (name, processor_id) VALUES (%s, %s);',
          ('Компьютер IRU Home 615', 3))

c.execute('INSERT INTO "app_computer" (name, processor_id) VALUES (%s, %s);',
          ('Ноутбук HP 15-dw1126ur', 5))

db.commit()

c.close()
db.close()
