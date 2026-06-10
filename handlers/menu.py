from aiogram import Router
from aiogram.types import CallbackQuery, FSInputFile
from keyboards.inline_kb import menu_inline, back_inline
from keyboards import inline_kb as kb


router = Router()


@router.callback_query(lambda c: c.data == "material")
@router.callback_query(lambda c: c.data == "back")
async def material(callback: CallbackQuery):
  await callback.message.delete()
  await callback.message.answer(
    '<b>Select a topic of your interest below:</b>',
    parse_mode='HTML', reply_markup=menu_inline()
  )
  await callback.answer()

@router.callback_query(lambda c: c.data == "check_sub_again")
async def check_subscription_button(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
      "☺️ <b>Thank you for subscribing!</b>\nThanks to your support, our bot remains free."
      "\nPlease press the /start command again.", parse_mode='HTML'
    )
    await callback.answer() 


@router.callback_query(kb.CategoryClick.filter())
async def show_material(callback: CallbackQuery, callback_data: kb.CategoryClick):
  materials = {
        "cold": ("files/cold_plunges.pdf", "🧊 <b>Cold Plunges & Deliberate Cooling Protocols</b>\n\nHere is your guide!"),
        "fitness": ("files/fitness.pdf", "🏋️ <b>Fitness & Workout Routines</b>\n\nHere is your guide!"),
        "light": ("files/lab_light.pdf", "☀️ <b>Light Exposure & Circadian Rhythm</b>\n\nHere is your guide!"),
        "neuro": ("files/neuroplasticity.pdf", "🧠 <b>The Brain and Neuroplasticity</b>\n\nHere is your guide!"),
        "sleep": ("files/sleep.pdf", "🌙 <b>Sleep Hygiene Protocols</b>\n\nHere is your guide!"),
        "supps": ("files/supplementation.pdf", "💊 <b>Supplementation Guide</b>\n\nHere is your guide!")
    }
  
  topic = callback_data.topic_id
  if topic in materials:
        file_path, caption = materials[topic]
  else:
        file_path, caption = "files/fitness.pdf", "Here!"
  
 
  file = FSInputFile(file_path)

  await callback.message.delete()
  await callback.message.answer_document(
    file, caption=caption,
    parse_mode= 'HTML',
    reply_markup=back_inline()
  )
  await callback.answer()



