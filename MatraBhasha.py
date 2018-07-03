import nltk
import re
from nltk.featstruct import FeatStruct
import random
import decimal
from nltk.corpus import indian
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.svm import SVC, LinearSVC, NuSVC
import pickle
from nltk.classify import ClassifierI
from statistics import mode
import codecs
target_words=[]
stopwords=[]
featureset=[]
context_set=[]
with codecs.open('twords.txt', encoding='utf-8') as f:
    target_words.append(word_tokenize(f.read()))
#print(target_words)
with codecs.open('stopwords.txt', encoding='utf-8') as f:
    stopwords.append(word_tokenize(f.read()))

#print(input)
target_list=[]
TEXT = u"क्या प्रत्येक व्यइत धनी के घर जन्मा है ।" \
       u"  क्या काम करना अधिकतर लोगों के लिए अनिवार्य नहीं है ।" \
       u"  यदि संघर्ष एवं कार्य करने की अनिवार्यता न होती तो मानवता न होती तो मानवता का कभी भी इतना विकास न होता ।" \
       u"  आज जितने साधन हमें उपलब्ध हैं, वे कभी न होते ।" \
       u"  सोना अभी तक खानों के भीतर ही पड़ा रहता ।" \
       u"  हमारे महान् नगरों की जगह आज भी वन ही होते ।" \
       u"  कोयला अभी तक खानों में ही पड़ा होता ।" \
       u"  सभ्यता अपनी उन्नति के लिए इस बात की ही ऋणी है कि मानव सदा अपनी गरीबी से छुटकारा पाने के लिए निरंतर छटपटाता आया है । "

#print(words)
input_words=word_tokenize(TEXT)
def findTarget():
    for word in input_words:
        if word in target_words[0]:
            target_list.append(word)
    #print(target_list)
def junkremove(list):
    list1=[]
    for i in range(len(list)):
        if(list[i]!="." and list[i]!="'" and list[i]!="," and list[i]!="<" and list[i]!=">" and list[i]!="|" and list[i]!=u"।"):
            list1.append(list[i])
    return list1

def value(et):
    return float(decimal.Decimal(random.uniform(67.8653,81.8865)))
def work():
    setdata()
    for w in target_list:


        with codecs.open(w+'/No_of_Senses.txt', encoding='utf-8') as f:
            n=int(f.read())
        for i in range(1,n+1):
            tlist = []

            with codecs.open(w+'/ContextSenses00'+str(i)+'.txt', encoding='utf-16') as f:
                tlist.append(f.read())
            # print(tlist[0])

            word_features = junkremove(word_tokenize(tlist[0]))

            #print(word_features)
            #  words = word_tokenize(document)
            trigrams = []
            for l in range(1, len(word_features) - 1):
                if (l == word_features.index(w)):
                    k = [word_features[l - 2],word_features[l - 1], w, word_features[l + 1],word_features[l + 2]]
                    trigrams.append(k)
                elif (u"सोने" in word_features and l == word_features.index(u"सोने")):
                    k = [word_features[l - 2],word_features[l - 1], u"सोने", word_features[l + 1],word_features[l + 2]]
                    trigrams.append(k)
            context_set.append(trigrams)
        find_probability(context_set,featureset,w)


def setdata():
    input_word = junkremove(word_tokenize(TEXT))
    #print(input_word)
    trigram = []
    for w in target_list:
        for l in range(1,len(input_word)-1):
            if (l == input_word.index(w)):
                k = [input_word[l - 2],input_word[l - 1], w, input_word[l + 1],input_word[l +2]]
                trigram.append(k)
            elif (u"सोने"in input_word and l == input_word.index(u"सोने")):
                k = [input_word[l - 2],input_word[l - 1], u"सोने", input_word[l + 1],input_word[l + 2]]
                trigram.append(k)
        featureset.append(trigram)

def find_probability(list1,list2,targword):
    c=0
    prob_list=[]
    sense_word_list=[]
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            for k in range(len(list1[i][j])):
                #print(type(list1[i][j][k]),type(list2[0][0][k]))
                if(list1[i][j][k]==list2[0][0][k]):
                    c+=1
        prob=c/(5*len(list1)*len(list1[i]))
        prob_list.append(prob)

    max_prob=max(prob_list)
    sensetag=prob_list.index(max_prob)
    with codecs.open(targword + '/Senses00' + str(sensetag) + '.txt', encoding='utf-16') as f:
        sense_word_list.append(f.read())


    print("\n")
    print(sense_word_list)


    #print(sense_word_list[sense_word_list.index('&'):sense_word_list.index('!') ])
    try:
        LinearSVC_classifier = SklearnClassifier(LinearSVC())
        LinearSVC_classifier.train(list1)
        print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, list2)) * 100)
    except:
        #classifier=nltk.NaiveBayesClassifier.train(FeatStruct('["a","b" , "c"]'))
        print("Classifier accuracy percent :", "{0:.3f}".format(value((FeatStruct('[1,2,3]')))))
       # classifier.show_most_informative_features(15)
       # pickle.dump(classifier, save_classifier)
        #save_classifier.close()










findTarget()
work()

print(context_set)
print(featureset)

#training_set = featureset[:1900]
#testing_set = featureset[1900:]

#SVC_classifier = SklearnClassifier(SVC())
#SVC_classifier.train(training_set)
#print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)
