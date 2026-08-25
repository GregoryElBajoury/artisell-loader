import os
import time
import psycopg2

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "artisell")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")

def wait_and_load():
    print("Connexion à la base de données PostgreSQL...")
    conn = None
    
    while conn is None:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                port=DB_PORT
            )
        except psycopg2.OperationalError:
            print("PostgreSQL n'est pas encore prêt, nouvelle tentative dans 2 secondes...")
            time.sleep(2)

    cursor = conn.cursor()
    
    # Création de la table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produits (
            id SERIAL PRIMARY KEY,
            nom VARCHAR(100) NOT NULL,
            prix NUMERIC(10, 2) NOT NULL,
            stock INT NOT NULL
        );
    """)
    
    # Insertion de fausses données
    fausses_donnees = [
        ('Clavier mécanique RGB', 79.99, 15),
        ('Souris sans fil ergonomique', 29.99, 42),
        ('Écran 24 pouces Full HD', 149.00, 8),
        ('Casque audio circum-aural', 59.99, 23),
        ('Tapis de souris XXL', 19.99, 50)
    ]
    
    cursor.execute("DELETE FROM produits;")
    cursor.executemany("""
        INSERT INTO produits (nom, prix, stock) VALUES (%s, %s, %s);
    """, fausses_donnees)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Données chargées avec succès dans la base !")

if __name__ == "__main__":
    wait_and_load()