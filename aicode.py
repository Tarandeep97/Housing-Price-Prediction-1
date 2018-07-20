import nltk
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
para = input()
sent = tokenizer.tokenize(para)
for sentence in sent:
    print(sentence)
