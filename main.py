meme_dict = {
            'КРИНЖ': 'Что-то очень странное или стыдное',
            'ЛОЛ': 'Что-то очень смешное',
            'КРАШ': 'Человек, который нравится',
            'РОФЛ': 'Шутка, прикол',
            'Вайб': 'Атмосфера, настроение.',
            'АГРИТЬСЯ': 'злиться',
            'ЩИЩ': 'одобрение или восторг'
            }
while True:
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('Такого слова нет')
