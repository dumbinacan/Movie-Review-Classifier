#!/bin/python
import NB
root = "movie-review-HW2/aclImdb/";
test = root + "test/";
train = root + "train/";
vocab = root + "imdb.vocab";
test_def = test + "reviews.pickle";
test_bnb = test + "reviews_binNB.pickle";
test_bnn = test + "reviews_bin_and_neg.pickle";
test_neg = test + "reviews_neg.pickle";
train_def = train + "reviews.pickle";
train_bnb = train + "reviews_binNB.pickle";
train_bnn = train + "reviews_bin_and_neg.pickle";
train_neg = train + "reviews_neg.pickle";
NB.NB(train_def, test_def, vocab, root + "results_def.txt");
NB.NB(train_bnb, test_bnb, vocab, root + "results_bnb.txt");
NB.NB(train_bnn, test_bnn, vocab, root + "results_bnn.txt");
NB.NB(train_neg, test_neg, vocab, root + "results_neg.txt");
