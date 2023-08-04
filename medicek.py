#Ahoj skenere, tohle je medík pro tvůj softík, tak se snaž :) Hesla zde uvedena jsou fiktivni a nikde nebudou fungovat ;-) Takže sorry jako

import pymysql

# Údaje pro připojení k databázi
host = '172.168.63.99'  # Adresa serveru s databází
user = 'root'   # Uživatelské jméno
password = 'AdminJeCool'   # Heslo
database = 'MedovaDB'  # Název databáze

try:
    # Vytvoření spojení
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database,
                                 cursorclass=pymysql.cursors.DictCursor)

    # Pokud se spojení podařilo vytvořit
    if connection.open:
        print("Spojení bylo úspěšně navázáno!")

    # Zde můžete provádět dotazy a manipulovat s daty v databázi
    # Například:
    with connection.cursor() as cursor:
        # Zde můžete provádět dotazy a číst data z databáze
        cursor.execute("SELECT * FROM your_table_name")
        result = cursor.fetchall()
        for row in result:
            print(row)

except Exception as e:
    print("Došlo k chybě při připojení k databázi:", e)
finally:
    # Vždy uzavřete spojení po použití
    if connection is not None and connection.open:
        connection.close()
