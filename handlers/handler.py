from states import state
from configs.config import bot, dp
from configs.filter import CheckState
from aiogram.types import Message, ContentType
from keyboards.keyboard import get_language_manu, get_ask_manu, get_buged_manu, get_contact_manu, remove_menu

@dp.message_handler(commands=["start"])
async def start_command(msg: Message) -> None:
    s = state.State("NAME", {"SALARY": 0}, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Assalomu alekum 😊\nAkbarov's Agency bot'ga Hush kelibsiz!\n\nToliq ismingizni kiriting 👇")

@dp.message_handler(CheckState("NAME"))
async def name_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    data.update({"NAME": msg.text})
    s = state.State("MAJOR", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Biznesingiz yo'nalishini kiriting 👇")

@dp.message_handler(CheckState("MAJOR"))
async def major_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    data.update({"MAJOR": msg.text})
    s = state.State("MAIN_LANGUAGE", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Accountiz asosiy tili qaysi til?", reply_markup=get_language_manu())

@dp.message_handler(CheckState("MAIN_LANGUAGE"), lambda msg: msg.text in ["Uzbek tili", "Rus tili", "Ingliz tili"])
async def main_language_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    data.update({"MAIN_LANGUAGE": msg.text})
    s = state.State("LANGUAGE", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Accountingiz qanday tillarda yurg'izilishi kerak?", reply_markup=remove_menu)

@dp.message_handler(CheckState("LANGUAGE"))
async def language_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    data.update({"LANGUAGE": msg.text})
    s = state.State("SOCIAL_NEED", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Qaysi ijtimoiy tarmoqlar kerak?", reply_markup=remove_menu)

@dp.message_handler(CheckState("SOCIAL_NEED"))
async def social_need_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    data.update({"SOCIAL_NEED": msg.text})
    s = state.State("LENTA_POST", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Oyiga nechta rasm (post) kerak? (Lenta uchun)", reply_markup=remove_menu)

@dp.message_handler(CheckState("LENTA_POST"))
async def lenta_post_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    salary = data.get("SALARY")
    lenta_post_count = int(msg.text)
    if lenta_post_count >= 1 and lenta_post_count <= 5:
        salary += (lenta_post_count * 150000)
    elif lenta_post_count >= 6 and lenta_post_count <= 10:
        salary += (lenta_post_count * 130000)
    elif lenta_post_count >= 11 and lenta_post_count <= 20:
        salary += (lenta_post_count * 100000)
    else:
        salary += (lenta_post_count * 100000)
    
    data.update({"LENTA_POST": msg.text})
    data.update({"SALARY": salary})
    s = state.State("LENTA_MOUSHN", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Oyiga nechta 2D moushnlar kerak? (Lenta uchun)", reply_markup=remove_menu)

@dp.message_handler(CheckState("LENTA_MOUSHN"))
async def lenta_moushn_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    salary = data.get("SALARY")
    lenta_moushn_count = int(msg.text)
    if lenta_moushn_count >= 1 and lenta_moushn_count <= 3:
        salary += (lenta_moushn_count * 320000)
    elif lenta_moushn_count >= 4 and lenta_moushn_count <= 6:
        salary += (lenta_moushn_count * 270000)
    elif lenta_moushn_count >= 7 and lenta_moushn_count <= 10:
        salary += (lenta_moushn_count * 220000)
    else:
        salary += (lenta_moushn_count * 220000)
    
    data.update({"LENTA_MOUSHN": msg.text})
    data.update({"SALARY": salary})
    s = state.State("LENTA_VIDEO", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Oyiga nechta video kerak? (Lenta uchun)", reply_markup=remove_menu)

@dp.message_handler(CheckState("LENTA_VIDEO"))
async def lenta_video_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    salary = data.get("SALARY")
    lenta_video_count = int(msg.text)
    if lenta_video_count >= 1 and lenta_video_count <= 5:
        salary += (lenta_video_count * 200000)
    elif lenta_video_count >= 6 and lenta_video_count <= 10:
        salary += (lenta_video_count * 160000)
    elif lenta_video_count >= 11 and lenta_video_count <= 20:
        salary += (lenta_video_count * 120000)
    else:
        salary += (lenta_video_count * 120000)
    
    data.update({"LENTA_VIDEO": msg.text})
    data.update({"SALARY": salary})
    s = state.State("STORY_POST", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Oyiga nechta rasm (post) kerak? (Istoriya uchun)", reply_markup=remove_menu)

@dp.message_handler(CheckState("STORY_POST"))
async def story_post_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    salary = data.get("SALARY")
    story_post_count = int(msg.text)
    if story_post_count >= 1 and story_post_count <= 5:
        salary += (story_post_count * 100000)
    elif story_post_count >= 6 and story_post_count <= 10:
        salary += (story_post_count * 80000)
    elif story_post_count >= 11 and story_post_count <= 20:
        salary += (story_post_count * 50000)
    else:
        salary += (story_post_count * 50000)

    data.update({"STORY_POST": msg.text})
    data.update({"SALARY": salary})
    s = state.State("STORY_MOUSHN", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Oyiga nechta 2D moushnlar kerak? (Istoriya uchun)", reply_markup=remove_menu)

@dp.message_handler(CheckState("STORY_MOUSHN"))
async def story_moushn_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    salary = data.get("SALARY")
    story_moushn_count = int(msg.text)
    if story_moushn_count >= 1 and story_moushn_count <= 3:
        salary += (story_moushn_count * 250000)
    elif story_moushn_count >= 4 and story_moushn_count <= 6:
        salary += (story_moushn_count * 200000)
    elif story_moushn_count >= 7 and story_moushn_count <= 10:
        salary += (story_moushn_count * 150000)
    else:
        salary += (story_moushn_count * 150000)

    data.update({"STORY_MOUSHN": msg.text})
    data.update({"SALARY": salary})
    s = state.State("STORY_VIDEO", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Oyiga nechta video kerak? (Istoriya uchun)", reply_markup=remove_menu)

@dp.message_handler(CheckState("STORY_VIDEO"))
async def story_video_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    salary = data.get("SALARY")
    story_video_count = int(msg.text)
    if story_video_count >= 1 and story_video_count <= 5:
        salary += (story_video_count * 120000)
    elif story_video_count >= 6 and story_video_count <= 10:
        salary += (story_video_count * 90000)
    elif story_video_count >= 11 and story_video_count <= 20:
        salary += (story_video_count * 60000)
    else:
        salary += (story_video_count * 60000)

    data.update({"STORY_VIDEO": msg.text})
    data.update({"SALARY": salary})
    s = state.State("TARGET_NEED", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Target hizmatlari kerakmi?", reply_markup=get_ask_manu())

@dp.message_handler(CheckState("TARGET_NEED"), lambda msg: msg.text in ["Ha", "Yo'q"])
async def target_need_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    data.update({"TARGET_NEED": msg.text})
    if msg.text == "Ha":    
        s = state.State("TARGET_BUGED", data, msg.chat.id)
        state.append(s)
        await bot.send_message(msg.chat.id, "Targrt uchun oylik budjetingiz qanaqa?", reply_markup=get_buged_manu())
    else:
        s = state.State("FACE_NEED", data, msg.chat.id)
        state.append(s)
        await bot.send_message(msg.chat.id, "Biznesingiz uchun ijtimoiy tarmoqlarda face hizmati kerakmi?", reply_markup=get_ask_manu())

@dp.message_handler(CheckState("TARGET_BUGED"), lambda msg: msg.text in ["100$ dan 500$ gacha", "500$ dan 1,000$ gacha", "1,000$ dan 2,500$ gacha"])
async def target_buged_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    salary = data.get("SALARY")
    if msg.text == "100$ dan 500$ gacha":
        salary += 1000000
    elif msg.text == "500$ dan 1,000$ gacha":
        salary += 2000000
    elif msg.text == "1,000$ dan 2,500$ gacha":
        salary += 3500000
    data.update({"TARGET_BUGED": msg.text})
    data.update({"SALARY": salary})
    s = state.State("FACE_NEED", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Biznesingiz uchun ijtimoiy tarmoqlarda face hizmati kerakmi?", reply_markup=get_ask_manu())

@dp.message_handler(CheckState("FACE_NEED"), lambda msg: msg.text in ["Ha", "Yo'q"])
async def face_need_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    salary = data.get("SALARY")
    if msg.text == "Ha":
        salary += 2000000
    data.update({"FACE_NEED": msg.text})
    data.update({"SALARY": salary})

    name = data.get("NAME")
    major = data.get("MAJOR")
    main_language = data.get("MAIN_LANGUAGE")
    language = data.get("LANGUAGE")
    social_need = data.get("SOCIAL_NEED")
    lenta_post = data.get("LENTA_POST")
    lenta_moushn = data.get("LENTA_MOUSHN")
    lenta_video = data.get("LENTA_VIDEO")
    story_post = data.get("STORY_POST")
    story_moushn = data.get("STORY_MOUSHN")
    story_video = data.get("STORY_VIDEO")
    target_need = data.get("TARGET_NEED")
    target_buged = data.get("TARGET_BUGED")
    face_need = data.get("FACE_NEED")
    salary = data.get("SALARY")
    text = f"""- To'liq ismingiz: {name}\n- Biznes yo'nalishingiz: {major}\n- Asosiy til: {main_language}\n- Qaday tillarda yuritilsin: {language}\n- Ijtiomiy tarmoqlar: {social_need}\n- Postlar soni: {lenta_post}\n- 2D moushnlar soni: {lenta_moushn}\n- Videolar soni: {lenta_video}\n Postlar soni (istoriya): {story_post}\n- 2D moushnlar soni (istoriya): {story_moushn}\n- Videolar soni (istoriya): {story_video}\n- Target hizmati: {target_need}\n- Oylik budjet (targetga): {target_buged}\n- Face hizmati: {face_need}\n\nNarxi: {salary:,.2f}so'm."""

    s = state.State("BIND_MANAGER", data, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, text, reply_markup=remove_menu)
    await bot.send_message("@baza20240818", text)
    await bot.send_message(msg.chat.id, "Sizga menejerlarimiz bog'lanib yana batafsil ma'lumot berishsinmi?", reply_markup=get_ask_manu())

@dp.message_handler(CheckState("BIND_MANAGER"), lambda msg: msg.text in ["Ha", "Yo'q"])
async def bind_manager_state(msg: Message) -> None:
    data = state.get_data(msg.chat.id)
    if msg.text == "Ha":
        s = state.State("CONTACT", data, msg.chat.id)
        state.append(s)
        await bot.send_message(msg.chat.id, "Raqamingizni yuboring va biz siz bilan bog'lanamiz 👇", reply_markup=get_contact_manu())
    else:
        s = state.State("", {"SALARY": 0}, msg.chat.id)
        state.append(s)
        await bot.send_message(msg.chat.id, "Hizmatimizdan foydalanganingiz uchun rahmat.\n\nQayta boshlash uchun /start", reply_markup=remove_menu)

@dp.message_handler(CheckState("CONTACT"), content_types=ContentType.CONTACT)
async def contact_state(msg: Message) -> None:
    s = state.State("", {"SALARY": 0}, msg.chat.id)
    state.append(s)
    await bot.send_message(msg.chat.id, "Hizmatimizdan foydalanganingiz uchun rahmat.\n\nQayta boshlash uchun /start", reply_markup=remove_menu)
    await bot.send_message("@baza20240818", f"Phone Number: {msg.contact.phone_number}.")
