from aiogram import executor
from aiogram.types import Message, CallbackQuery
from config import dp
from buttonlar import start_button, cours_button, pyt_found, obuna


@dp.message_handler(commands='start')
async def start(message: Message):
    image = open('rasmlar/channels4_profile.jpg', 'rb')
    await message.answer_photo(image, caption=f'Assalomu-alaykum {message.from_user.full_name}\n'
                                              f'Prince12 O\'quv markazi botiga hush kelibsiz',
                               reply_markup=start_button)


@dp.message_handler(commands='help')
async def help(message: Message):
    await message.reply('Yordam uchun 📱+998911219015 ga murojaat qiling')


@dp.message_handler(text='Biz haqimizda')
async def about(message: Message):
    image = open('rasmlar/bizhaqimizda.jpg', 'rb')
    text = ('Bizning o\'quv markazimiz 2022-yildan buyon ish olib boradi\n'
            'Bizda IT kurslari mavjud🤑')

    await message.answer_photo(image, caption=text)


@dp.message_handler(text='Kurslar')
async def courses(message: Message):
    await message.answer('Kerakli kursni tanlang👇', reply_markup=cours_button)


@dp.message_handler(text='Foundation Python🐍')
async def python_foundation(message: Message):
    await message.answer_photo(open('rasmlar/python.jpg', 'rb'), caption='Python Foundation Kursi\n'
                         '⏰Kurs davomiyligi: 4 oy\n'
                         '🧔Ustoz: Alimardon Boqijonov\n'
                         '💲Kurs Narxi: 900.000 1 oy uchun', reply_markup=pyt_found)

@dp.callback_query_handler(text='1')
async def python(call: CallbackQuery):
    await call.message.answer('Ismingiz va telefon raqam, manzilingizni yuboring', reply_markup=obuna)
    await call.answer(cache_time=10)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
