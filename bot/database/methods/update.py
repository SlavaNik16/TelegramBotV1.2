from bot.database.main import *
from bot.database.methods.get import *
from bot.database.models import *

def Update_Permission(message,is_admin):

    db.cursor.execute(f'UPDATE AccountingUser SET Permission = "True", Modifier = "{is_admin}" WHERE Id == {message.from_user.id}')
    db.connect.commit()

def Update_Users_Privilage(message,privilage):
    db.cursor.execute(f'UPDATE Users SET Privilage = {privilage} WHERE IdUsers == {message.from_user.id}')
    db.connect.commit()

def Update_Permission_Off(callback):
    db.cursor.execute(f'UPDATE AccountingUser SET Permission = "False" WHERE Id == {callback.from_user.id}')
    db.connect.commit()

def Update_IsAdmin(message,is_admin):
    db.cursor.execute(f'UPDATE AccountingUser SET Modifier = "{is_admin}" WHERE Id == {message.from_user.id}')
    db.connect.commit()

async def Update_Rename(message,Name,SurName):
    try:
        db.cursor.execute(f"UPDATE AccountingUser SET Name = '{Name}', SurName = '{SurName}' WHERE Id == {message.from_user.id}")
        db.connect.commit()
    except:
        await message.answer('Несуществующие кавычки! Операция была отменена!')
async def Update_Phone(callback,phone):
    try:
        db.cursor.execute(f"UPDATE AccountingUser SET Phone = '{phone}' WHERE Id == {callback.from_user.id}")
        db.connect.commit()
    except:
        await callback.answer('Несуществующие кавычки! Операция была отменена!')

async def Update_Between(message, text, var1, var2):
    try:
        db.cursor.execute(f"UPDATE AccountingUser SET {var1} = '{var2}' WHERE Id == {message.from_user.id}")
        db.connect.commit()
        await message.answer(text)
    except:
        await message.answer('Несуществующие кавычки! Операция была отменена!')

async def Update_Data(message,DataStart,DataEnd):
    try:
        db.cursor.execute(f"UPDATE Practic SET DateStart = '{DataStart}', DateEnd = '{DataEnd}' "
                       f"WHERE Id == 1")
        db.connect.commit()
        await Update_Date_All(message,DataStart,DataEnd)
    except:
        await message.answer('Несуществующие кавычки! Операция была отменена!')

async def Update_Date_All(message,DataStart,DataEnd):
    try:
        db.cursor.execute(f"UPDATE AccountingUser SET Date_Start_Practic = '{DataStart}', Date_End_Practic = '{DataEnd}'")
        db.connect.commit()
    except:
        await message.answer('Несуществующие кавычки! Операция была отменена!')

def Delete_USER(id):
    db.cursor.execute(f"DELETE FROM Users WHERE IdUsers == '{id}'")
    db.connect.commit()

