from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message,CallbackQuery
from bot.Memory import Users
from bot.keyboards import *

class IsUsers:
    def ValUsers(self, message: Message, Id):
        person = message.from_user.id
        try:
              if person == Id[0]:
                  return True
              return False
        except:
              return False
user = IsUsers()


class Reg:
      async def Login(call):
            await call.message.answer('Введите логин:')
            await Users.Login.set()
      async def Password1(message):
            await message.answer('Введите пароль:')
            await Users.Password.set()
      async def Password2(message):
            await message.answer('Введите пароль еще раз:')
            await Users.Password2.set()

class Ent:
      async def InputLogin(call):
            await call.message.answer('Введите логин:')
            await Users.InputLogin.set()
      async def InputPassword(message):
            await message.answer('Введите пароль:')
            await Users.InputPasswdord.set()

class Objects:
      async def Name(message):
            await message.answer('Введите новое имя:')
            await Users.Name.set()
      async def SurName(message):
            await message.answer('Введите Фамилию:')
            await Users.SurName.set()

      async def Phone(message):
            await message.answer('Введите новый телефон: ')
            await Users.Phone.set()

      async def Kurs(message):
            await message.answer('Введите курс: ')
            await Users.Kurs.set()

      async def NameInstitutions(message):
            await message.answer('Введите новое название учреждения: ')
            await Users.NameInstitutions.set()

      async def InstitutionsTeachers(message):
            await message.answer('Введите нового куратора от учреждения:')
            await Users.InstitutionsTeachers.set()

      async def Date_Practic_Start(message):
            await message.answer('Введите новую дату!\n\rСоблюдайте формат(2 пары по 2 цифры, разделенные '
                                 'точкой и полный год ): день.месяц.год (пример: 01.12.2022)')
            await message.answer('Начало практики: ')
            await Users.Date_Practic_Start.set()
      async def Date_Practic_End(message):
            await message.answer('Конец практики: ')
            await Users.Date_Practic_End.set()

      async def NamePractic(message):
            await message.answer('Введите новое название практики: ')
            await Users.NamePractic.set()

      async def Resumehh(message):
            await message.answer('Вставьте ссылку резюме на hh.ru: ')
            await Users.Resumehh.set()

      async def Git(message):
            await message.answer('Вставьте ссылку на полезные материалы(github, gitlub и т.п.): ')
            await Users.Git.set()

class Capthca_Input:
      async def Output(message):
            await message.answer('Вы слишком много спамили! Введите капчу, чтобы подтвердить что вы не робот!')
            await message.answer('У вас 20 попыток, иначе вас забанят из бота!')
            await message.answer('Так что же изображено на рисунке: ')
            await Users.Captcha.set()


class AccountUsers:
      async def Add(message):
            await message.answer('Введите id пользователя, которого вы хотите добавить: ')
            await Users.AddUsers.set()
      async def Delete(message):
            await message.answer('Введите id, пользователя которого хотите удалить: ')
            await Users.DeleteUsers.set()





