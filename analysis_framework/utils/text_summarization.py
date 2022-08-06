from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words 
from sumy.summarizers.edmundson import EdmundsonSummarizer
from analysis_framework.utils import static as rs

# Uncomment below imports if not pre-installed
import nltk
# nltk.download('punkt')


def summarize_text(text, language='english'):
    summarizer = EdmundsonSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)
    summarizer.bonus_words = rs.bonus_words_list
    summarizer.stigma_words = rs.stigma_words_list
    summarizer.null_words = get_stop_words(language)
    sentence_list=[]
    count=0
    summary = summarizer(PlaintextParser(text, Tokenizer(language)).document, rs.sentence_count)
    for sentence in summary:
        count += 1
        sentence_list.append(str(f'{count}. {sentence}'))
    output = "\n".join(sentence_list)
    return output
