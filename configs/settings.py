import os
from dotenv import load_dotenv
from support.messages import *
load_dotenv()

try:
    TOKEN_TELEGRAM = os.environ['TOKEN_TELEGRAM']
    print(sucess_message("VÁRIAVEIS DE AMBIENTE CARREGADAS!"))
except Exception as error:
    raise Exception(error_message(f"ERRO AO CARREGAR AS VARIÁVEIS DE AMBIENTE! {error}"))