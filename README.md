# Telegram_Bot
Hello, this bot was created to verify the presence of members of a group on telegram


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
$ cd Telegram_Bot
```
2. Execute o arquivo do bot:
```shell
$ bot_online.py
```
## Passo 4: Utilização

1. Para definir o status online, digite o comando "on" no grupo do telegram no qual o bot esta alocado e pressione Enter.
O bot enviará uma mensagem informando que você está online a partir do horário em que o comando foi enviado.

2. Para definir o status offline, digite o comando "off" no grupo do telegram no qual o bot esta alocado e pressione Enter.

O bot enviará uma mensagem informando que você está offline a partir do horário em que o comando foi enviado e fornecerá o tempo decorrido entre o momento em que você digitou "on" e quando você digitou "off".

3. Para encerrar a execução do bot, pressione Ctrl+C no terminal.

## Considerações Finais

Certifique-se de que o bot esteja em execução para que ele possa receber e processar os comandos "on" e "off" corretamente. Lembre-se de seguir as etapas de configuração e execução descritas acima.

Sinta-se à vontade para personalizar e adaptar o código-fonte do bot de acordo com suas necessidades.

---
