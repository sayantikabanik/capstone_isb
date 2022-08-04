import os
import pandas as pd
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words 
from sumy.summarizers.lex_rank import LexRankSummarizer 
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
stop_words = stopwords.words('english')
from analysis_framework import PIPELINE_PATH


class Text_summarization:

    def __init__(self):
        pass

    @classmethod
    def summarize(text, summarizer, sentence_count, bonus_words=['work life balance', 'job security', 'work environment', 'career growth', 'salary', 'culture', 'career' ,'pay', 'improvement', 'manager', 'employees', 'company', 'compensation', 'appraisal'], language='english'):
        summarizer = summarizer(Stemmer(language))
        summarizer.stop_words = get_stop_words(language)
        if isinstance(summarizer, EdmundsonSummarizer):
            summarizer.bonus_words = bonus_words
            summarizer.stigma_words = ['worst', 'low', 'poor', 'bad', 'insecurity', 'no', 'long', 'slow', 'less', 'pressure', 'struggle', 'lack', 'decent', 'issues', 'exhaustion', 'detachment', 'boring', 'hectic', 'pathetic', 'challenging']
            summarizer.null_words = get_stop_words(language)
        summary = summarizer(PlaintextParser.from_file("compiled_text.txt", Tokenizer(language)).document, sentence_count)
        return summary 