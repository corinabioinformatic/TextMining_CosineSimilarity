## What is this repo?

This repository contains two scripts. One (*cosinesimilarity10words.py*)  return the 10 most similar words  found for your word. The other (*cosinesimilaritypredictionanalogy.py*) predicts analogies of your word.

In essence this is an example of how you can use a pre-trained model of embedded words (FastToText) for predict analogies, using  *Cosine similarity* for finding the 10 most similar words and the closer analogue word. 

Moreover there is an extra script to run a bunch of results at once to test the code is running properly. This script (*cosinesimilarity_test.py*) don't need any entry argument from the user. 

You just need plain Python 3 with no additional dependencies.

The code can be download for improvement. 
Take into account that the code is writted down by using MyPy for more clarity of the code. 

Thanks to the work of @Martinkonicek [Playing with word vectors](https://medium.com/@martinkonicek/playing-with-word-vectors-308ab2faa519) for a detailed explanation.
This project is part of a serie of text Mining exercises inspired by @JimMc99 (see [Tweeter](https://github.com/JimMc99/Tweeter) example).


## Usage

Once you download into your folder this repo, ensure you unzip the files from the folder *data/wordvectors/*. After you can simply run:

```

# 1. Running the test file to see the bunch of results for similarities and analogies. 

$ python cosinesimilarity_test.py


# 2. You also can run the following script to get the 10 most similar words to the input. E.g:

$ python cosinesimilarity10words.py dog 


# 3. You also can run the following script to get the analogue following a pair test. You have to add three words following this mindset:
# Paris is similar to France Like Rome is similar to ____.
# E.g:


$ python cosinesimilaritypredictionanalogy.py Paris France Rome 

```

### Notes from the original author:
Try to edit the code to explore the word embeddings.

This repo only includes a small data file with 1000 words. To get interesting results you'll need to download the [pre-trained word vectors from the fastText website](https://fasttext.cc/docs/en/english-vectors.html).

But don't use the whole 2GB file! The program would use too much memory. Instead, once you download the file take only the top n words, save them to a separate file, and remove the first line. For example (in Ubuntu):

```
$ cat data/wiki-news-300d-1M.vec | head -n 50001 | tail -n 50000 > data/vectors.vec
```

 LICENSE : MIT
