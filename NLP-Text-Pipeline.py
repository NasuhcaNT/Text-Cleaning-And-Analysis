import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from textblob import Word
from warnings import filterwarnings

# Hide warnings and adjust Pandas settings
filterwarnings('ignore')
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.width', 200)

# Load dataset (generic path)
# Example usage: df = pd.read_csv("data/input.csv", index_col=0)
data_path = "your_text_data.csv"
df = pd.read_csv(data_path, index_col=0)
df = df[:2000]  # Optional: limit to first 2000 rows

# Function for text cleaning
def clean_text(text):
    """
    Performs all text preprocessing steps:
    - Convert to lowercase
    - Remove punctuation
    - Remove numbers
    - Remove stopwords
    - Lemmatization
    - Remove rare words
    """
    # Lowercase
    text = text.str.lower()
    # Remove punctuation
    text = text.str.replace(r'[^\w\s]', '')
    # Remove line breaks
    text = text.str.replace("\n", '')
    # Remove numbers
    text = text.str.replace('\d', '')
    
    # Remove stopwords
    stop_words = stopwords.words('english')
    text = text.apply(lambda x: " ".join(x for x in str(x).split() if x not in stop_words))
    
    # Remove rare words
    rare_words = pd.Series(' '.join(text).split()).value_counts()[-1000:]
    text = text.apply(lambda x: " ".join(x for x in x.split() if x not in rare_words))
    
    # Lemmatization
    text = text.apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    
    return text

# Pipeline: text cleaning and visualization

def text_pipeline(text, Barplot=False, Wordcloud=False):
    """
    A full pipeline for text cleaning and visualization.

    :param df: DataFrame containing raw text
    :param Barplot: Boolean, whether to display a barplot of frequent terms
    :param Wordcloud: Boolean, whether to display a wordcloud visualization
    :return: Text column
    """

    df['cleaned_text'] = clean_text(text)
    text = clean_text(text)

    if Barplot:
        tf = text.apply(lambda x: pd.value_counts(x.split(" "))).sum(axis=0).reset_index()
        tf.columns = ["words", "tf"]
        tf[tf["tf"] > 200].plot.bar(x="words", y="tf")
        plt.show()

    if Wordcloud:

        text = " ".join(i for i in text)
        wordcloud = WordCloud(max_font_size=50,
                              max_words=100,
                              background_color="white").generate(text)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    return text


text_pipeline(df["text"], True, True)



