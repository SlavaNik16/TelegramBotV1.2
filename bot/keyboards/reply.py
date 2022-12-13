from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Reply:
    def Button(self, n=2, text=[]):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=n)
        for y in text:
            markup.insert(KeyboardButton(y))
        return markup
Rep = Reply()