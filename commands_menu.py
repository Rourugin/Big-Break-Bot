from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='surveys',
            description='Список опросов'
        ),
        BotCommand(
            command='game',
            description='Игра'
        ),
        BotCommand(
            command='timetable',
            description='Составить расписание'
        ),
        BotCommand(
            command='shop',
            description='Магазин'
        ),
        BotCommand(
            command='settings',
            description='Настройки'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())