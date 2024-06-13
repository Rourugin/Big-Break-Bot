import os
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F, Router, Bot
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv

import app.keyboards as kb
import app.states as st
import app.database.requests as rq


load_dotenv()
router = Router()
bot = Bot(token=os.getenv('TOKEN'))


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await bot.send_message(chat_id=os.getenv('ADMIN_ID'), text=f'бот был запущен {message.from_user.username}')
    await rq.set_user(message.from_user.id)
    await bot.send_sticker(message.from_user.id, sticker="CAACAgQAAxkBAAEMPJ9mXMO9h75Yd1Ax5JUJndL6Bpta8wAC9AIAAtkjZCGmdye4daM15DUE")
    await message.answer(f'{message.from_user.first_name}, приветствую тебя в боте Вдохновителей! 👋 \n\n\nЗдесь ты можешь поиграть в увлекательные игры, найти лекции и меоприятия по интересам, а также познакомиться со множеством удивительных и приятных личностей!\n\nА если у тебя возникут вопросы, просто воспользуйся командой "помощь" без кавычек \n\nТакже не забудь подписаться на наш телеграм-канал(@vdoh_vdoh)😏\n\nНадеюсь, тебе понравиться у нас!')
    await message.answer('Очень приятно! А теперь давай приступим к самому интересному😋 \n\nЧем хочешь заняться?', reply_markup=None)


@router.message(F.text.lower() == 'помощь')
async def cmd_help(message: Message) -> None:
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEMQCZmYg6ZypS6fNceSw943gOWu0mLjQACeg0AAsCf8Ev-fdx9cnSwwTUE')
    await message.answer('Судя по всему у тебя произошли какие-то технические шоколадки🍫\n\nНадеюсь здесь ты найдёшь ответ на свой вопрос, а если нет или ты нашёл(-шла) какой-то баг, то обратись к нам лично @Rouruginn к твоим услугам\n\n\nТакже не забывай про быстрые команды, они намного урощают жизнь😸\nМеню\nопросы\nМагазин или магаз\nИгра\nНастройки\nпомощь(хотя эту ты наверняка уже знаешь🙈\n\nКстати, неважно как ты напишешь команду, бот всё равно тебя поймёт (даже если написать "нАсТрОйКи"))', reply_markup=None)


@router.message(F.text.lower() == 'меню')
async def cmd_menu(message: Message) -> None:
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEMSPhmZ1aJsFbV9q4bkHN4Cfs1-wQO7gACIwEAAladvQo3E4Jzu18GwjUE')
    await message.answer('Ого, неожидал тебя здесь увидеть, в любом случае отсюда ты можешь отправиться в любую точку бота!', reply_markup=None)


@router.message(Command(commands='game') or F.text.lower() == 'игра')
async def cmd_game(message: Message, state: FSMContext) -> None:
    await state.set_state(st.cityRegistr.name)
    await bot.send_sticker('CAACAgIAAxkBAAEMSlFmaJcqGGJYwLxKTiyBS7VARc30HwACmgAD9wLID9HVBvL9etQ4NQQ')
    await message.answer('Добро пожаловать, в эту... в этот... в этот пока что лес, но я уверен, что ты сможешь превратить его в чудесный мегаполис!')
    await message.answer('А что нужно каждому начинающему городу? \n\nПравльно! Название, с него и начнём. Придумай название ссвоему городу!', reply_markup=None)


@router.message(st.cityRegistr.name)
async def game_cityname(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.clear()
    await message.answer('Отлично! \n\nА теперь давай поставим твой первый дом! Для этого выбери раздел "Строительство", а в нём "Здания" и нажмите построить, первый дом за мой счёт!', reply_markup=kb.gameMain)


@router.message(F.text.lower() == 'информация')
async def info_game(message: Message) -> None:
    await message.answer('Здесь пока ничего нет, вернитесь, пожалуйста, к обучению')


@router.message(F.text.lower() == 'строительство')
async def construction(message: Message) -> None:
    await message.answer('Здесь ты можешь выбрать, что хочешь строить, дело за тобой)', reply_markup=kb.gameConstruction)


@router.message(F.text.lower() == 'парки')
async def parks(message: Message) -> None:
    await message.answer('Здесь пока ничего нет, вернитесь к обучению')


@router.message(F.text.lower() == 'здания')
async def buildings(message: Message) -> None:
    await message.answer('Отлично, а теперь нажми "Построить" и возведи своё первое здание!', reply_markup=kb.build)


@router.callback_query(F.data == 'build')
async def build_frst_house(callback: CallbackQuery) -> None:
    await callback.answer(None)
    await callback.message.answer('Отлично, вот и твоё первое здание! Дальше тебя ждёт самостоятельный путь, Удачи!')
    await callback.message.answer('Инструктаж окончен. К сожалению остальная часть игры недоступна😭', reply_markup=None)


@router.message(Command(commands='timetable') or F.text.lower() == 'расписание')
async def cmd_checklist(message: Message) -> None:
    await message.answer(text='📝Расписание\n\n\nЗдесь ты можешь выбрать интересные тебе события и записать их в своё расписание.', reply_markup=kb.timetable)


@router.callback_query(F.data == 'changeTimetable')
async def changeTimetable(callback: CallbackQuery) -> None:
    await callback.answer(None)
    await callback.message.answer(text='К сожалению это пока что невозможно😰 \nПопробуйте вернуться в меню', reply_markup=None)


@router.message(Command(commands='settings') or F.text.lower() == 'настройки')
async def cmd_settings(message: Message) -> None:
    await message.answer('⚙Настройки\n\n\nЗдесь так пусто...', reply_markup=None)


@router.message(Command(commands='shop') or F.text.lower() == 'магазин' or F.text.lower() == 'магаз')
async def cmd_shop(message: Message) -> None:
    await message.answer('Здесь ты можешь обменять свои вдохновляшки на мерч Вдохновителей\n\n\nСеучас у тебя 0 вдохновляшек', reply_markup=kb.shopSelect)


@router.callback_query(F.data == 'menu')
async def callback_menu(callback: CallbackQuery) -> None:
    await callback.answer(None)
    await bot.send_sticker(callback.message.from_user.id, sticker='CAACAgIAAxkBAAEMSPhmZ1aJsFbV9q4bkHN4Cfs1-wQO7gACIwEAAladvQo3E4Jzu18GwjUE')
    await callback.message.answer('Ого, неожидал тебя здесь увидеть, в любом случае отсюда ты можешь отправиться в любую точку бота!', reply_markup=None)


@router.callback_query(F.data == 'anklet')
async def callback_anklet(callback: CallbackQuery) -> None:
    await callback.answer(None)
    await callback.message.answer(text='Браслет Вдохновителей\n\n\nОписание: Крутой браслет от Влохновителей😎\n\n\nСтоимость: 20 вдохновляшек', reply_markup=kb.buySmth)


@router.callback_query(F.data == 'hoodie')
async def callback_hoodie(callback: CallbackQuery) -> None:
    await callback.answer(None)
    await callback.message.answer(text='Худи Вдохновителей\n\n\nОписание: худи, в котором всешда будет тепло и уютно🔥\n\n\nСтоимость: 40 вдохновляшек', reply_markup=kb.buySmth)


@router.callback_query(F.data == 'termocup')
async def callback_termocup(callback: CallbackQuery) -> None:
    await callback.answer(None)
    await callback.message.answer(text='Термокружка Вдохновителей\n\n\nОписание: кружка для небольших прогулок с газировкой и долгих путешествий с горячим чаем\n\n\nСтоимость: 30 вдохновляшек', reply_markup=kb.buySmth)


@router.callback_query(F.data == 'comeBack')
async def callback_comeBack(callback: CallbackQuery) -> None:
    await callback.answer(None)
    await callback.message.answer(text='Здесь ты можешь обменять свои вдохновляшки на мерч Вдохновителей\n\n\nСеучас у тебя 0 вдохновляшек', reply_markup=kb.shopSelect)


@router.callback_query(F.data == 'buy')
async def callback_buy(callback: CallbackQuery) -> None:
    await callback.answer(None)
    await callback.message.answer(text='К сожалению это пока что невозможно😭', reply_markup=None)


@router.message(Command(commands='surveys') or F.text.lower() == 'опросы')
async def surveys(message: Message) -> None:
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEMPXxmXhN1QD1q2CkuV8fsjn0vLf-2bAACRQADWbv8JfvUpDThE_jrNQQ')
    await message.answer('У нас есть несколько опросов для тебя \n\nС чего хочешь начать?\n\n1)Всё обо мне\n2)Наш бот', reply_markup=kb.surveys)


@router.callback_query(F.data == 'aboutBot')
async def aboutBot(callback: CallbackQuery) -> None:
    await callback.answer(None)
    await callback.message.answer(text='Твоё мнение очень поможет нам в развитии бота! Спасибо ❤️\nДавай начнём!', reply_markup=kb.letsStartAB)


@router.message(F.text.lower() == 'поехали!')
async def firstAB(message: Message, state: FSMContext) -> None:
    await state.set_state(st.aboutBotSurvey.howLong)
    await message.answer('Ииииииии...\nПервый вопрос:\nКак давно ты пользуешься ботом?\n1 - Менее месяца\n2 - 1-3 месяца\n3 - 4-6 месяцев\n4 - 6-12 месяцев\n5 - Более 1 года\n\nПросьба ответить одной из этих цифр😜', reply_markup=None)


@router.message(st.aboutBotSurvey.howLong)
async def secondAB(message: Message, state: FSMContext) -> None:
    await state.update_data(howLong=message.text)
    await state.set_state(st.aboutBotSurvey.douLike)
    await message.answer('Второй вопрос капельку посложнее🙈\nНасколько тебе нравится взаимодействовать с этим ботом?\n\n1 - Не нравится вообще\n2 - В основном не нравится\n3 - Удовлетворяет\n4 - Нравится\n5 - Очень навится\n\nНа этот вопрос также попросим ответить числом😉')


@router.message(st.aboutBotSurvey.douLike)
async def thirdAB(message: Message, state: FSMContext) -> None:
    await state.update_data(douLike=message.text)
    await state.set_state(st.aboutBotSurvey.dontLike)
    await message.answer('А для третьего вопросика придётся немного пописать✍\nПодуай, что тебе НЕ нравится в взаимодействии с ботом сейчас?')


@router.message(st.aboutBotSurvey.dontLike)
async def fourthAB(message: Message, state: FSMContext) -> None:
    await state.update_data(dontLike=message.text)
    await state.set_state(st.aboutBotSurvey.comment)
    await message.answer('Пришло время для последнего вопроса! Однако тут тоже придётся напрячь ручки. Напиши своё мнение о боте, что ты хотел(-а) бы увидить в нём, расскажи обо всём.')

@router.message(st.aboutBotSurvey.comment)
async def thxAB(message: Message, state: FSMContext) -> None:
    await state.update_data(comment=message.text)
    await state.clear()
    await message.answer('Спасибо за прохождения опроса! Мы тебе очень благодарны💘\nТеперь ты можешь вернуться в главное меню, нажав кнопку или написав "меню" (без кавычек)', reply_markup=None)


@router.callback_query(F.data == 'allAboutMe')
async def startAAM(callback: CallbackQuery) -> None:
    await callback.answer(None)
    await callback.message.answer('Ты готов к этому опросу? Надеюсь, что да, однако рекомендую выделить на этот опрос побольше времени, ведь  он не самый короткий!', reply_markup=kb.letsStartAAM)


@router.message(F.text.lower() == 'Погнали!')
async def frst_q(message: Message, state: FSMContext) -> None:
    await state.set_state(st.allAboutMeSurvey.frst_ans)
    await message.answer('Сколько тебе лет?', reply_markup=None)


@router.message(st.allAboutMeSurvey.frst_ans)
async def scnd_q(message: Message, state: FSMContext) -> None:
    await state.update_data(frst_ans=message.text)
    await state.set_state(st.allAboutMeSurvey.scnd_ans)
    await message.answer('Какой у теюя любимый фильм?')


@router.message(st.allAboutMeSurvey.thrd_ans)
async def thrd_q(message: Message, state: FSMContext) -> None:
    await state.update_data(scnd_ans=message.text)
    await state.set_state(st.allAboutMeSurvey.thrd_ans)
    await message.answer('Какой(-ие) у тебя любимый(-ые) предмет(-ы) в школе?')


@router.message(st.allAboutMeSurvey.thrd_ans)
async def frth_q(message: Message, state: FSMContext) -> None:
    await state.update_data(thrd_ans=message.text)
    await state.set_state(st.allAboutMeSurvey.frth_ans)
    await message.answer('Любишь ли ты настольные игры/игры на свежем воздухе, если да, то какие?')


@router.message(st.allAboutMeSurvey.frth_ans)
async def ffth_q(message: Message, state: FSMContext) -> None:
    await state.update_data(frth_ans=message.text)
    await state.set_state(st.allAboutMeSurvey.ffth_ans)
    await message.answer('Ты играешь на каком-нибудь музыкальном инструменте? Если да, то на каком. Если нет, то на каком ты бы хотел(-а) научиться играть?')


@router.message(st.allAboutMeSurvey.ffth_ans)
async def sxth_q(message: Message, state: FSMContext) -> None:
    await state.update_data(ffth_ans=message.text)
    await state.set_state(st.allAboutMeSurvey.sxth_ans)
    await message.answer('Какая твоя любимая книга?')


@router.message(st.allAboutMeSurvey.sxth_ans)
async def svnth_q(message: Message, state: FSMContext) -> None:
    await state.update_data(sxth_ans=message.text)
    await state.set_state(st.allAboutMeSurvey.svth_ans)
    await message.answer('Что ты считаешь успешным обучением?')


@router.message(st.allAboutMeSurvey.svth_ans)
async def eghth_q(message: Message, state: FSMContext) -> None:
    await state.update_data(svnth_ans=message.text)
    await state.set_state(st.allAboutMeSurvey.ghth_ans)
    await message.answer('Если бы вы с друзьями ставили концерт, кем бы ты хотел(-а) бы быть?')


@router.message(st.allAboutMeSurvey.ghth_ans)
async def nnth_q(message: Message, state: FSMContext) -> None:
    await state.update_data(ghth_ans=message.text)
    await state.set_state(st.allAboutMeSurvey.nnth_ans)
    await message.answer('Кем ты себя считаешь в компании своих друзей?')


@router.message(st.allAboutMeSurvey.nnth_ans)
async def tnth_q(message: Message, state: FSMContext) -> None:
    await state.update_data(nnth_ans=message.text)
    await state.clear()
    await message.answer('Огромное спасибо за прохождения опроса, благодаря этому рекомендации улучшаться, и ты будешь получать более качественный контент!')