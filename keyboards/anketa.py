from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
kb_apteka_cancel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel_anketa')]])
kb_apteka_cancel_and_back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='back_anketa'),
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel_anketa'),]])
kb_apteka_by_gender = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='back_anketa'),
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel_anketa'),
    ],[
        InlineKeyboardButton(
            text='CS2',
            callback_data='game_cs2'),
        InlineKeyboardButton(
            text='Valorant',
            callback_data='game_Valorant'),
        InlineKeyboardButton(
            text='DOTA2',
            callback_data='game_dota2'
        )]])