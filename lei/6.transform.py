import pickle
import re


def data_format(path):
    product2feature = {}
    with open(path, 'r', errors='ignore') as f:
        line = f.readline()
        while line != '':
            product = line.split('\t')[2]
            line = f.readline()
            if line == '' or line.startswith('e'):
                continue

            feature2adj = {}
            while line != '' and not line.startswith('e'):
                feature = line[1:].strip()

                adj2sen = {}
                line = f.readline()
                while line.startswith('o'):
                    content = line[1:].strip().split('\t')
                    adj_phrase = content[0]
                    phrase_count = int(content[1])
                    sentence_c = []
                    while phrase_count > 0:
                        line = f.readline()[1:].strip()
                        sentence_count = re.findall('\([0-9]+\)', line)[-1]
                        sentence = line[:-(len(sentence_count) + 1)]
                        count = int(sentence_count[1:-1])
                        sentence_c.append((sentence, count))

                        phrase_count -= count

                    adj2sen[adj_phrase] = sentence_c

                    line = f.readline()

                feature2adj[feature] = adj2sen

            product2feature[product] = feature2adj

    return product2feature


product2feature_pos = data_format('lei/output/pos.sentence.txt')
product2feature_neg = data_format('lei/output/neg.sentence.txt')
pickle.dump(product2feature_pos, open('lei/intermediate/product2feature_pos.pickle', 'wb'))
pickle.dump(product2feature_neg, open('lei/intermediate/product2feature_neg.pickle', 'wb'))


'''
an example:

{'The Ritz-Carlton, Hong Kong':
    {'gluten':
        {'and the': [('My Wife is gluten free and they were able to provide gluten free bread at short notice', 1)],
        'free': [('I have special dietary requirements - gluten free - which the Concierge Club Staff went out of the way to accommodate', 1),
                    ('My Wife is gluten free and they were able to provide gluten free bread at short notice', 1),
                    ('They were even able to accommodate my Wife with gluten free pasta which she thoroughly enjoyed', 1)]},
    'smiles': {'warm': [('The Ritz-Carlton welcomed my family and me with the warmest of smiles in the fifth tallest building in the world and most luxurious from Hong Kong', 1)],
                'superb': [('We were greeted by different staff with smiles and superb services', 1)]}},
'Korean Hostel': {'stay': {'on': [("If you've stayed on a backpackers before you'll be fine", 1)]}},
'Gloria Guesthouse': {'staff': {'helpful': [('staff is helpful', 1)]}, 'room': {'basic': [('room is spacious enough for 2 people with good bathroom and all basic amenities', 1)]}}}

'''
