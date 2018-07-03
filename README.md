# MatraBhasha

Matrabhasha is a python command line application that makes use of Word Sense Disambiguition(WSD) in Hindi language, to find and predict the proper sense for the ambiguous words present in a context paraphrase provided by the user.

## Word Sense Disambiguition

A language is the biggest source of communication to exchange the
information from one network to other. The human mind is very proficient to discover
the exact sense of the particular word in a particular context but it is a long-term
challenge to develop the ability in machine to do natural language processing and
machine learning task.
In Computational Linguistic “word sense disambiguation” (WSD) is a general
problem in natural language processing (NLP). The words or phrases in a language are
said to be ambiguous if they have more than one probable senses or meanings. Words
in a sentence having more than one meanings are said to be polysemous words. To
find the accurate sense of a polysemous word is an important and challenging task so
the method of finding the correct meaning of a polysemous word called as word sense
disambiguation.

Word Sense Disambiguation is the problem of determining the activated sense
of a word in a particular phrase. It is one of the hard problem in NLP so it is said to be
AI Hard problem in Natural language processing. The key to this problem influences
other machine related writing such as anaphora resolution, machine translation,
coherence, discourse, inference, improving relevance of search engines. It is useful for
language understanding applications, for example, man-machine communication,
message understanding etc.

While applying machine translation on a polysemous Hindi word “फल” to
English language, That Hindi word “फल” have two different senses. Sense1 (“फल”)
refer to “Fruit” and the Sense2 refer to “Result”. Similarly, for word “हार” it gives
two senses. Sense1 (“हार”) refer to “Necklace” and the Sense2 refer to “Defeat”.
Therefore, it is important to know the exact sense of a word while doing machine
translation.

## Problem

Problem is to find the accurate sense of a word in a certain Hindi context by
applying supervised machine learning approaches that are Naive Bayes algorithm on
linear support vector machine (SVM) classifier.

To accomplish the above problem, the following research objectives have been dealt
with:

  - To convert the dataset into suitable form to the proposed algorithm
  
  - To train the data by building the feature sets
  
  - To extract the feature sets and compare the testing sets with the training sets
  
  - To find the probability using Naïve Bayes algorithm
  
  - To calculate maximum probability for finding the exact sense
  
  - To find the final correct sense

## Implementation Hardware/Software Interface:

This section lists the minimum hardware and software requirements needed to develop the system efficiently.
    
###### Hardware Interface:

•	8 GB RAM

•	i5 processor

•	GPU
  
###### Software Interface:

•	Operating System		          : Windows

•	IDE				                  : Pycharm

•	Machine Learning Libraries    : Scikit


## Sense annotated corpus

I have used a sense annotated corpus of Hindi language to perform WSD by applying the proposed approach. A sense annotated corpus is a collection of contexts of particular senses, meanings of the senses, and no of senses for each ambiguous word. There are directories made on the name of the ambiguous words and in each directory there are several files, which include the ContextSenses and Senses whose numbers depend on the no of senses that word has in standard Hindi language. For example, ‘सोना’ word is an ambiguous word with two senses, one means gold and other means to sleep.
                                 
The ContextSenses files consist of various paragraphs that are based on the use of the target word in a particular sense for that number. For example, ContextSenses002 contains paragraphs that are based on the meaning ‘to sleep’ for the word ‘सोना’.
 
Then there are files named Senses which consist of meanings for the ambiguous word to make the user understand the meaning portrayed by the sense that is being pointed to after the comparison.

## Bibliography

•	Natural Language Processing with Python– Analyzing Text with the Natural Language Toolkit by Steven Bird, Ewan Klein, and Edward Loper.

•	Software Engineering, Seventh Edition, Ian Somerville.

•	Hands-On Machine Learning with Scikit-Learn and Tensor Flow: Concepts, Tools, and Techniques to Build Intelligent Systems by Aurelian Geron.

•	Machine Learning with Scikit learn Part One | SciPy 2017 Tutorial | Andreas Mueller & Alexandre Gram at youtube.com.

•	Mathematics for machine learning Coursera.org.

•	NLTK 3.3 documentation www.nltk.org.
         
			

