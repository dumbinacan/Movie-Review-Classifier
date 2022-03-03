#!/bin/python
import pre_process
import pre_process_binNB
import pre_process_binNB_and_Neg
import pre_process_Neg

root = "movie-review-HW2/aclImdb/";
test = root + "test/";
train = root + "train/";
#default
pre_process.prep(test);
pre_process.prep(train);
#Binary Multinomial Naive Bayes
pre_process_binNB.prep(test);
pre_process_binNB.prep(train);
#Binary Multinomial Naive Bayes and Negation handler
pre_process_binNB_and_Neg.prep(test);
pre_process_binNB_and_Neg.prep(train);
#only using Negation handler
pre_process_Neg.prep(test);
pre_process_Neg.prep(train);
