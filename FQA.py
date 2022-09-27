#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN, admin, admin1
import keyboard as kb
import functions as func
import sqlite3
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import Throttled

storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
connection = sqlite3.connect('data.db')
q = connection.cursor()

class st(StatesGroup):
	item = State()
	item2 = State()
	item3 = State()
	item4 = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin or message.chat.id == admin1:
			await message.answer('Добро пожаловать, администратор.', reply_markup=kb.menu)
		else:
			await message.answer('Приветствую, это бот-помощник.\nНапиши мне свой вопрос и вам ответят в ближайшее время.\nЗа спам/флуд - ЧС!\n\nP.S. Информация неофициальная, уточнайте у кураторов', reply_markup=kb.fqa)
	else:
		await message.answer('Ваш аккаунт заблокирован в данном боте.')


@dp.message_handler(content_types=['text'], text='Админка')
async def handfler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin or message.chat.id == admin1:
			await message.answer('Добро пожаловать в админ-панель.', reply_markup=kb.adm)

@dp.message_handler(content_types=['text'], text='Назад')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('Добро пожаловать, администратор.', reply_markup=kb.menu)

@dp.message_handler(content_types=['text'], text='ЧС')
async def handlaer(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin or message.chat.id == admin1:
			q.execute(f"SELECT * FROM users WHERE block == 1")
			result = q.fetchall()
			sl = []
			for index in result:
				i = index[0]
				sl.append(i)

			ids = '\n'.join(map(str, sl))
			await message.answer(f'ID пользователей в ЧС:\n{ids}')

@dp.message_handler(content_types=['text'], text='Добавить в ЧС')
async def hanadler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin or message.chat.id == admin1:
			await message.answer('Введите id пользователя, которого нужно заблокировать.\nДля отмены нажмите кнопку ниже', reply_markup=kb.back)
			await st.item3.set()

@dp.message_handler(content_types=['text'], text='Убрать из ЧС')
async def hfandler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin or message.chat.id == admin1:
			await message.answer('Введите id пользователя, которого нужно разблокировать.\nДля отмены нажмите кнопку ниже', reply_markup=kb.back)
			await st.item4.set()

@dp.message_handler(content_types=['text'], text='Рассылка')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin or message.chat.id == admin1:
			await message.answer('Введите текст для рассылки.\n\nДля отмены нажмите на кнопку ниже', reply_markup=kb.back)
			await st.item.set()
@dp.message_handler(content_types=['text'], text='Задать вопрос')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('Опишите по подробнее вашу проблему', reply_markup=kb.off)
		fqa()
@dp.message_handler(content_types=['text'], text='Отменить')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('Какой вопрос вас интересует?', reply_markup=kb.fqa)
@dp.message_handler(content_types=['text'], text='Часто задаваемые вопросы')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('Какой вопрос вас интересует?', reply_markup=kb.fqamenu)
@dp.message_handler(content_types=['text'], text='Вопросы по Tinder')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('Q: Если комната уже сформирована, нужно ли проходить?\n\n'
												 'A: Да, причём каждый участник комнаты должен самостоятельно ответить на вопросы бота,\n переслав анкеты соседей (необходимо понимать, что для корректного распределения и сохранения комнаты в задуманном виде нельзя подписываться на сторонние анкеты).\n\n'
												 'Q: «What is your name?» - отвечать имя или алиас?\n'
												 'A: Ответом на данный вопрос является ваше имя (алиас подтягивается  автоматически).\n\n'
												 'Q: Если у меня или моего соседа нет анкеты, что делать?\n'
												 'A: Бот не смотрит на содержание пересланной анкеты, он лишь ищет алиас - отправьте его.\n\n'
							 					 'Q: Как претендовать на двушку?\n'
							 					 'A: Вы и человек, с которым вы же предварительно договорились, должны быть подписанными на друг друга, но ни на кого больше.', reply_markup=kb.fqamenu)
@dp.message_handler(content_types=['text'], text='Сроки подачи документов')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('*ГРАНТ - ЭТО ПЛАТКА*\n\n'
							 'БЮДЖЕТ\n\n'
							 '26 июля - Завершение приема документов от лиц, поступающих по результатам ЕГЭ\n\n'
							 '27 июля - Размещение рейтинговых списков\n\n'
							 '28 июля - Прием заявлений о согласии на зачисление на приоритетном этапе\n(для поступающих по льготе, на целевое обучение, победители и призеры олимпиад без вступительных испытаний)\n\n'
							 '30 июля - Издаются приказы о зачислении (для поступающих по льготе, на целевое обучение, победители и призеры олимпиад без вступительных испытаний)\n\n'
							 '3 августа - Завершение приема заявлений о согласии на зачислениена основном этапе\n\n'
							 '9 августа - Издается приказ о зачислении\n\n\n'
							 'ГРАНТ\n\n'
							 'С 20 июня до 12 августа - Прием заявлений от лиц, поступающих по результатам ЕГЭ'
							 'С 20 июня до 12 августа - Прием заявлений от лиц, сдающих внутренние вступительные испытания\n(право имеют поступающие на базе СПО; иностранные абитуриенты; лица с ОВЗ)\n\n'
							 'с 11 июля по 16 августа - Сроки проведения внутренних вступительных испытаний\n\n'
							 '17 августа - Завершение приема заявлений о согласии на зачисление\n\n'
							 '18 августа - Издается приказ о зачислении', reply_markup=kb.fqamenu)
@dp.message_handler(content_types=['text'], text='Бюджет')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('Чтоб получить бюджет нужно отправлять аттестат или документы можно привезти самому у Иннополис\nЕсли уже заполнены печатные формы заявлений и договоров, то можно и их.\nНужно отправить до 26 июля по адресу:\nг.Иннополис ул.Университетская д.1\n8(843)203-92-53(вн.113)\nАНО ВО "Университет Иннополис"(Хузиной Елене, приемная комиссия)', reply_markup=kb.fqamenu)
@dp.message_handler(content_types=['text'], text='Заполнение договоров')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('Выберете какой договор вам нужен', reply_markup=kb.dog)
@dp.message_handler(content_types=['text'], text='Кураторы')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('По вопросам заполнения формы и подготовки документов для зачисления обращайтесь:\n'
							 'Елена Хузина\n(Секретарь Приемной комиссии Университета Иннополис)\n\n\n'
							 'По остальным вопросам обращайтесь к:\n'
							 'Ксения Бусыгина\n(Куратор набора в бакалавриат)', reply_markup=kb.kurat)
@dp.message_handler(content_types=['text'], text='Елена Хузина')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('Телефон: +7-843-203-92-53 (доб. 113)\n\nE-mail: e.maltseva@innopolis.ru', reply_markup=kb.kurat)
@dp.message_handler(content_types=['text'], text='Ксения Бусыгина')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('Телефон: +7-843-203-92-53 (доб. 183)\n\nE-mail: admissions@innopolis.ru\n\nVK: https://vk.com/kseniia_iu\n\nТелеграм: https://t.me/kseniia_busygina', reply_markup=kb.kurat)
@dp.message_handler(content_types=['text'], text='Олимпиадники')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		photo = open("/root/bot/IMG_20220714_122548_314.jpg", 'rb')
		await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=kb.dog)
@dp.message_handler(content_types=['text'], text='Грант+бюджет')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		photo = open("/root/bot/IMG_20220714_122540_648.jpg", 'rb')
		await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=kb.dog)
@dp.message_handler(content_types=['text'], text='Вернуться')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('Какой вопрос вас интересует?', reply_markup=kb.fqamenu)
@dp.message_handler(content_types=['text'], text='Меню')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		await message.answer('Что вам нужно?', reply_markup=kb.fqa)
def fqa():
	@dp.message_handler(content_types=['text'])
	@dp.throttled(func.antiflood, rate=3)
	async def h(message: types.Message, state: FSMContext):
		func.join(chat_id=message.chat.id)
		q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
		result = q.fetchone()
		if result[0] == 0:
			if message.chat.id == admin or message.chat.id == admin1:
				pass
			else:
				await message.answer('Сообщение отправлено.', reply_markup=kb.fqa)
				await bot.send_message(admin, f"<b>Получен новый вопрос!</b>\n<b>От:</b> {message.from_user.mention}\nID: {message.chat.id}\n<b>Сообщение:</b> {message.text}", reply_markup=kb.fun(message.chat.id), parse_mode='HTML')
		else:
			await message.answer('Ваш аккаунт заблокирован в данном боте.', reply_markup=kb.fqa)


@dp.callback_query_handler(lambda call: True) # Inline часть
async def cal(call, state: FSMContext):
	if 'ans' in call.data:
		a = call.data.index('-ans')
		ids = call.data[:a]
		await call.message.answer('Введите ответ пользователю:', reply_markup=kb.back)
		await st.item2.set() # админ отвечает пользователю
		await state.update_data(uid=ids)
	elif 'ignor' in call.data:
		await call.answer('Удалено')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await state.finish()

@dp.message_handler(state=st.item2)
async def proc(message: types.Message, state: FSMContext):
	if message.text == 'Отмена':
		await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.menu)
		await state.finish()
	else:
		await message.answer('Сообщение отправлено.', reply_markup=kb.menu)
		data = await state.get_data()
		id = data.get("uid")
		await state.finish()
		await bot.send_message(id, 'Вам поступил ответ:\n\nТекст: {}'.format(message.text))

@dp.message_handler(state=st.item)
async def process_name(message: types.Message, state: FSMContext):
	q.execute(f'SELECT user_id FROM users')
	row = q.fetchall()
	connection.commit()
	text = message.text
	if message.text == 'Отмена':
		await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.adm)
		await state.finish()
	else:
		info = row
		await message.answer('Рассылка начата!', reply_markup=kb.adm)
		for i in range(len(info)):
			try:
				await bot.send_message(info[i][0], str(text))
			except:
				pass
		await message.answer('Рассылка завершена!', reply_markup=kb.adm)
		await state.finish()


@dp.message_handler(state=st.item3)
async def proce(message: types.Message, state: FSMContext):
	if message.text == 'Отмена':
		await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.adm)
		await state.finish()
	else:
		if message.text.isdigit():
			q.execute(f"SELECT block FROM users WHERE user_id = {message.text}")
			result = q.fetchall()
			connection.commit()
			if len(result) == 0:
				await message.answer('Такой пользователь не найден в базе данных.', reply_markup=kb.adm)
				await state.finish()
			else:
				a = result[0]
				id = a[0]
				if id == 0:
					q.execute(f"UPDATE users SET block = 1 WHERE user_id = {message.text}")
					connection.commit()
					await message.answer('Пользователь успешно заблокирован.', reply_markup=kb.adm)
					await state.finish()
					await bot.send_message(message.text, 'Вы были заблокированы администрацией.')
				else:
					await message.answer('Данный пользователь уже имеет блокировку.', reply_markup=kb.adm)
					await state.finish()
		else:
			await message.answer('Ты вводишь буквы...\nВведи ID')

@dp.message_handler(state=st.item4)
async def proc(message: types.Message, state: FSMContext):
	if message.text == 'Отмена':
		await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.adm)
		await state.finish()
	else:
		if message.text.isdigit():
			q.execute(f"SELECT block FROM users WHERE user_id = {message.text}")
			result = q.fetchall()
			connection.commit()
			if len(result) == 0:
				await message.answer('Такой пользователь не найден в базе данных.', reply_markup=kb.adm)
				await state.finish()
			else:
				a = result[0]
				id = a[0]
				if id == 1:
					q.execute(f"UPDATE users SET block = 0 WHERE user_id = {message.text}")
					connection.commit()
					await message.answer('Пользователь успешно разбанен.', reply_markup=kb.adm)
					await state.finish()
					await bot.send_message(message.text, 'Вы были разблокированы администрацией.')
				else:
					await message.answer('Данный пользователь не заблокирован.', reply_markup=kb.adm)
					await state.finish()
		else:
			await message.answer('Ты вводишь буквы...\nВведи ID')
@dp.message_handler(content_types=['text'], text='Пользователи')
async def hfandler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id != admin or message.chat.id != admin1:
			await message.answer('Введите id пользователя, которого нужно разблокировать.\nДля отмены нажмите кнопку ниже', reply_markup=kb.back)
			await st.item4.set()

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
