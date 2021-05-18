import pickle
import gzip
import re

raw_path = 'input/reviews_Musical_Instruments_5.json.gz'  # path to load raw reviews
writer_1 = open('input/record.per.row.txt', 'w', encoding='utf-8')
product2text_list = {}
product2json = {}
for line in gzip.open(raw_path, 'r'):
    review = eval(line)
    text = ''
    if 'summary' in review:
        summary = review['summary']
        if summary != '':
            text += summary + '\n'
    text += review['reviewText']

    writer_1.write('<DOC>\n{}\n</DOC>\n'.format(text))

    item_id = review['asin']
    json_doc = {'user': review['reviewerID'],
                'item': item_id,
                'rating': int(review['overall']),
                'text': text}

    if item_id in product2json:
        product2json[item_id].append(json_doc)
    else:
        product2json[item_id] = [json_doc]

    if item_id in product2text_list:
        product2text_list[item_id].append('<DOC>\n{}\n</DOC>\n'.format(text))
    else:
        product2text_list[item_id] = ['<DOC>\n{}\n</DOC>\n'.format(text)]

with open('input/records.per.product.txt', 'w', encoding='utf-8') as f:
    for (product, text_list) in product2text_list.items():
        f.write(product + '\t' + str(len(text_list)) + '\tfake_URL')
        text = '\n\t' + re.sub('\n', '\n\t', ''.join(text_list).strip()) + '\n'
        f.write(text)

pickle.dump(product2json, open('input/product2json.pickle', 'wb'))
