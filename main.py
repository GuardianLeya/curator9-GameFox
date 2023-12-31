import telebot

bot = telebot.TeleBot('6464021667:AAHsEYLBJs6TMz-9x3G_t5t17zld8bPrpu4')

# 1
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет! Я твой персональный помощник! Чтобы узнать о моих возможностях, напиши команду /help',
                     parse_mode='Markdown')

# 2
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,
                     '*Это список доступных команд:* \n/start - Начать бота \n/info - Информация \n/sayhello - Поздороваться \n/goodbye - Попрощаться \n/motivation - Замотивировать \n*/meme - весёлые мемы*',
                     parse_mode='Markdown')

# 3
@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id,
                     '*Лучший бот на свете* — это лучший персональный помощник, созданный с целью облегчить твою жизнь и помочь тебе в самых различных задачах. Он оснащен *мощным искусственным интеллектом*, который позволяет ему понимать и адаптироваться к твоим потребностям. Благодаря своей надежности и универсальности, этот бот стал незаменимым союзником в твоём ежедневном рутинном распорядке. Он помогает тебе вести учет твоих дел, отслеживать важные события и напоминать о встречах и важных задачах. Бот также обладает навыками языка и может оказать помощь в поиске ответов на вопросы, предоставляя информацию из различных источников в режиме реального времени. Весь процесс взаимодействия с ним очень интуитивный и удобный, даже приложений нет необходимости скачивать. Бот является твоим *верным соратником*, который всегда находится рядом и готов помочь в любое время дня и ночи.',
                     parse_mode='Markdown')

# 4
@bot.message_handler(commands=['sayhello'])
def main(message):
    bot.send_message(message.chat.id, 'Привет)', parse_mode='Markdown')

# 5
@bot.message_handler(commands=['goodbye'])
def main(message):
    bot.send_message(message.chat.id, 'Увидимся) Удачи!', parse_mode='Markdown')

# 6
@bot.message_handler(commands=['motivation'])
def main(message):
    bot.send_message(message.chat.id,
                     'Не всегда в жизни все идет гладко, переживая сложности и невзгоды, мы иногда теряем весь энтузиазм и веру в свои силы. Но даже в трудные моменты стоит помнить, что каждая преграда — это лишь _новый_ вызов, который поможет нам стать сильнее и увереннее в себе. Страстно притягивай мечты, повышай планку своих целей и не останавливайся на достигнутом. Временами мотивация может покинуть тебя, но помни, что *огонь* внутри тебя никогда не должен погаснуть. Поставь перед собой ясные и амбициозные цели, иди вперед с уверенностью и решимостью. Каждый шаг вперед — это шаг к успеху. И независимо от того, сколько времени или усилий тебе потребуется, помни, что ты способен преодолеть любые сложности. Твой потенциал безграничен, поверь в себя и не останавливайся на достигнутом. Будьте своим собственным источником мотивации, ведь только ты знаешь, на что способен, и какие цели хочешь достигнуть. Уверенно иди к своей мечте, и с каждым пройденным этапом ты будешь только усиливаться. *Жизнь* — это _непредсказуемый_ путь, полный возможностей и испытаний. Используй каждую трудность как спусковой крючок для твоего роста, и позволь своей страсти осветить каждый шаг твоего пути к _успеху_.',
                     parse_mode='Markdown')

@bot.message_handler(commands=['meme'])
def main(message):
    bot.send_message(message.chat.id, '[ССЫЛКА](https://vk.com/shvt)', parse_mode='Markdown')

bot.infinity_polling()

