import nltk
nltk.download('punkt')
nltk.download('gutenberg')

# Task 1 (1 mark)
import collections
def get_top_tokens(text_collection, n, stopwords):
    """Return a list of the n most frequent non-stop tokens, sorted by frequency.
    Make sure that the list of tokens returned is lowercased, and that all
    comparison with the list of stop words are not case sensitive.
    >>> get_top_tokens(gutenberg_collection, 10, nltk_stopwords)
    ['shall', 'said', "'s", 'unto', 'lord', 'thou', 'one', 'thy', 'man', 'god']
    >>> my_collection = ["This is sentence 1", "This is sentence 2", "And sentence 3"]
    >>> get_top_tokens(my_collection, 3, [])
    ['sentence', 'this', 'is']

    """
    return []

# Task 2 (1 mark)
def get_tf(text, template):
    """Return the frequency of each of the tokens listed in the template.
    Make sure that the comparison with the words in the template is not case
    sensitive.

    >>> get_tf("This is sentence 1. This is sentence 2. And sentence 3.", ['this', 'sentence'])
    [2, 3]
    >>> get_tf(gutenberg_collection[0], ['emma', 'my', 'the'])
    [855, 728, 5201]

    """
    return []

# Task 3 (1 mark)
from math import log
def get_idf(text_collection, template):
    """Return a list of inverse document frequencies for every token listed in the
    template, where each element in text_collection represents one document.
    Again, make sure that the comparisons are not case sensitive. The inverse
    document frequency is computed by the formula indicated in the lectures,
    where the base of log is 10:

                        number of documents
    idf(t) = log(-----------------------------------)
                 number of documents that contain t

    >>> get_idf(gutenberg_collection, ['emma', 'my', 'sam'])
    [0.9542425094393249, 0.0, 1.255272505103306]
    >>> get_idf(gutenberg_collection, ['unto', 'lord', 'thou'])
    [0.47712125471966244, 0.07918124604762482, 0.1413291527964693]
    """
    return []

# Task 4 (1 mark)
def get_tfidf(text_collection, list_documents, template):
    """Return the tf.idf of each document of the list of documents, where the idf
    is computed relative to the text collection. The tf.idf values should be
    computed based on the words of the template. Again, make sure that all
    comparisons are not case sensitive.
    >>> get_tfidf(gutenberg_collection, gutenberg_collection[:2], ['unto', 'lord', 'thou'])
    [[0.0, 0.4750874762857489, 0.1413291527964693], [0.0, 0.7126312144286233, 0.0]]
    """
    return []

# Task 5 (1 mark)
from math import sqrt
def cosine_similarity(text_collection, text1, text2, template):
    """Return the cosine similarity between the tfidf of text1 and that of text2
    where the cosine similarity is defined with the formula given in the
    lectures:

                                sum_i(text1_i*text2_i)
    cos(text1, text2) = ----------------------------------------------
                        sqrt(sum_i(text1_i^2)) sqrt(sum_i(text2_i^2))

    You can implement the cosine similarity directly, or you can use a library such as sklearn:
    https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html
    >>> cosine_similarity(gutenberg_collection, gutenberg_collection[0], gutenberg_collection[0], ['unto', 'lord', 'thou'])
    1.0
    >>> cosine_similarity(gutenberg_collection, gutenberg_collection[0], gutenberg_collection[1], ['unto', 'lord', 'thou'])
    0.9584884365371023
    """
    return 2.0

# DO NOT MODIFY THE CODE BELOW
if __name__ == "__main__":
    import doctest
    gutenberg_collection = [nltk.corpus.gutenberg.raw(d) for d in nltk.corpus.gutenberg.fileids()]
    nltk_stopwords = nltk.corpus.stopwords.words('english') + [',', '.', ';', "''", ':', '``', '?', '--', '!']
    doctest.testmod()
