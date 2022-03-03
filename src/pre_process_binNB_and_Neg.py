#!/bin/python
import re;
import glob;
import pickle;

def tokenize(review):
    tmp = review.lower();
    token = re.compile("[^a-zA-Z0-9_' ]")
    review = "";
    for char in tmp:
        if re.match(token, char):
            review += " " + char + " ";
        else:
            review += char;
    return review.strip();
def vectf(class_name, review):
    rev = dict();
    negged = False;
    neg = ("no", "not", "never");
    punc = re.compile("[^a-zA-Z0-9_' ]")
    rev["<class>"] = class_name;
    tokens = review.split(" ");
    for token in tokens:
        if token in neg or "n't" in token:
            negged = True;
        if re.match(punc, token):
            negged = False;
        if negged:
            token = "NOT_" + token;
        rev[token] = 1;
    return rev;
def prep(path_to_classes):
    classes = glob.glob(path_to_classes + "*");
    reviews_file = open(path_to_classes + "reviews.txt", "w");
    reviews_dict = dict();
    for c in classes:
        cid = c.replace(path_to_classes, "");
        reviews = glob.glob(c + "/*");
        for review in reviews:
            name = review.replace(c + "/", "");
            tmp = tokenize(open(review, "r").read());
            reviews_dict[name] = vectf(cid, tmp);
    reviews_vect = open(path_to_classes + "/reviews_bin_and_neg.pickle", "wb");
    pickle.dump(reviews_dict, reviews_vect);
