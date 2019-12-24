from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('TW Chat Bot')

conversa = ['oi', 'olá', 'olá,Bom dia', 'Bom dia','BOM dia', 'Como estás?', '¡Estoy Bién!',
 'Nosotras sentimos sua falta','É um passaro? , É um avião?, É um homem nuvem!','Oi', 'Olá', 'Tudo bem?',
  'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Você: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Robozinho camarada: ', resposta)
    else:
        print('Robozinho camarada: Meu intelecto ainda não é evoluido o suficiente para responder este tipo de pergunta!')
