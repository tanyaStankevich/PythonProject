# myBest_scheduleBot
# 5616428738:AAE5_Cfn9kJFIGvNCjidN-FTeYrWNtWpFPE
# API https://core.telegram.org/bots/api


from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from bottoken import bot_token

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Что Вы хотите сделать:\n /view - Просмотреть расписание \n /add - Добавить событие \n /del - Удалить событие \n/change - Изменить событие')
    # keyboard = [
    #     [InlineKeyboardButton('Просмотреть расписание', callback_data='1'), InlineKeyboardButton('Добавить событие', callback_data='2')],
    #     [InlineKeyboardButton('Удалить событие', callback_data='3'), InlineKeyboardButton('Изменить событие', callback_data='4')]
    # ]
    # update.message.reply_text('Что Вы хотите сделать?',
    #                           reply_markup=InlineKeyboardMarkup(keyboard))


def view(update, context):
    schedule = open('events.txt', 'r')
    line = schedule.readline()
    if line == '':
        context.bot.send_message(update.effective_chat.id, 'В Вашей записной книжке нет событий')
    else:
        while line:
            context.bot.send_message(update.effective_chat.id, line)
            line = schedule.readline()

    schedule.close()

def add_message(update, context):
    if 'add' in update.message.text:
        events = open('events.txt', 'a')
        event = str(update.message.text)
        event_write = event.split(' - ')
        # i = 1
        if len(event_write):
            events.write(event_write[1])
        events.write('\n')
        context.bot.send_message(update.effective_chat.id, 'Событие добавлено в Вашу записную книжку')
        events.close()

    if 'del' in update.message.text:
        event = str(update.message.text)
        event_del_find = event.split(' - ')
        del_event = event_del_find[1]
        print(del_event)
        events = open('events.txt', 'r')
        new_events = open('new_events.txt', 'w')
        line = events.readline()

        while line != '':
            line1 = line.split(' ')
            if line1[0] == del_event:
                new_events.write('')
                print(line1[0])
                # break
            if line1[0] != del_event:
                new_events.write(line)
                # break
            line = events.readline()

        events.close()
        new_events.close()

        events = open('events.txt', 'w')
        new_events = open('new_events.txt', 'r')

        linecopy = new_events.readline()
        while linecopy != '':
            events.write(linecopy)
            linecopy = new_events.readline()
        events.close()
        new_events.close()
        context.bot.send_message(update.effective_chat.id, 'Событие удалено')

    if 'change' in update.message.text:
        event = str(update.message.text)
        event_change_find = event.split(' - ')
        change_event = event_change_find[1]
        change_event_add = event_change_find[2]

        events = open('events.txt', 'r')
        new_events = open('new_events.txt', 'w')
        line = events.readline()

        while line != '':
            line1 = line.split(' ')
            if line1[0] == change_event:
                new_events.write(change_event + ' ' + change_event_add + '\n')
                print(line1[0])
                # break
            if line1[0] != change_event:
                new_events.write(line)
                print('error')
                # break
            line = events.readline()

        events.close()
        new_events.close()

        events = open('events.txt', 'w')
        new_events = open('new_events.txt', 'r')

        linecopy = new_events.readline()
        while linecopy != '':
            events.write(linecopy)
            linecopy = new_events.readline()
        events.close()
        new_events.close()
        context.bot.send_message(update.effective_chat.id, 'Событие обновлено')

def add(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите: add - название события (1 слово) + дедлайн + описание (по желанию). Например (соблюдения формата обязательно): add - отчетГД 11.01.2023 Подготовить таблицу')


def del_(update, context):
    # schedule = open('new.txt', 'r')
    # line = schedule.readline()
    # while line:
    #     context.bot.send_message(update.effective_chat.id, line)
    #     line = schedule.readline()
    #
    # schedule.close()

    context.bot.send_message(update.effective_chat.id, 'Введите название записи, которую нужно удалить в формате: del - отчетГД')


def change(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите название записи, которую нужно изменить в формате: change - отчетГД - 14.02.2023 Подготовить презентацию')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, 'Я не могу выполнить эту команду. Выберите команды из списка:\n /view \n /add \n /del \n /change \n')
    # update.effective_chat.id('Я не могу выполнить эту команду. Выберите команды из списка: /view \n /add \n /del \n /change \n')
# def button(update, context):
#     query = update.callback_query
#     query.answer()
#     if query.data == '1':
#         context.bot.send_message(update.effective_chat.id, 'Вы выбрали просмотреть расписание')
#         view
#     if query.data == '2':
#         context.bot.send_message(update.effective_chat.id, 'Вы выбрали добавить событие')
#         add
#     if query.data == '3':
#         context.bot.send_message(update.effective_chat.id, 'Вы выбрали удалить событие')
#         del_
#     if query.data == '4':
#         context.bot.send_message(update.effective_chat.id, 'Вы выбрали изменить событие')
#         change

# button_handler = CallbackQueryHandler(button)
# dispatcher.add_handler(button_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

view_handler = CommandHandler('view', view)
dispatcher.add_handler(view_handler)

add_handler = CommandHandler('add', add)
dispatcher.add_handler(add_handler)

del_handler = CommandHandler('del', del_)
dispatcher.add_handler(del_handler)

change_handler = CommandHandler('change', change)
dispatcher.add_handler(change_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

add_message_handler = MessageHandler(Filters.text, add_message)
dispatcher.add_handler(add_message_handler)

updater.start_polling()
updater.idle()