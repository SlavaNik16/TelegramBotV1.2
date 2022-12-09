from .main import *

class Table:
    def AccountingUser(self):
            db.cursor.execute("""CREATE TABLE IF NOT EXISTS AccountingUser(
                            Id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                            Name TEXT,
                            SurName TEXT,
                            Phone INTEGER(11),
                            Kurs INTEGER(1),
                            NameInstitutions TEXT,
                            InstitutionsTeachers TEXT,
                            Date_Start_Practic TEXT(8),
                            Date_End_Practic TEXT(8),
                            NamePractic TEXT,
                            Resumehh TEXT,
                            Git TEXT,
                            Modifier TEXT,
                            Login TEXT NOT NULL,
                            Password TEXT NOT NULL,
                            Permission TEXT
                         )""")
            db.connect.commit()
    def IdAdmin(self):
            db.cursor.execute("""CREATE TABLE IF NOT EXISTS IdAdmin(
                           IdAdmin INTEGER UNIQUE NOT NULL  PRIMARY KEY
                           )""")
            db.connect.commit()
