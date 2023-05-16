# Arquivo: bot_online.py
# Autor: Caio Smith
# Data de criação: 21/04/2023
# Última modificação: 21/04/2023
# Descrição: Este código implementa um bot no Telegram que permite registrar o tempo de trabalho online de um usuário.

# Importa as bibliotecas necessárias
import telebot
from configs.settings import *
import datetime

# Define o token do bot do Telegram
TOKEN = TOKEN_TELEGRAM

# Cria uma instância do bot
bot = telebot.TeleBot(TOKEN)

user_status = {}

# Função que é executada quando o usuário digita "on"
@bot.message_handler(func=lambda message: True and 'on' in message.text.lower().split())
def on_handler(message):
    global user_status
    
    if message.text.lower().strip() == 'on':
    
        user_id = message.from_user.id
        
        # Verifica se o usuário já está online
        if user_id in user_status and user_status[user_id]['is_online']:
            bot.send_message(chat_id=message.chat.id, text= f'@{message.from_user.username} Você já está online SEU IMBECIL BURRO, PRESTA ATENÇÃO POHA')
        else:
            # Registra o horário de entrada
            now = datetime.datetime.now()
            new_now = now.strftime('%H:%M:%S')
            user_status[user_id] = {'is_online': True, 
                                    'on_time': now, 
                                    'total_time': datetime.timedelta(0)}
            
            # Envia uma mensagem confirmando a entrada
            reply_message = f'@{message.from_user.username} você está ON seu merda, e ainda é ás {new_now} seu bosta'
            bot.send_message(chat_id=message.chat.id, text=reply_message)

# Função que é executada quando o usuário digita "off"
@bot.message_handler(func=lambda message: True)
def off_handler(message):
    global user_status
    
    if message.text.lower().strip() == 'off':
        
        user_id = message.from_user.id
        
        # Verifica se o usuário já estava online antes de digitar "off"
        if user_id in user_status and user_status[user_id]['is_online']:
            # Calcula o tempo de trabalho online
            now = datetime.datetime.now()
            on_time = user_status[user_id]['on_time']
            diff = now - on_time
            
            user_status[user_id]['is_online'] = False
            user_status[user_id]['on_time'] = None
            
            hours, remainder = divmod(diff.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            if hours >= 6:
                reply_message = f"@{message.from_user.username} Horário excedido! Você já trabalhou por mais de 6 horas."
                bot.send_message(chat_id=message.chat.id, text=reply_message)
            else:
                # Formata a mensagem de resposta com o tempo trabalhado
                if hours > 0:
                    reply_message = f"@{message.from_user.username} está OFFLINE ás {now.strftime('%H:%M:%S')}\n Ficou ONLINE por {hours:02}:{minutes:02}:{seconds:02} horas"
                elif minutes > 0:
                    reply_message = f"@{message.from_user.username} está OFFLINE ás {now.strftime('%H:%M:%S')}\n Ficou ONLINE por {hours:02}:{minutes:02}:{seconds:02} minutos"
                else:
                    reply_message = f"@{message.from_user.username} está OFFLINE ás {now.strftime('%H:%M:%S')}\n Ficou ONLINE por {hours:02}:{minutes:02}:{seconds:02} segundos"
                    
                bot.send_message(chat_id=message.chat.id, text=reply_message)
        else:
            reply_message = f'@{message.from_user.username} Você não estava ON antes porra, deixa de ser burro crlh, putaqpariu!'
            bot.send_message(chat_id=message.chat.id, text=reply_message)

# # Função para mostrar o tempo que os usuários ficaram online
# @bot.message_handler(func=lambda message: True and 'users' in message.text.lower().split())
# def temp_handler(message):
#     global user_status
    
#     # Verifica se há usuários online
#     online_users = [x for x, y in user_status.items() if v['is_online']]
    
#     if not online_users:
#         # Se não houver usuários online, envia uma mensagem informando
#         bot.send_message(chat_id=message.chat.id, text='Nenhum usuário está online no momento.')
#     else:
#         # Se houver usuários online, cria uma mensagem com o tempo que eles estão online
#         reply_message = 'Usuários online:\n'
        
#         for user_id in online_users:
#             user_info = user_status[user_id]
#             on_time = user_info['on_time']
#             now = datetime.datetime.now()
            
#             diff = now - on_time
#             hours, remainder = divmod(diff.seconds, 3600)
#             minutes, seconds = divmod(remainder, 60)
            
#             # Adiciona o nome do usuário e o tempo que está online à mensagem
#             reply_message += f'@{bot.get_chat_member(message.chat.id, user_id).user.username} - {hours:02}:{minutes:02}:{seconds:02}\n'
        
#         bot.send_message(chat_id=message.chat.id, text=reply_message)
    
# Inicia o polling do bot
bot.polling()