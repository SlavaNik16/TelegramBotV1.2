from loguru import logger

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot.database import *
from bot.database.methods.get import *
from bot.ImagePhoto import image
from bot.utils import *

from bot.keyboards import *
from bot.handlers import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

async def Delete_MES(message,val1, val2):
    try:
        for i in range(val1, val1 + val2):
            #await message.delete(message.message_id - i)
            await bot.delete_message(message.chat.id,message.message_id - i)
    except:
        print()


@dp.message_handler(commands=['start'])
async def text(message:types.Message):
      mes = f'Привет {message.from_user.first_name} ' \
            f'{message.from_user.last_name}\n\r/id - посмотреть ваш id'
      await message.answer(mes)
      #image.generated_capthca()
      # photo = open('captcha.png','rb')
      #await bot.send_photo(message.chat.id, photo)
      await START.start(message)

@dp.message_handler(commands=['id'])
async def start(message: types.Message):
    await message.answer(f'Ваш Id: {message.from_user.id}')

@dp.callback_query_handler(text='Reg',state=None)
async def CallReg(callback: types.CallbackQuery,state: FSMContext):
    await Delete_MES(callback.message, 0, 2)
    data = get_IdUser(callback)
    if data is None:
       await Reg.Login(callback)
    else:
        await bot.send_message(callback.message.chat.id, 'Такой пользователь уже существует!')
        await state.finish()

@dp.message_handler(state=Users.Login)
async def Log(message: types.Message, state: FSMContext):
    global login
    login = message.text
    await Reg.Password1(message)

@dp.message_handler(state=Users.Password)
async def Passwd(message: types.Message, state: FSMContext):
    global passwd
    passwd = message.text
    await Reg.Password2(message)

@dp.message_handler(state=Users.Password2)
async def Passwd2(message: types.Message, state: FSMContext):
    passwd2 = message.text
    if (passwd2 == passwd):
        Insert_User(message,login,passwd)
        await message.answer('Регистрация прошла успешна! Войдите в профиль /start')
    else:
        await message.answer('Неправильный пароль! Повторите попытку снова!')
    await state.finish()



@dp.callback_query_handler(text='Ent',state=None)
async def CallEnt(callback: types.CallbackQuery,state: FSMContext):
    if get_Permission(callback.message):
        await bot.send_message(callback.message.chat.id, 'Вы уже вошли в профиль!')
        await state.finish()
    else:
        await Ent.InputLogin(callback)
    await Delete_MES(callback.message, 0, 4)

@dp.message_handler(state=Users.InputLogin)
async def InputLog(message: types.Message, state: FSMContext):
    global loginUser
    loginUser = message.text
    await Ent.InputPassword(message)

@dp.message_handler(state=Users.InputPasswdord)
async def InputPasswd(message: types.Message, state: FSMContext):
    global passwdUser
    passwdUser = message.text
    data = get_UserEnt(message,loginUser, passwdUser)
    if data is not None:
        info = Is_Admin_list()
        admin = Admin.ValAdmin(message,info)
        Update_Permission(message,admin)
        await message.answer('Вы успешно вошли в профиль!')
        await message.answer( 'Чтобы ознакомится с ботом введите /Menu')
    else:
        await message.answer('Введен неправильный логин или пароль! Возможно вы не зарегистрировались!')
    await state.finish()


@dp.message_handler(commands=['Exit'])
async def exit(message: types.Message):
    if get_Permission(message):
        markup = In.Button(1, ['Выход'], ['exit'])
        await message.answer('Можете выйти из профиля', reply_markup=markup)
    else:
        await message.answer('Вы уже вышли из профиля! Чтобы зайти обратно, введите /start')


@dp.callback_query_handler(text='exit')
async def CallExit(callback: types.CallbackQuery):
      Update_Permission_Off(callback)
      await callback.answer('Вы успешно вышли из профиля!')
      await Delete_MES(callback.message, 0, 1)
      await callback.message.answer('Чтобы вновь войти в учетную запись пропишите /start')

@dp.message_handler(commands =['Menu'])
async def Menu(message: types.Message):
    if get_Permission(message):
       await MENU.Menu_Info(message)
    else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(commands = ['Rename'],state=None)
async def Rename(message: types.Message):
    if get_Permission(message):
        await Objects.Name(message)
    else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(state=Users.Name)
async def InputName(message: types.Message, state:FSMContext):
    global Name
    Name = message.text
    await Objects.SurName(message)

@dp.message_handler(state = Users.SurName)
async def InputSurName(message:types.Message, state:FSMContext):
    SurName = message.text
    await Update_Rename(message,Name,SurName)
    await message.answer('Смена имени прошла успешно!')
    await state.finish()

@dp.message_handler(commands = ['Practic'])
async def Practic(message: types.Message):
    if get_Permission(message):
        await message.answer('Вы готовы к практике, тогда переходите по ссылке!')
        markup = In.ButtonURL(1,['Перейти'],['https://t.me/+0Y9hJclUaNI4NzAy'])
        await message.answer('Нажимая на ссылку, вы готовы перейти в практику!!!', reply_markup=markup)
    else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(commands = ['AllCommands'])
async def AllCommands(message: types.Message):
    if get_Permission(message):
        await message.answer('Все команды!')
        await message.answer(
                 'Команды на изменение информации пользователя:\n\r/Phone - изменяет номер телефона;'
                 '\n\r/Kurs - изменяет курс;\n\r/NameInstitutions - изменяет название учреждения;'
                 '\n\r/InstitutionsTeachers - изменяет куратора от учреждения;'
                 '\n\r/Date_Practic - меняет начало и конец даты практики;\n\r/NamePractic - меняет название практики;'
                 '\n\r/Resumehh - добавляет ссылку на ваше резюме hh.ru;\n\r/Git - добавляет ссылку на GitHub и т.п.')
    else:
        await message.answer('Войдите в профиль!')


@dp.message_handler(commands = ['Developer'])
async def Developer(message: types.Message):
    await message.answer('Бота создал студент 3 курса группы ИП-20-3 Николаев Вячеслав')


@dp.message_handler(commands = ['Info'])
async def Info(message: types.Message):
     if get_Permission(message):
        data = get_UserInfo(message)
        await message.answer(
                         f'Вся известная информация:\n\rId: {data[11]}\n\rИмя: {data[0]}\n\rФамилия: {data[1]}\n\r'
                         f'Тип пользователя: {data[12]}\n\rТелефон: {data[2]}\n\rКурс: {data[3]}\n\r'
                         f'Название учреждения: {data[4]}\n\rКуратор от учреждения: {data[5]}\n\r'
                         f'Начало/Конец практики: {data[6]}-{data[7]}\n\rНазвание практики: {data[8]}\n\r'
                         f'Резюме на hh.ru : {data[9]}\n\rGit: {data[10]}')
        if data[12] == 'Admin':
            doc = open('users2.db','rb')
            await bot.send_document(message.chat.id, doc)
        await message.answer('Если вы хотите изменить информацию, тогда нажмите /AllCommands')
     else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(commands = ['Phone'], state=None)
async def Phone(message: types.Message):
    if get_Permission(message):
        await Objects.Phone(message)
    else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(state = Users.Phone)
async def InputPhone(message: types.Message, state: FSMContext):
    try:
        global phone
        phone = int(message.text)
        text = ['Да','Отменить']
        call = ['Phone','Cansel']
        markup = In.Button(2,text,call)
        await state.finish()
        if (len(message.text) == 11):
            await message.answer(f'Вы уверены, что вы ввели правильный номер телефона ({phone})!',
                                   reply_markup=markup)
        else:
            await message.answer("Длина не соответствует требованиям! Номер должен содержать 11 цифр!")
    except:
        await message.answer('Неверный формат! Введите номер ТОЛЬКО ЦИФРАМИ!')
        await state.finish()

@dp.callback_query_handler(text='Phone')
async def CallPhone(callback: types.CallbackQuery):
    await Delete_MES(callback.message, 0, 1)
    await Update_Phone(callback,phone)
    await callback.message.answer('Номер успешно изменен!')

@dp.callback_query_handler(text='Cansel')
async def CallCansel(callback: types.CallbackQuery):
    await callback.answer('Операция успешно отменена!')
    await Delete_MES(callback.message,0,4)

@dp.message_handler(commands = ['Kurs'],state=None)
async def Kurs(message: types.Message, state: FSMContext):
    if get_Permission(message):
        await Objects.Kurs(message)
    else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(state=Users.Kurs)
async def InputKurs(message: types.Message, state: FSMContext):
        try:
            kurs = int(message.text)
            if (len(message.text) == 1):
                if (kurs > 0 and kurs < 5):
                    await Update_Between(message, 'Курс успешно сменен!', 'Kurs', kurs)
                    await state.finish()
                else:
                    await message.answer('Не может быть такого курса!')
            else:
                await message.answer('Длина не соответствует требованиям! Номер должен содержать 1 цифру!')
        except:
            await message.answer('Неверный формат! Введите номер ТОЛЬКО ЦИФРОЙ')
        await state.finish()


@dp.message_handler(commands = ['NameInstitutions'],state=None)
async def NameInstitutions(message: types.Message):
    if get_Permission(message):
        await Objects.NameInstitutions(message)
    else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(state=Users.NameInstitutions)
async def InputNameInstitutions(message: types.Message, state: FSMContext):
    NameInst = message.text
    await Update_Between(message, 'Название учреждения изменено!', 'NameInstitutions', NameInst)
    await state.finish()


@dp.message_handler(commands = ['InstitutionsTeachers'],state=None)
async def InstitutionsTeachers(message: types.Message):
    if get_Permission(message):
        await Objects.InstitutionsTeachers(message)
    else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(state=Users.InstitutionsTeachers)
async def InputInstitutionsTeachers(message: types.Message, state: FSMContext):
    NameTeach = message.text
    await Update_Between(message, 'Название куратора от учреждения изменено!', 'InstitutionsTeachers', NameTeach)
    await state.finish()

@dp.message_handler(commands = ['Date_Practic'],state=None)
async def Date_Practic(message: types.Message):
    if get_Permission(message):
        await Objects.Date_Practic_Start(message)
    else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(state=Users.Date_Practic_Start)
async def InputDataStart(message: types.Message, state: FSMContext):
    global DataStart
    DataStart = message.text
    if await Validate.Data(message, DataStart):
       await Objects.Date_Practic_End(message)
    else:
        await state.finish()

@dp.message_handler(state=Users.Date_Practic_End)
async def InputDataEnd(message: types.Message, state: FSMContext):
    DataEnd = message.text
    await state.finish()
    if await Validate.Data(message, DataEnd):
        await Update_Data(message,DataStart,DataEnd)
        await message.answer('Дата практики изменена!')

@dp.message_handler(commands = ['NamePractic'],state=None)
async def NamePractic(message: types.Message):
    if get_Permission(message):
        await Objects.NamePractic(message)
    else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(state=Users.NamePractic)
async def InputNamePractic(message: types.Message, state: FSMContext):
    NamePractic = message.text
    await Update_Between(message, 'Название практики изменено!', 'NamePractic', NamePractic)
    await state.finish()

@dp.message_handler(commands = ['Resumehh'],state=None)
async def Resumehh(message: types.Message):
    if get_Permission(message):
        await Objects.Resumehh(message)
    else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(state=Users.Resumehh)
async def InputResumehh(message: types.Message, state: FSMContext):
    Resumehh = message.text
    await Update_Between(message, 'Ссылка на резюме hh.ru  изменена!', 'Resumehh', Resumehh)
    await state.finish()

@dp.message_handler(commands = ['Git'],state=None)
async def Git(message: types.Message):
    if get_Permission(message):
        await Objects.Git(message)
    else:
        await message.answer('Войдите в профиль!')

@dp.message_handler(state=Users.Git)
async def InputGit(message: types.Message, state: FSMContext):
    git = message.text
    await Update_Between(message, 'Ссылка Git изменена!', 'Git', git)
    await state.finish()

@dp.message_handler(content_types=['text'])
async def text(message:types.Message):
      await TEXT.get_user_text(message)

def start_bot():
    executor.start_polling(dp, skip_updates=True)