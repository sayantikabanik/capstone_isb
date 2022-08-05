import os
import pandas as pd
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words 
from sumy.summarizers.edmundson import EdmundsonSummarizer
stop_words = stopwords.words('english')
from analysis_framework import PIPELINE_PATH
from analysis_framework.utils import static as rs


class Text_summarization:

    def __init__(self):
        pass

    @classmethod
    def summarize(text, summarizer, sentence_count, bonus_words=rs.bonus_words_list, language='english'):
        summarizer = summarizer(Stemmer(language))
        summarizer.stop_words = get_stop_words(language)
        if isinstance(summarizer, EdmundsonSummarizer):
            summarizer.bonus_words = rs.bonus_words_list
            summarizer.stigma_words = rs.stigma_words_list
            summarizer.null_words = get_stop_words(language)
        summary = summarizer(PlaintextParser.from_file("compiled_text.txt", Tokenizer(language)).document, sentence_count)
        return summary 