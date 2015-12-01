from __future__ import division

import math
from collections import Counter

class FuzzyCategory(object) :
    def __init__(self, field_name, corpus, other_fields=None):

        docs = {}
        for document in corpus :
            document = dict(document)
            field = document.pop(field_name)
            if field :
                tokens = set(self._list(document, other_fields))
                docs.setdefault(field, set()).update(tokens)

        doc_freq = Counter(token 
                           for tokens in docs.values()
                           for token in tokens)

        num_docs = len(docs)

        token_weights = {token : math.log(count/num_docs)
                         for token, count 
                         in doc_freq.items()
                         if count > 1}

        self.docs = {}
        for field, tokens in docs.items() :
            vector = {token : token_weights[token]
                      for token in tokens 
                      if token in token_weights}

            norm = math.sqrt(sum(weight * weight for weight in vector.values()))
            
            self.docs[field] = (vector, norm)

    def __call__(self, field_1, field_2):
        if field_1 == field_2 :
            return 1.0
        
        elif (field_1 not in self.docs) or (field_2 not in self.docs) :
            return float('nan')

        else :
            vector_1, norm_1 = self.docs[field_1]
            vector_2, norm_2 = self.docs[field_2]

            if norm_1 and norm_2 :
                numerator = 0.0
                for word in set(vector_1) & set(vector_2) :
                    numerator += vector_1[word] * vector_2[word]
                return numerator/(norm_1 * norm_2)
            else :
                return 0.0

    def _list(self, document, other_fields) :
        if other_fields is None :
            return document.values()
        else :
            return (document[field] for field in other_fields)
 
