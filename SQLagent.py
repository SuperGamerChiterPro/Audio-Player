import sqlite3


class SQLAgent:
    def __init__(self, name_db):
        self.db = sqlite3.connect(name_db)
        self.db.row_factory = sqlite3.Row

    def get_quizzes(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM Quizz")
        result = cursor.fetchall()
        cursor.close()

        return result


    def get_audio(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM Audio")
        result = cursor.fetchall()
        cursor.close()

        return result

    def get_audio_by_id(self, audio_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM Audio where ID = ?", [audio_id])
        result = cursor.fetchone()
        cursor.close()

        return result