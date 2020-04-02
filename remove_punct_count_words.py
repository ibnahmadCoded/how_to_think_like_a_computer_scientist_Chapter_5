import string

article = """
We humans constantly attempt to identify our unique characteristics.
For many our special status comes from possessing a soul or consciousness.
For Descartes, the essence of the soul was “only to think,” and the
possession of the soul distinguished us from the animals (Descartes,
1637/1960). Because they lacked souls, animals could not be distinguished
from machines: “If there were any machines which had the organs
and appearance of a monkey or of some other unreasoning animal, we
would have no way of telling that it was not of the same nature as these
animals” (p. 41). This view resulted in Cartesian philosophy being condemned
by modern animal rights activists (Cottingham, 1978).
More modern arguments hold that it is our intellect that separates us
from animals and machines (Bronowski, 1973). “Man is distinguished
from other animals by his imaginative gifts. He makes plans, inventions,
new discoveries, by putting different talents together; and his discoveries
become more subtle and penetrating, as he learns to combine his
talents in more complex and intimate ways” (p. 20). Biologist Ludwig
von Bertalanffy noted, “symbolism, if you will, is the divine spark distinguishing
the poorest specimen of true man from the most perfectly
adapted animal” (Bertalanffy, 1967, p. 36).
It has been argued that mind emerged from the natural selection of
abilities to reason about the consequences of hypothetical actions (Popper,
1978). Rather than performing an action that would have fatal consequences,
the action can be thought about, evaluated, and discarded
before actually being performed.
"""

def remove_punct(phrase):
    new_article = ""
    for letter in phrase:
        if letter not in string.punctuation:
            new_article += letter
            
    words_list = new_article.split()
    number_of_words = len(words_list) + 1

    count = 0
    for word in words_list:
        if "e" in word:
            count += 1

    print('Your text contains {0} words, of which {1} ({2}%) contains an "e"'
          .format(number_of_words, count, (count * 100 / number_of_words)))
    
