import sqlite3


class Tracker:
    def __init__(self, path):
        self.database = sqlite3.connect(path)
