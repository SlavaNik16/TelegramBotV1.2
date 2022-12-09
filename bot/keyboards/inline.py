from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import bot

class Inline:
     def Button(self, n, text = [], callback = []):
        markup = InlineKeyboardMarkup(row_width=n)
        for y,z in zip(text,callback):
           markup.insert(InlineKeyboardButton(y, callback_data=z))
        return markup
     def ButtonURL(self, n, text = [], url = []):
         markup = InlineKeyboardMarkup(row_width=n)
         for y, z in zip(text, url):
             markup.insert(InlineKeyboardButton(y, url=z))
         return markup
In = Inline()