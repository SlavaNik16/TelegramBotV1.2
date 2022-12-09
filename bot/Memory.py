from aiogram.dispatcher.filters.state import StatesGroup, State

class Users(StatesGroup):
    Name = State()
    SurName = State()
    Phone = State()
    Kurs = State()
    NameInstitutions = State()
    InstitutionsTeachers = State()
    Date_Practic_Start = State()
    Date_Practic_End = State()
    NamePractic = State()
    Resumehh = State()
    Git = State()
    Login = State()
    Password = State()
    Password2 = State()
    InputLogin = State()
    InputPasswdord = State()