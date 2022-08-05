from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words 
from sumy.summarizers.edmundson import EdmundsonSummarizer
from analysis_framework.utils import static as rs
import nltk
# nltk.download('punkt')

sentence_count = 5


def summarize_text(text, language='english'):
    summarizer = EdmundsonSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)
    summarizer.bonus_words = rs.bonus_words_list
    summarizer.stigma_words = rs.stigma_words_list
    summarizer.null_words = get_stop_words(language)
    summary = summarizer(PlaintextParser(text, Tokenizer(language)).document, sentence_count)
    for sentence in summary:
        return sentence

