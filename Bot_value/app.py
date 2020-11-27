import telebot
from extensions import get_price,APIException
from config import TOKEN,keys


bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def star_help(message: telebot.types.Message):
    text='Для начало работы бота введите команду боту в следующем формате:\n<Имя валюты>\n<В какую валюту перевести>\n<Кол-во переводимой валюты>\n/values-увидеть список всех доступных валют'
    bot.reply_to(message,text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text="Доступные валюты:"
    for key in keys.keys():
        text='\n'.join((text,key,))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) !=3:
            raise APIException ('Кол-во параметров не соответствует трем.')

        quote, base, amount = values
        total_base=get_price.get(quote, base, amount)
    except APIException as e:
        bot.reply_to(message,f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
