from keras.preprocessing.text import Tokenizer

# define 5 documents
docs = ['Well done!',
		'Good work',
		'Great effort',
		'nice work',
		'Excellent!']

# create the tokenizer
tnr = Tokenizer()

# fit the tokenizer on the documents
tnr.fit_on_texts(docs)

# summarize what was learned
print(tnr.word_counts)
print(tnr.document_count)
print(tnr.word_index)
print(tnr.word_docs)

# integer encode documents
encoded_docs = tnr.texts_to_matrix(docs, mode='count')
print(encoded_docs)