import nltk
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
words = nltk.tokenize.word_tokenize
para = input()
sent = tokenizer.tokenize(para)
for sentence in sent:
    print(sentence)
    print(words.sentence)
    

