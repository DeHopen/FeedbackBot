from aiogram import types



menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    types.KeyboardButton('Админка')
)

adm = types.ReplyKeyboardMarkup(resize_keyboard=True)
adm.add(
    types.KeyboardButton('ЧС'),
    types.KeyboardButton('Добавить в ЧС'),
    types.KeyboardButton('Убрать из ЧС')
)
adm.add(types.KeyboardButton('Рассылка'))
adm.add('Назад')

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(
    types.KeyboardButton('Отмена')
)


def fun(user_id):
    quest = types.InlineKeyboardMarkup(row_width=3)
    quest.add(
        types.InlineKeyboardButton(text='Ответить', callback_data=f'{user_id}-ans'),
        types.InlineKeyboardButton(text='Удалить', callback_data='ignor')
    )
    return quest
fqa = types.ReplyKeyboardMarkup(resize_keyboard=True)
fqa.add(
    types.KeyboardButton('Часто задаваемые вопросы'),
    types.KeyboardButton('Задать вопрос')
)
fqa.add(types.KeyboardButton('Кураторы'))
off = types.ReplyKeyboardMarkup(resize_keyboard=True)
off.add(
    types.KeyboardButton('Отменить')
)

fqamenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
fqamenu.add(
    types.KeyboardButton('Бюджет'),
    types.KeyboardButton('Заполнение договоров'),
    types.KeyboardButton('Сроки подачи документов')
)
fqamenu.add(types.KeyboardButton('Вопросы по Tinder'))
fqamenu.add(types.KeyboardButton('Меню'))

dog = types.ReplyKeyboardMarkup(resize_keyboard=True)
dog.add(
    types.KeyboardButton('Олимпиадники'),
    types.KeyboardButton('Грант+бюджет')
)
dog.add('Вернуться')
kurat = types.ReplyKeyboardMarkup(resize_keyboard=True)
kurat.add(
    types.KeyboardButton('Елена Хузина'),
    types.KeyboardButton('Ксения Бусыгина')
)
kurat.add(types.KeyboardButton('Меню'))
