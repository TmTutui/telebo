bot = 0

def Facebookstuff():
    import requests
    import urllib.parse

    Facebook_API= "https://graph.facebook.com/"

    page_name = input("Digite o nome da pagina: ")
    page_data = requests.get(Facebook_API + page_name).json()
    print(page_data)


def Weather():
    import requests

    weatherI = {}
    jsonweather = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=6835fc6a602ac1cd58e1dd9d8d0a7879&lat=-23.5&lon=-46.6").json()
    weatherI['stats'] = jsonweather['weather'][0]['description']
    weatherI['maxtemp'] = ((jsonweather['main']['temp_max'] - 273)//0.01)/100
    weatherI['mintemp'] = ((jsonweather['main']['temp_min'] - 273)//0.01)/100
    
    return weatherI


def Telebot():
    global bot

    import telepot
    token = '660132807:AAHzPff8hI72A3Vmb1zHxkiDCthpdbGoR8Q'
    bot = telepot.Bot(token)

    bot.message_loop(RecebeMsg)

    # answer[0]['message']['text']
    # bot.sendMessage(answer[2]['message']['from']['id'], "executa https://www.google.com.br/")

    while True:
        pass

def RecebeMsg(msg):
    import random

    lista = list(msg['text'])
    Clima = Weather()
    caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
    'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' ,'q' ,'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '-']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    vardig = []
    ndig = []

    print(msg['text'])
    if (msg['text'] == 'Clima') or (msg['text'] == 'clima') or (msg['text'] == '/Clima') or (msg['text'] == '/clima'):
        bot.sendMessage(msg['chat']['id'], "Hoje: " + Clima['stats'] )
        bot.sendMessage(msg['chat']['id'], "A tempertura máxima será de: " + str(Clima['maxtemp']) + "°C" )
        bot.sendMessage(msg['chat']['id'], "E a tempertura mínima será de: " + str(Clima['mintemp']) + "°C" )

    else:
        lista = list(msg['text'])

        if lista[0] == "/" and lista[1] == "r":
            if lista[2] == " ":
                numero = lista[5]
                if len(lista) >=7:
                    numero += lista[6]
                    if len(lista) >=8:
                        numero += lista[7]
                for i in range(int(lista[3])):
                    bot.sendMessage(msg['chat']['id'], random.randint(1,int(numero)))
            else:
                numero = lista[4]
                if len(lista) >=6:
                    numero += lista[5]
                    if len(lista) >=7:
                        numero += lista[6]
                for i in range(int(lista[2])):
                    bot.sendMessage(msg['chat']['id'], random.randint(1,int(numero)))




Telebot()