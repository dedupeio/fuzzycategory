# fuzzycategory
Fuzzy Categorical Distances

Part of the [Dedupe.io](https://dedupe.io/) cloud service and open source toolset for de-duplicating and finding fuzzy matches in your data.

For cases which the number of classes is large, but much smaller than the number of of records we can do something like a "semantic" distance between categories. A good example would be something like occupation in campaign finance data.

```python
{'name' : 'Jim Bob', 'employer' : 'JP Morgan Chase', 'occupation' : 'lawyer'}
{'name' : 'James Bob', 'employer' : 'JP Morgan Chase', 'occupation' : 'lawyer'}
{'name' : 'Jim Bob', 'employer' : 'JP Morgan Chase', 'occupation' : 'attorney''}
```

We can 1.

# Create a vector of all the terms that don't appear in the focal field

```python
lawyer : {'Jim' : 1, 'James' : 1, 'Bob' : 2, 'JP' : 2, 'Morgan' : 2, 'Chase' : 2}
attorney : {'Jim' : 1, 'Bob' : 1, 'JP' : 1, 'Morgan' : 1, 'Chase' : 1}
```

The "distance" between attorney and lawyer is then the tfidf weighted cosine distance between those vectors.

Alternately, 

# Create a vector of exact field matches

```python
lawyer : {'Jim Bob' : 1, 'James Bob' : 1, 'JP Morgan Chase' : 2}
attorney : {'Jim Bob' : 1, 'JP Morgan Chase' : 2}
```

Or even a 

# vector exact matches for everything except the focal field

```python
lawyer : {'Jim Bob, JP Morgan Chase' : 1, 'James Bob, JP Morgan Chase' : 1}
attorney : {'James Bob, JP Morgan Chase' : 1}
```

This last version is very similar to what http://www.naviddianati.com/fec is doing with their Maximum Likelihood Filter: http://arxiv.org/abs/1503.04085


If we wanted to get even more fancy we could use word2vec instead of the tfidf business: https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-2-word-vectors
