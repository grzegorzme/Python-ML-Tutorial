from nltk.stem.porter import PorterStemmer

def tokenizer(text):
    return text.split()
	
_porter = PorterStemmer()
def tokenizer_porter(text):
    return [_porter.stem(word) for word in text.split()]
    #return pd.Series(text.split()).apply(porter.stem).tolist()