from aiogram.fsm.state import State, StatesGroup


class aboutBotSurvey(StatesGroup):
    howLong = State()
    douLike = State()
    dontLike = State()
    comment = State()


class allAboutMeSurvey(StatesGroup):
    frst_ans = State()
    scnd_ans = State()
    thrd_ans = State()
    frth_ans = State()
    ffth_ans = State()
    sxth_ans = State()
    svth_ans = State()
    ghth_ans = State()
    nnth_ans = State()


class cityRegistr(StatesGroup):
    name = State()