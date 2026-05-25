# ============================================================
#  GUNGNIR — Recruitment Bot (InlineKeyboard version)
#  python-telegram-bot v20+
#  pip install python-telegram-bot
# ============================================================

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, CallbackQueryHandler,
    ConversationHandler, filters, ContextTypes
)

TOKEN   = "8916685212:AAGygsqJka323jWBa8iMNDWrLOYuXDbiU5E"
CHAT_ID = -1003918420875  # GUNGNIR | Анкети

logging.basicConfig(level=logging.INFO)

# ===== Кроки =====
(
    NAME, AGE, CITY, PHONE, MESSENGER, RELOCATION,
    MIL_SERVICE, MIL_COMBAT, MIL_UNITS, MIL_VOS, UAV_EXP,
    HEALTH, WARZONE, SZCh, BAD_HABITS, STRESS,
    EDUCATION, PROFESSION, SKILLS,
    MOTIVATION, STRENGTHS, ROLE, SERVICE_MEANING,
    DRIVER_LIC, OWN_CAR, PASSPORT, INTERVIEW,
    UAV_TYPES, SOLDERING, HEAVY_BOMBERS, NIGHT_FLIGHTS, SOFTWARE, UAV_THEORY,
    CONFIRM
) = range(34)

def yn():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("✅ Так", callback_data="Так"),
        InlineKeyboardButton("❌ Ні",  callback_data="Ні")
    ]])

def stress_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(1, 6)],
        [InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(6, 11)],
    ])

def skills_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💻 ІТ",          callback_data="ІТ"),
         InlineKeyboardButton("⚡ Електроніка", callback_data="Електроніка")],
        [InlineKeyboardButton("🚗 Водіння",     callback_data="Водіння"),
         InlineKeyboardButton("⚙️ Інженерія",   callback_data="Інженерія")],
        [InlineKeyboardButton("📝 Інше / Немає", callback_data="Інше")],
    ])

def confirm_kb():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("✅ Надіслати", callback_data="SEND"),
        InlineKeyboardButton("❌ Скасувати", callback_data="CANCEL")
    ]])

# ===== /start =====
async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.clear()
    await update.message.reply_text(
        "👋 Вітаємо у системі відбору *GUNGNIR*\n\n"
        "Підрозділ важких ударних безпілотних бомберів.\n\n"
        "Анкета складається з 7 блоків і займе ~5 хвилин.\n"
        "Відповідай чесно — це в твоїх інтересах.\n\n"
        "✏️ Введи своє *Прізвище, ім'я та по батькові:*",
        parse_mode="Markdown"
    )
    return NAME

# ===== Блок 1 — Загальне =====
async def get_name(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["name"] = update.message.text
    await update.message.reply_text("✏️ Вік:")
    return AGE

async def get_age(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["age"] = update.message.text
    await update.message.reply_text("✏️ Місто проживання:")
    return CITY

async def get_city(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["city"] = update.message.text
    await update.message.reply_text("✏️ Контактний номер телефону:")
    return PHONE

async def get_phone(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["phone"] = update.message.text
    await update.message.reply_text("✏️ Telegram або Signal (username або номер):")
    return MESSENGER

async def get_messenger(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["messenger"] = update.message.text
    await update.message.reply_text(
        "Чи готові до переїзду або відряджень?",
        reply_markup=yn()
    )
    return RELOCATION

async def get_relocation(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["relocation"] = q.data
    await q.edit_message_text(f"Переїзд/відрядження: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text(
        "─────────────────\n*Блок 2 — Військовий досвід*\n─────────────────\n\n"
        "Чи проходили військову службу?",
        parse_mode="Markdown",
        reply_markup=yn()
    )
    return MIL_SERVICE

# ===== Блок 2 — Військовий досвід =====
async def get_mil_service(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["mil_service"] = q.data
    await q.edit_message_text(f"Військова служба: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text("Чи маєте бойовий досвід?", reply_markup=yn())
    return MIL_COMBAT

async def get_mil_combat(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["mil_combat"] = q.data
    await q.edit_message_text(f"Бойовий досвід: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text("✏️ У яких підрозділах служили? (або напиши 'Не служив')")
    return MIL_UNITS

async def get_mil_units(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["mil_units"] = update.message.text
    await update.message.reply_text("✏️ Ваша військова спеціальність / ВОС (або 'Немає'):")
    return MIL_VOS

async def get_mil_vos(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["mil_vos"] = update.message.text
    await update.message.reply_text("Чи є досвід роботи з БПЛА?", reply_markup=yn())
    return UAV_EXP

async def get_uav_exp(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["uav_exp"] = q.data
    await q.edit_message_text(f"Досвід БПЛА: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text(
        "─────────────────\n*Блок 3 — Фізична та психологічна готовність*\n─────────────────\n\n"
        "Чи маєте обмеження по здоров'ю?",
        parse_mode="Markdown",
        reply_markup=yn()
    )
    return HEALTH

# ===== Блок 3 — Здоров'я =====
async def get_health(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["health"] = q.data
    await q.edit_message_text(f"Обмеження здоров'я: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text("Чи готові працювати в зоні бойових дій?", reply_markup=yn())
    return WARZONE

async def get_warzone(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["warzone"] = q.data
    await q.edit_message_text(f"Готовність до ЗБЗ: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text("Чи перебуваєте зараз на службі у ЗСУ (СЗЧ)?", reply_markup=yn())
    return SZCh

async def get_szch(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["szch"] = q.data
    await q.edit_message_text(f"На службі (СЗЧ): *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text("Чи маєте шкідливі звички?", reply_markup=yn())
    return BAD_HABITS

async def get_bad_habits(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["bad_habits"] = q.data
    await q.edit_message_text(f"Шкідливі звички: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text(
        "Як оцінюєте свою стресостійкість від 1 до 10?",
        reply_markup=stress_kb()
    )
    return STRESS

async def get_stress(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["stress"] = q.data
    await q.edit_message_text(f"Стресостійкість: *{q.data}/10*", parse_mode="Markdown")
    await q.message.reply_text(
        "─────────────────\n*Блок 4 — Цивільні навички*\n─────────────────\n\n"
        "✏️ Освіта (школа / технікум / вища / інше):",
        parse_mode="Markdown"
    )
    return EDUCATION

# ===== Блок 4 — Цивільні навички =====
async def get_education(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["education"] = update.message.text
    await update.message.reply_text("✏️ Основна цивільна професія:")
    return PROFESSION

async def get_profession(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["profession"] = update.message.text
    await update.message.reply_text(
        "Навички корисні підрозділу:",
        reply_markup=skills_kb()
    )
    return SKILLS

async def get_skills(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["skills"] = q.data
    await q.edit_message_text(f"Навички: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text(
        "─────────────────\n*Блок 5 — Мотивація*\n─────────────────\n\n"
        "✏️ Чому хочете приєднатись саме до GUNGNIR?",
        parse_mode="Markdown"
    )
    return MOTIVATION

# ===== Блок 5 — Мотивація =====
async def get_motivation(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["motivation"] = update.message.text
    await update.message.reply_text("✏️ Ваші сильні сторони:")
    return STRENGTHS

async def get_strengths(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["strengths"] = update.message.text
    await update.message.reply_text("✏️ Яку роль бачите для себе у підрозділі?")
    return ROLE

async def get_role(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["role"] = update.message.text
    await update.message.reply_text("✏️ Що для вас означає служба?")
    return SERVICE_MEANING

async def get_service_meaning(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["service_meaning"] = update.message.text
    await update.message.reply_text(
        "─────────────────\n*Блок 6 — Додатково*\n─────────────────\n\n"
        "✏️ Водійське посвідчення — які категорії? (або 'Немає')",
        parse_mode="Markdown"
    )
    return DRIVER_LIC

# ===== Блок 6 — Додатково =====
async def get_driver_lic(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["driver_lic"] = update.message.text
    await update.message.reply_text("Чи є власне авто?", reply_markup=yn())
    return OWN_CAR

async def get_own_car(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["own_car"] = q.data
    await q.edit_message_text(f"Власне авто: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text("Чи є закордонний паспорт?", reply_markup=yn())
    return PASSPORT

async def get_passport(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["passport"] = q.data
    await q.edit_message_text(f"Закордонний паспорт: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text("Чи готові пройти співбесіду та перевірку?", reply_markup=yn())
    return INTERVIEW

async def get_interview(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["interview"] = q.data
    await q.edit_message_text(f"Співбесіда та перевірка: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text(
        "─────────────────\n*Блок 7 — Спеціалізація БПЛА*\n─────────────────\n\n"
        "✏️ З якими типами дронів працювали? (або 'Не працював')",
        parse_mode="Markdown"
    )
    return UAV_TYPES

# ===== Блок 7 — БПЛА =====
async def get_uav_types(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["uav_types"] = update.message.text
    await update.message.reply_text("Чи маєте досвід пайки / ремонту електроніки?", reply_markup=yn())
    return SOLDERING

async def get_soldering(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["soldering"] = q.data
    await q.edit_message_text(f"Пайка/ремонт: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text("Чи працювали з важкими бомберами?", reply_markup=yn())
    return HEAVY_BOMBERS

async def get_heavy_bombers(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["heavy_bombers"] = q.data
    await q.edit_message_text(f"Важкі бомбери: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text("Чи маєте досвід нічних польотів?", reply_markup=yn())
    return NIGHT_FLIGHTS

async def get_night_flights(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["night_flights"] = q.data
    await q.edit_message_text(f"Нічні польоти: *{q.data}*", parse_mode="Markdown")
    await q.message.reply_text("✏️ Які програми або софт використовували? (або 'Не використовував')")
    return SOFTWARE

async def get_software(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["software"] = update.message.text
    await update.message.reply_text("Чи розумієте принципи роботи БПЛА?", reply_markup=yn())
    return UAV_THEORY

async def get_uav_theory(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    ctx.user_data["uav_theory"] = q.data
    await q.edit_message_text(f"Теорія БПЛА: *{q.data}*", parse_mode="Markdown")
    d = ctx.user_data
    preview = (
        f"─────────────────\n"
        f"📋 *Перевір свою анкету*\n"
        f"─────────────────\n\n"
        f"👤 *{d.get('name')}*\n"
        f"Вік: {d.get('age')} | Місто: {d.get('city')}\n"
        f"Телефон: {d.get('phone')} | {d.get('messenger')}\n"
        f"Переїзд: {d.get('relocation')}\n\n"
        f"🪖 Служба: {d.get('mil_service')} | Бойовий досвід: {d.get('mil_combat')}\n"
        f"Підрозділи: {d.get('mil_units')} | ВОС: {d.get('mil_vos')}\n"
        f"Досвід БПЛА: {d.get('uav_exp')}\n\n"
        f"❤️ Здоров'я: {d.get('health')} | ЗБЗ: {d.get('warzone')}\n"
        f"СЗЧ: {d.get('szch')} | Шкідливі звички: {d.get('bad_habits')} | Стрес: {d.get('stress')}/10\n\n"
        f"🎓 Освіта: {d.get('education')} | Професія: {d.get('profession')}\n"
        f"Навички: {d.get('skills')}\n\n"
        f"💬 Мотивація: {d.get('motivation')[:80]}...\n\n"
        f"🚗 Права: {d.get('driver_lic')} | Авто: {d.get('own_car')} | Закордонний: {d.get('passport')}\n\n"
        f"🚁 Дрони: {d.get('uav_types')}\n"
        f"Пайка: {d.get('soldering')} | Бомбери: {d.get('heavy_bombers')} | Ніч: {d.get('night_flights')}\n"
        f"Софт: {d.get('software')} | Теорія: {d.get('uav_theory')}\n\n"
        f"─────────────────\nНадіслати анкету?"
    )
    await q.message.reply_text(preview, parse_mode="Markdown", reply_markup=confirm_kb())
    return CONFIRM

# ===== Підтвердження =====
async def confirm(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "SEND":
        d = ctx.user_data
        u = q.from_user
        card = (
            f"🟡 *НОВА АНКЕТА — GUNGNIR*\n"
            f"─────────────────────\n\n"
            f"👤 *{d.get('name')}*\n"
            f"Telegram: @{u.username or '—'} | ID: `{u.id}`\n\n"
            f"*1 / ЗАГАЛЬНЕ*\n"
            f"Вік: {d.get('age')}\n"
            f"Місто: {d.get('city')}\n"
            f"Телефон: {d.get('phone')}\n"
            f"Месенджер: {d.get('messenger')}\n"
            f"Переїзд/відрядження: {d.get('relocation')}\n\n"
            f"*2 / ВІЙСЬКОВИЙ ДОСВІД*\n"
            f"Служба: {d.get('mil_service')}\n"
            f"Бойовий досвід: {d.get('mil_combat')}\n"
            f"Підрозділи: {d.get('mil_units')}\n"
            f"ВОС: {d.get('mil_vos')}\n"
            f"Досвід БПЛА: {d.get('uav_exp')}\n\n"
            f"*3 / ФІЗИЧНА ТА ПСИХОЛОГІЧНА ГОТОВНІСТЬ*\n"
            f"Обмеження здоров'я: {d.get('health')}\n"
            f"Готовність до ЗБЗ: {d.get('warzone')}\n"
            f"На службі (СЗЧ): {d.get('szch')}\n"
            f"Шкідливі звички: {d.get('bad_habits')}\n"
            f"Стресостійкість: {d.get('stress')}/10\n\n"
            f"*4 / ЦИВІЛЬНІ НАВИЧКИ*\n"
            f"Освіта: {d.get('education')}\n"
            f"Професія: {d.get('profession')}\n"
            f"Навички: {d.get('skills')}\n\n"
            f"*5 / МОТИВАЦІЯ*\n"
            f"Чому GUNGNIR: {d.get('motivation')}\n"
            f"Сильні сторони: {d.get('strengths')}\n"
            f"Роль у підрозділі: {d.get('role')}\n"
            f"Служба для мене: {d.get('service_meaning')}\n\n"
            f"*6 / ДОДАТКОВО*\n"
            f"Водійські права: {d.get('driver_lic')}\n"
            f"Власне авто: {d.get('own_car')}\n"
            f"Закордонний паспорт: {d.get('passport')}\n"
            f"Готовність до співбесіди: {d.get('interview')}\n\n"
            f"*7 / БПЛА СПЕЦІАЛІЗАЦІЯ*\n"
            f"Типи дронів: {d.get('uav_types')}\n"
            f"Пайка/ремонт: {d.get('soldering')}\n"
            f"Важкі бомбери: {d.get('heavy_bombers')}\n"
            f"Нічні польоти: {d.get('night_flights')}\n"
            f"Програми/софт: {d.get('software')}\n"
            f"Теорія БПЛА: {d.get('uav_theory')}\n"
            f"─────────────────────"
        )
        await ctx.bot.send_message(chat_id=CHAT_ID, text=card, parse_mode="Markdown")
        await q.edit_message_text(
            "✅ *Анкету надіслано!*\n\n"
            "Ми розглянемо її та зв'яжемось з тобою протягом 24 годин.\n\n"
            "Слава Україні! 🇺🇦",
            parse_mode="Markdown"
        )
    else:
        await q.edit_message_text("Анкету скасовано. Напиши /start щоб почати заново.")
    ctx.user_data.clear()
    return ConversationHandler.END

async def cancel(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.clear()
    await update.message.reply_text("Анкету скасовано. Напиши /start щоб почати заново.")
    return ConversationHandler.END

def main():
    app = Application.builder().token(TOKEN).build()
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME:           [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            AGE:            [MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)],
            CITY:           [MessageHandler(filters.TEXT & ~filters.COMMAND, get_city)],
            PHONE:          [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            MESSENGER:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_messenger)],
            RELOCATION:     [CallbackQueryHandler(get_relocation)],
            MIL_SERVICE:    [CallbackQueryHandler(get_mil_service)],
            MIL_COMBAT:     [CallbackQueryHandler(get_mil_combat)],
            MIL_UNITS:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_mil_units)],
            MIL_VOS:        [MessageHandler(filters.TEXT & ~filters.COMMAND, get_mil_vos)],
            UAV_EXP:        [CallbackQueryHandler(get_uav_exp)],
            HEALTH:         [CallbackQueryHandler(get_health)],
            WARZONE:        [CallbackQueryHandler(get_warzone)],
            SZCh:           [CallbackQueryHandler(get_szch)],
            BAD_HABITS:     [CallbackQueryHandler(get_bad_habits)],
            STRESS:         [CallbackQueryHandler(get_stress)],
            EDUCATION:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_education)],
            PROFESSION:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_profession)],
            SKILLS:         [CallbackQueryHandler(get_skills)],
            MOTIVATION:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_motivation)],
            STRENGTHS:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_strengths)],
            ROLE:           [MessageHandler(filters.TEXT & ~filters.COMMAND, get_role)],
            SERVICE_MEANING:[MessageHandler(filters.TEXT & ~filters.COMMAND, get_service_meaning)],
            DRIVER_LIC:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_driver_lic)],
            OWN_CAR:        [CallbackQueryHandler(get_own_car)],
            PASSPORT:       [CallbackQueryHandler(get_passport)],
            INTERVIEW:      [CallbackQueryHandler(get_interview)],
            UAV_TYPES:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_uav_types)],
            SOLDERING:      [CallbackQueryHandler(get_soldering)],
            HEAVY_BOMBERS:  [CallbackQueryHandler(get_heavy_bombers)],
            NIGHT_FLIGHTS:  [CallbackQueryHandler(get_night_flights)],
            SOFTWARE:       [MessageHandler(filters.TEXT & ~filters.COMMAND, get_software)],
            UAV_THEORY:     [CallbackQueryHandler(get_uav_theory)],
            CONFIRM:        [CallbackQueryHandler(confirm)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True
    )
    app.add_handler(conv)
    print("Бот запущено...")
    app.run_polling()

if __name__ == "__main__":
    main()
