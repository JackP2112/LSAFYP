### LSA
####  - Francisco Iacobelli
[Youtube](https://www.youtube.com/watch?v=bzNch-dBCN8)

For the term-document matrix, cosine similarity may be used to determine the
similarity between different documents and different words, based on the
occurence of the same words in different documents.

One interpretation of the meaning of a word is that it is a kind of average of
the documents in which it occurs, and the meaning of a document is an average of
the words it contains.

This notion of average suggests a dimensionality reduction may be used (SVD).

A simple application of this definition is to generate a document vector for
a new document based on the existing document vectors and the words they
contain.
For each existing document vector, average the word weights of the words which
also occur in the new document.
This average can now be considered a coefficient for that document vector and
the new document can be represented as a vector sum of the existing vectors.

This neatly captures the concept that the meaning of a document is an average
of the words it contains, and the meaning of those words are in turn an average
of the documents in which they occur.

An extension of this introduces the concept of topics, which are an expression
of the context of a word.
One failing of the previous method is that two words may indeed be related but
may not necessarily co-occur.
Taking the cosine similarity of two term vectors which do not co-occur gives
zero, as they share no common document dimension they are orthogonal.

An example given considers papers on human-computer interaction and graph theory
as the body of documents.
The words human and user do not co-occur and so have a similarity of zero,
despite intuitively being related terms.
However, the words human and computer occur together and so do computer and
user.
This gives a notion of context, that two words may be linked through a common
topic rather than direct co-occurence.

This is achieved mathematically via a dimensionality reduction using SVD.
The resultant decomposition allows the extraction of the most significant
components of the matrix, giving a low-rank approximation which essentially
merges similar terms into topics.

Returning to the previous example, the approximated term-document matrix now
contains new coefficients which give a strong positive similarity between human
and user, in line with our intuition about these terms.
Similarly, a negative similarity is found between terms which are not related
through a topic.
