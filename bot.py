# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')
conv = ['oi', 'olá', 'olá,Bom dia', 'Bom dia','Bum dinha', 'Como estás?', '¡Estoy Bién!', 'Nosotras sentimos sua falta','É um passaro? , É um avião?, É um homem nuvem!']

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
    quest = input ('Você: ')
    response = bot.get_response (quest)
    print('Robozinho camarada:',response)

while False: print('Meu intelecto ainda não é evoluido o suficiente para responder este tipo de pergunta escrota!')

