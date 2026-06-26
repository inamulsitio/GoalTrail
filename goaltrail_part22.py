# === Stage 22: Add favorite records and quick favorite listing ===
# Project: GoalTrail
class FavoriteManager:
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self._create_favorites_table()

    def _create_favorites_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                record_id INTEGER UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.db.commit()

    def add_favorite(self, record_id: int):
        try:
            self.cursor.execute('INSERT INTO favorites (record_id) VALUES (?)', (record_id,))
            self.db.commit()
        except sqlite3.IntegrityError:
            pass  # Already favorited

    def remove_favorite(self, record_id: int):
        self.cursor.execute('DELETE FROM favorites WHERE record_id = ?', (record_id,))
        self.db.commit()

    def is_favorited(self, record_id: int) -> bool:
        cursor = self.cursor.execute('SELECT 1 FROM favorites WHERE record_id = ?', (record_id,))
        return cursor.fetchone() is not None

    def get_favorite_records(self):
        cursor = self.cursor.execute('''
            SELECT r.id, r.title, r.description, r.created_at
            FROM records r
            JOIN favorites f ON r.id = f.record_id
            ORDER BY f.created_at DESC
        ''')
        return cursor.fetchall()

    def close(self):
        self.db.close()
