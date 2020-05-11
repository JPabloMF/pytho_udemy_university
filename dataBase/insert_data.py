import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')

cursor = conexion.cursor()
query = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
valores = ('Carlos','Lara','clara@hotmail.com')
cursor.execute(query, valores)
# guardamos la informacion en la base de datos
conexion.commit()
registros_insertados = cursor.rowcount
print(f'Registros isertados: {registros_insertados}')

cursor.close()
conexion.close()
