import sqlite3

class DatabaseHandler:
    _instance = None

    def __new__(cls, db_name="healthybite.db"):
        if cls._instance is None:
            cls._instance = super(DatabaseHandler, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(db_name)
            cls._instance.cursor = cls._instance.connection.cursor()
            cls._instance.create_table()
        return cls._instance

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT,
                ingredients TEXT,
                instructions TEXT,
                prep_time INTEGER
            )
        ''')
        self.connection.commit()

    def insert_recipe(self, name, category, ingredients, instructions, prep_time):
        self.cursor.execute('''
            INSERT INTO recipes (name, category, ingredients, instructions, prep_time)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, category, ingredients, instructions, prep_time))
        self.connection.commit()

    def get_all_recipes(self):
        self.cursor.execute("SELECT * FROM recipes")
        return self.cursor.fetchall()
