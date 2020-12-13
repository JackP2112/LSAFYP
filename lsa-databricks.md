### Latent Semantic Analysis
####  - Databricks Academy
[Youtube](https://www.youtube.com/watch?v=hB51kkus-Rc)

#### (1/5)
Document - A collection of words, rows of the dataset

Body - A collection of documents, the dataset

Dictionary - The set of all words that appear in the body

Topic - A collection of words that co-occur

Latent refers to features which cannot be directly measured.
LSA is an unsupervised learning technique.
The objective of LSA is to create representations of the text data in terms of
topics.
An additional benefit is the reduction of the dimensionality of the text-based
dataset.

LSA is comprised of two steps, to compose a document-term matrix and then
perform a singular value decomposition (SVD) on that matrix.

SVD encodes the document-term matrix in terms of its principal components, in
the case of LSA these represent the topics latent in the original text data.

#### (2/5)
Raw text is converted into a bag-of-words, being the simplest implementation of
a document-term matrix, where each word is associated with the number of times
it occurs in a document.

The SVD is then performed on the bag-of-words matrix, resulting in topic encoded
data.
This data takes the form of two columns representing each topic, being the two
principal components of the data as requested.

Two by-products of the LSA which can provide insight into the topics are the
dictionary, the set of all words, and the encoding matrix.

The encoding matrix has a row for each word in the dictionary and a column for
each topic, the entries in the matrix can be thought of as an expression of that
word in a given topic.

Words which are strongly positive are strongly associated with a topic, words
which are strongly negative are strongly disassociated with a topic.

#### (3/5)
Common words such as 'the' or 'a' which carry little meaning, known as stop
words, can be removed from the analysis when constructing the document-term
matrix to improve the analysis.

#### (4/5)
Due to the nature of the SVD, that is that the vectors returned are inherent to
the data, there is no way to tune the model by adjusting parameters.
What can be adjusted however, is the document-term matrix itself.
This is commonly done using the term frequency-inverse document frequency
(tf-idf) metric.
A simple count, as was used previously, collects term frequency, the number of
times a term appears in a given document.
By weighting this number by the inverse document frequency, a term is penalised
if it appears in many documents.
This is intuitive in that a word which appears in many different documents
is less meaningful to a particular topic.

The topic-encoded data returned from the SVD can be observed to be less noisy
than when measuring term frequency alone.

#### (5/5)
An additional preprocessing step that can be applied to the document-term matrix
is the generation of word lemmas.
A word lemma is the dictionary definition of a word.
The example given is that the words run, ran and running all stem from the word
run.
In LSA, these words should be considered to be the same as they all have the
same meaning with regard to topics.
The same applies for plurals.
