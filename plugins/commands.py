#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('𝗞𝗠𝗧𝗭 𝗖𝗛𝗔𝗡𝗡𝗘𝗟', url='https://t.me/kmtz_channel_v3'),
        InlineKeyboardButton('🔞𝗔𝗗𝗠𝗜𝗡🔞', url='https://t.me/KL_2335')
    ],[
        InlineKeyboardButton('𝗞𝗠𝗧𝗭 𝗚𝗥𝗢𝗨𝗣 ☠️', url='https://t.me/kmtz_v4')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.START_TXT.format(
                message.from_user.first_name),
        parse_mode="html")

@Client.on_message(filters.private & filters.command(['help']))
async def help(client, message):
    buttons = [[
        InlineKeyboardButton('close 🔐', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.HELP_TXT,
        parse_mode="html")

@Client.on_message(filters.private & filters.command(['about']))
async def about(client, message):
    buttons = [[
        InlineKeyboardButton('𝗞𝗠𝗧𝗭 𝗚𝗥𝗢𝗨𝗣 ☠️', url='https://t.me/kmtz_v4'),
        InlineKeyboardButton('close 🔐', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        parse_mode="html"
    )

        
