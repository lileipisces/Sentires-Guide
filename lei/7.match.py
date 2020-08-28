import pickle


product2json = pickle.load(open('lei/input/product2json.pickle', 'rb'))
product2feature_pos = pickle.load(open('lei/intermediate/product2feature_pos.pickle', 'rb'))
product2feature_neg = pickle.load(open('lei/intermediate/product2feature_neg.pickle', 'rb'))


reviews = []
for (product_id, review_list) in product2json.items():
    if product_id in product2feature_pos:
        feature2adj = product2feature_pos[product_id]
        for (feature, adj2sent_list) in feature2adj.items():
            for (adj, sent_list) in adj2sent_list.items():
                for (sent, count) in sent_list:
                    for idx, review in enumerate(review_list):
                        text = review['text']
                        if text.find(sent) != -1:
                            if 'sentence' in review:
                                review['sentence'].append((feature, adj, sent, 1))  # (feature, adj, sent)
                            else:
                                review['sentence'] = [(feature, adj, sent, 1)]
                            review_list[idx] = review
                            count -= 1
                            if count == 0:
                                break

    if product_id in product2feature_neg:
        feature2adj = product2feature_neg[product_id]
        for (feature, adj2sent_list) in feature2adj.items():
            for (adj, sent_list) in adj2sent_list.items():
                for (sent, count) in sent_list:
                    for idx, review in enumerate(review_list):
                        text = review['text']
                        if text.find(sent) != -1:
                            if 'sentence' in review:
                                review['sentence'].append((feature, adj, sent, -1))  # (feature, adj, sent)
                            else:
                                review['sentence'] = [(feature, adj, sent, -1)]
                            review_list[idx] = review
                            count -= 1
                            if count == 0:
                                break

    reviews.extend(review_list)

pickle.dump(reviews, open('lei/output/reviews.pickle', 'wb'))

'''
keys:
'user',
'item',
'rating',
'text',
'sentence' (feature, adj, sent, score)
'''
