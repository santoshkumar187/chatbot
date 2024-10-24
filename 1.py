import gensim
from gensim.models import Word2Vec
import nltk
from nltk.corpus import brown
nltk.download('brown')  # Download the Brown corpus dataset


# Load the Brown corpus (a collection of sentences)
sentences = brown.sents()

# Display an example sentence
print(sentences[0])  # Output: ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]

# Initialize the Word2Vec model with hyperparameters
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# Train the model
model.train(sentences, total_examples=len(sentences), epochs=10)

# Get the vector (embedding) for a specific word
word_embedding = model.wv['jury']
print("Word embedding for 'jury':")
print(word_embedding)

# Find words that are most similar to 'jury'
similar_words = model.wv.most_similar('jury')
print("Words similar to 'jury':")
print(similar_words)

# Save the model to a file
model.save("word2vec_brown.model")

# Load the model from the saved file
loaded_model = Word2Vec.load("word2vec_brown.model")


import gensim
from gensim.models import Word2Vec
import nltk
from nltk.corpus import brown
nltk.download('brown')

# Load the Brown corpus dataset
sentences = brown.sents()

# Initialize the Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# Train the model
model.train(sentences, total_examples=len(sentences), epochs=10)

# Access the word embedding for a specific word
print("Word embedding for 'jury':")
print(model.wv['jury'])

# Find words that are most similar to 'jury'
similar_words = model.wv.most_similar('jury')
print("\nWords similar to 'jury':")
print(similar_words)

# Save the model to a file
model.save("word2vec_brown.model")

# Load the model from the file
loaded_model = Word2Vec.load("word2vec_brown.model")
