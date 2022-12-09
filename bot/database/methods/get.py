import sqlite3
from bot.database.main import db
from bot.database.models import *

def get_Permission(message):
    db.cursor.execute(f'SELECT Permission FROM AccountingUser WHERE Id == {message.from_user.id}')
    data = db.cursor.fetchone()
    if data is not None and data[0] == 'True':
        return True
    return False

def get_IdUser(callback):
    people_id = callback.from_user.id
    db.cursor.execute(f'SELECT Id FROM AccountingUser WHERE Id == {people_id}')
    data = db.cursor.fetchone()
    return data

def Insert_User(message,login,passwd):
    user_acc = [message.from_user.id,
                        message.from_user.first_name,
                        message.from_user.last_name,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                       'User',
                        login,
                        passwd,
                        'False']
    db.cursor.execute('INSERT INTO AccountingUser VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', user_acc)
    db.connect.commit()

def get_UserEnt(message,loginUser, passwdUser):
    people = message.from_user.id
    db.cursor.execute(f'SELECT Permission, Id, Login, Password FROM AccountingUser '
                   f'WHERE Id = {people} AND Login = "{loginUser}" AND Password = "{passwdUser}"')
    data = db.cursor.fetchone()
    return data

def Is_Admin_list():
    db.cursor.execute(f"SELECT IdAdmin FROM IdAdmin")
    info = db.cursor.fetchall()
    return info

def get_UserInfo(message):
    db.cursor.execute(f'SELECT Name, SurName, Phone, Kurs, NameInstitutions, InstitutionsTeachers, Date_Start_Practic,'
                   f' Date_End_Practic, NamePractic, Resumehh, Git, Id, Modifier FROM AccountingUser '
                   f'WHERE Id == {message.from_user.id}')
    data = db.cursor.fetchone()
    return data
