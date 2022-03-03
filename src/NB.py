#!/bin/python
import math;
import pickle
class Naive_Bayes:
    prior_probabilities = dict();
    feature_vectors = dict();
    vocab = dict();
    tots = dict();
    def __init__(self, vocab):
        for word in vocab:
            self.vocab[word.strip()] = 0;
    def prior(self, class_name):
        tot = 0;
        prior = self.prior_probabilities[class_name];
        for classifier in self.prior_probabilities:
            tot += self.prior_probabilities[classifier];
        return math.log(prior/tot, 2);
    def prob(self, class_name, word):
        countwc = 1;
        tots = self.tots[class_name] + len(self.vocab);
        if word in self.feature_vectors[class_name]:
            countwc += self.feature_vectors[class_name][word];
        return math.log(countwc/tots, 2);
def train(model, reviews):
    for review in reviews:
        tmp = reviews[review];
        if tmp["<class>"] not in model.feature_vectors:
            model.feature_vectors[tmp["<class>"]] = dict();
            model.prior_probabilities[tmp["<class>"]] = 0;
            model.tots[tmp["<class>"]] = 0;
        model.prior_probabilities[tmp["<class>"]] += 1;
        total = model.tots[tmp["<class>"]] = 0;
        vects = model.feature_vectors[tmp["<class>"]]
        for token in tmp:
            total += 1;
            if token in model.vocab:
                if token in vects:
                    vects[token] += tmp[token];
                else:
                    vects[token] = tmp[token];
    return model;
def argmax(model, features):
    aMax = "";
    pMax = None;
    for classifier in model.feature_vectors:
       tmp = model.prior(classifier) + features[classifier];
       if pMax == None or tmp > pMax:
           pMax = tmp;
           aMax = classifier;
    return aMax;
def test(model, review):
    features = dict();
    for classifier in model.feature_vectors:
        features[classifier] = 0;
        for feature in review:
            if feature in model.vocab:
                features[classifier] += model.prob(classifier, feature);
    return argmax(model, features);
def test_all(model, reviews, results):
    correct = 0;
    total = 0;
    for review in reviews:
        test_vector = reviews[review];
        total += 1;
        classifier = test_vector["<class>"];
        del test_vector["<class>"];
        guess = test(model, test_vector);
        tmp = "Review: "  
        for word in test_vector:
            tmp += word + " ";
        tmp += ", Guess: " + guess + ", Answer: " + classifier + " result: ";
        if guess == classifier:
            correct += 1;
            tmp += "correct";
        else:
            tmp += "incorrect";
        results.write(tmp + "\n");
    results.write("Final results. Correct: " + str(correct) + ", Total: " + str(total) + ", Accuracy: " + str((correct/total)*100) +"%");
def NB(train_path, test_path, vocab_path, result_path):
    train_vectors = pickle.load(open(train_path, "rb"));
    test_vectors = pickle.load(open(test_path, "rb"));
    results = open(result_path, "w");
    model = Naive_Bayes(open(vocab_path, "r"));
    train(model, train_vectors);
    test_all(model, test_vectors, results);
def testing(train_path, result_path):
    train_vectors = pickle.load(open(train_path, "rb"));
    results = open(result_path, "w");
    vocab = ("couple", "fast", "fly", "fun", "furious", "love", "shoot")
    review = dict()
    review["fast"] = 1;
    review["couple"] = 1;
    review["shoot"] = 1;
    review["fly"] = 1;
    features = dict();
    model = Naive_Bayes(vocab);
    train(model, train_vectors);
    for classifier in model.feature_vectors:
        features[classifier] = 0;
        for feature in review:
            if feature in model.vocab:
                features[classifier] += model.prob(classifier, feature);
    for classifier in features:
        results.write("p(" + classifier + ") = " + str(features[classifier] + model.prior(classifier)) + "\n");
