import csv
import sqlite3
import os

def main():
    # Ruta al archivo CSV
    csv_path = os.path.join(os.path.dirname(__file__), 'static', 'desersion_escolar.csv')

    # Ruta para la base de datos SQLite
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'desersion_escolar.db')

    # Nombre de la tabla
    table_name = 'desersion_escolar'

    # Leemos encabezado del CSV
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')  
        headers = next(reader)

    # Creamos la conexión a SQLite
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Creamos la tabla
    cur.execute(f'DROP TABLE IF EXISTS {table_name}')
    cur.execute(f'''
        CREATE TABLE {table_name} (
            {', '.join([f'"{col}" TEXT' for col in headers])}
        )
    ''')

    # Insertamos los datos
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';') 
        next(reader)  
        for row in reader:
            placeholders = ', '.join('?' * len(row))
            cur.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', row)

    conn.commit()
    conn.close()

    print(f'Datos importados exitosamente a {db_path}')

if __name__ == '__main__':
    main()
