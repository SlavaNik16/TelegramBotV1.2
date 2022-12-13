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
                            Modifier INTEGER,
                            Login TEXT NOT NULL,
                            Password TEXT NOT NULL,
                            Permission TEXT
                         )""")
            db.connect.commit()

    def IdUsers(self):
        db.cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
                              IdUsers INTEGER UNIQUE NOT NULL PRIMARY KEY,
                              Privilage INTEGER
                              )""")
        db.connect.commit()

    def Practic(self):
        db.cursor.execute("""CREATE TABLE IF NOT EXISTS Practic(
                                Id INTEGER UNIQUE NOT NULL PRIMARY KEY,
                                DateStart TEXT NOT NULL,
                                DateEnd TEXT
                                 )""")
        db.connect.commit()

    def Anonim(self):
        db.cursor.execute("""CREATE TABLE IF NOT EXISTS Anonim(
                                       Id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                                       Name TEXT,
                                       SurName TEXT,
                                       Message TEXT
                                        )""")
        db.connect.commit()


