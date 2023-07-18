import random

messages = ['Sim com certeza',
            'Sim claro',
            'Me explique devagar e tente de novo',
            'Me pergunte mais tarde',
            'Se concentre e pergunte de novo',
            'Minha resposta é não',
            'Não nem pensar',
            'Definitivamente não']

print(messages[random.randint(0, len(messages) - 1)])