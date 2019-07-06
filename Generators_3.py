# B_R_R
# M_S_A_W



"""
Coding Problem on Iterators and Generators:
First, using Iterators, we will write a code that pass in a sentence and print out all words in the sentence in line.
Then, we will do the same thing with generators.
"""

class Sentence:

    def __init__(self, sentence):
        self.sentence=sentence
        self.index=0
        self.words=self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index>=len(self.words):
            raise StopIteration
        index=self.index
        self.index+=1
        return self.words[index]

my_sent=Sentence("Bo nomi parvardigori olamiyon og'oz kardam")
for sent in my_sent:
    print(sent)



# Below is generators code:

def my_sentence(sentence):
    for word in sentence.split():
        yield word

my_sent=my_sentence("Bo nomi Xudovandi Karim sar kardam")
for sent in my_sent:
    print(sent)
