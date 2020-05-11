import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')

cursor = conexion.cursor()
query = 'SELECT * FROM persona WHERE id_persona = %s'
id_persona = int(input("Proporciona la pk a buscar: "))
llave_primaria = (id_persona,)
cursor.execute(query, llave_primaria)
registros = cursor.fetchone()
print(registros)

cursor.close()
conexion.close()
