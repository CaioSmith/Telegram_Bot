
# Como criar um bot no Telegram

Este é um passo a passo resumido de como criar um bot no BotFather.

## Passo 1: Encontre o BotFather

Abra o aplicativo Telegram e procure por "BotFather" na barra de pesquisa.

## Passo 2: Crie um novo bot

Inicie uma conversa com o BotFather e digite o comando "/newbot" para criar um novo bot.

## Passo 3: Escolha um nome para o bot

Siga as instruções do BotFather para escolher um nome para o seu bot.

## Passo 4: Obtenha o token de acesso

Após escolher o nome, o BotFather fornecerá a você um token de acesso único para o seu bot. Anote esse token, pois ele será necessário para interagir com a API do Telegram.

## Passo 5: Personalize o bot (opcional)

Opcionalmente, você pode definir uma descrição e uma foto de perfil para o seu bot usando os comandos fornecidos pelo BotFather.

## Passo 6: Comece a usar o seu bot

Agora que você criou o bot com sucesso, você pode usar o token fornecido pelo BotFather para programar e interagir com o seu bot.

## Recursos Adicionais

Consulte a [documentação oficial do Telegram Bot API](https://core.telegram.org/bots/api) para obter mais informações sobre todas as opções e recursos disponíveis para personalizar e desenvolver seu bot.

---

# Passo a Passo para Utilizar o Bot

Este repositório contém um bot que permite definir o status online/offline com base nos comandos "on" e "off" digitados. O bot também informará o tempo decorrido entre o momento em que você digitou "on" e quando você digitou "off".

## Passo 1: Instalação

Clone este repositório para sua máquina local usando o comando:
```shell
$ git clone https://github.com/CaioSmith/Telegram_Bot.git
```

## Passo 2: Configuração

Certifique-se de ter o Python instalado em sua máquina. Em seguida, instale as dependências necessárias executando o seguinte comando:
```shell
$ pip install -r requirements.txt
```
## Passo 3: Execução

1. Navegue até o diretório do projeto:
```shell
$ cd caminho/do/diretorio/na/sua/maquina
```
2. Execute o arquivo do bot:
```shell
$ python bot_online.py
```
## Passo 4: Utilização

1. Para definir o status online, digite o comando "on" no grupo do telegram no qual o bot esta alocado e pressione Enter.
O bot enviará uma mensagem informando que você está online a partir do horário em que o comando foi enviado.

2. Para definir o status offline, digite o comando "off" no grupo do telegram no qual o bot esta alocado e pressione Enter.
O bot enviará uma mensagem informando que você está offline a partir do horário em que o comando foi enviado e fornecerá o tempo decorrido entre o momento em que você digitou "on" e quando você digitou "off".

3. Para encerrar a execução do bot, pressione Ctrl+C no terminal no qual o bot está sendo executado.

## Considerações Finais

Certifique-se de que o bot esteja em execução para que ele possa receber e processar os comandos "on" e "off" corretamente. Lembre-se de seguir as etapas de configuração e execução descritas acima.

Sinta-se à vontade para personalizar e adaptar o código-fonte do bot de acordo com suas necessidades.

---
