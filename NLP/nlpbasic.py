# text = "I am learning python"
# lower_text = text.lower()
# token = lower_text.split()
# print(token)
# stopwords = ["am", "is", "are", "the", "a", "an", "i"]
# filtered_tokens = [word for word in token if word not in stopwords]
# print(filtered_tokens)
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string
stop_words = set(stopwords.words('english'))
sentence1 = 'Sentiment analysis uses natural language processing (NLP) and machine learning (ML) technologies to train computer software to analyze and interpret text in a way similar to humans. The software uses one of two approaches, rule-based or ML—or a combination of the two known as hybrid.Each approach has its strengths and weaknesses'
tokenized_word = word_tokenize(sentence1.lower())
filtered_tokens = [word for word in tokenized_word if word not in stop_words]
cleaned_tokens = [word for word in filtered_tokens if word not in string.punctuation]
print(cleaned_tokens)