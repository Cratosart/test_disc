from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from states import NaturalPerson

@dp.callback_query_handler(state='discount')
async def set_date_from_buttons (
    call:types.CallbackQuery,
    state:FSMContext
):
    await call.answer()
    await call.message.delete()

    message_data = await call.message.answer('Введите промокод')
    await state.update_data(message_to_delete=message_data.message_id)

    await NaturalPerson.discount.set()



