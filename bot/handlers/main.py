from aiogram import Dispatcher, types
import random
import bot
from bot.handlers.user import *
from bot.handlers.admin import *

BOT_MES = {
        'Intents':{
            'Greeting': {
                'Example': ['Привет!','Хай!','Добрый день!','Новый день настал!'
                    ,'Ну, вот поспали — теперь можно и поесть!'],
                'Resposes':['прив','хаюхай', 'добрового времени суток',"hello","привет"],
            },
            'Bue': {
                'Example': ['Пока!', 'Доброй ночи!', 'До завтра!', 'Счастливо!','До скорого!'],
                'Resposes': ['пока', 'спокойной ночи', 'ночи', 'bue'],
            }
        }
    }

class Output:
    async def get_user_text(self,message: Message):
        if get_Permission(message):
            mes = self.get_privets(message.text.lower())
            if mes != 'Не найдена':
                await message.answer(mes)
            else:
                await message.reply(f'Пользователь написал:\n{message.text}!')
        else:
            await message.answer('Пожалуйста войдите в учетную запись! /start')

    def get_privets(self,text):
        for hello, value in BOT_MES['Intents'].items():
            for examples in value['Resposes']:
                if examples == text:
                    return random.choice(BOT_MES['Intents'][hello]['Example'])
        return 'Не найдена'

TEXT = Output()

class Start:
    async def start(self,message:types.Message):
        if not get_Permission(message):
            text = ['Регистрация', 'Войти!']
            call = ['Reg','Ent']
            markup = In.Button(4, text, call)
            await message.answer('Пожалуйста Зарегистрируйтесь или Войдите в профиль', reply_markup=markup)
        else:
            await message.answer('Вы уже вошли в профиль, пожалуйста ознакомьтесь с меню команд /Menu')

START = Start()

class Menu:
    async def Menu_Info(self,message: types.Message):
            info = get_UserInfo(message)
            if info[12] >= 10:
                list = ['/Rename', '/Practic', '/AllCommands', '/Developer','/AddUsers','/DeleteUsers', '/Info', '/Update', '/Exit']
                markupMenu = Rep.Button(2, list)
                await message.answer(
                    'Меню - Здесь есть возможность:\n\r* /Rename - поменять свое ФИО, если вы зарегистрировались '
                    'в телеграмме вымышленным ФИО;'
                    '\n\r* /Practic - перейти на практику;\n\r* /AllCommands - посмотреть всевозможные команды;'
                    '\n\r* /Developer - узнать кто разработал бота;\n\r* /AddUsers - Добавление пользователя'
                    '\n\r* /DeleteUsers - удаление пользователей\n\r* /Info - посмотреть всю информацию о вас;'
                    '\n\r* /Update - обновление всей информации;\n\r* /Exit - выход из профиля.',
                    reply_markup=markupMenu
                )
            else:
                list = ['/Rename','/Practic','/AllCommands','/Developer','/Info','/Update','/Exit']
                markupMenu = Rep.Button(2, list)
                await message.answer(
                    'Меню - Здесь есть возможность:\n\r* /Rename - поменять свое ФИО, если вы зарегистрировались '
                    'в телеграмме вымышленным ФИО;'
                    '\n\r* /Practic - перейти на практику;\n\r* /AllCommands - посмотреть всевозможные команды;'
                    '\n\r* /Developer - узнать кто разработал бота;'
                    '\n\r* /Info - посмотреть всю информацию о вас;\n\r* /Update - обновление всей информации;'
                    '\n\r* /Exit - выход из профиля.',
                    reply_markup=markupMenu
            )
MENU = Menu()

class Validate:
    async def Data(message, data):
        global run
        try:
            timeStr = data.split('.')
            time = [int(timeStr[i]) for i in range(3)]
            daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            run = True
            if time[1] > 12 or time[1] < 1:
                await message.answer('Несуществующий день/месяц !')
                run = False
            elif time[0] > daysInMonth[time[1] - 1] or time[0] < 1:
                await message.answer('Несуществующий день/месяц !')
                run = False
            elif time[2] < 2000 or time[2] >= 3000:
                await message.answer('Несуществующий день/месяц !')
                run = False
            return run
        except:
            await message.answer('Неверный формат!')
DATA = Validate




