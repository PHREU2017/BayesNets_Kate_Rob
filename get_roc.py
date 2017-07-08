# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:54:08 2017

@author: Katie Bug
"""

def get_list(file):
    l = []
    for line in file:
            s = line.split()
            for v in s[1:]:
            #for v in s:
                l.append(int(v) - 1)
    return l

def get_false(value, labels, pred):
    false = 0
    for i in range(len(labels)):
        if pred[i] == value:
            if labels[i] != value:
                false+= 1
    return false

def get_true(value, labels, pred):
    true = 0
    for i in range(len(labels)):
        if labels[i] == value:
            if pred[i] == value:
                true+= 1
    return true

def get_accuracy(tp, tn, total_pop):
    return (tp + tn) / total_pop

def get_rate(v1, v2):
    return v1 / (v1 + v2)

def get_f(beta, tp, tn, fp, fn):
    num = (1 + beta**2) * tp
    den = ((1 + beta**2) * tp) + (beta**2 * fn) + fp
    return num/den

with open('C:/Users/Katie Bug/Desktop/ProHealth/test_3x_labels.txt', 'r') as labels:
    with open('C:/Users/Katie Bug/Desktop/ProHealth/test_3x_pred.txt', 'r') as pred:

        label_list = get_list(labels)
        pred_list = get_list(pred)
        total_pop = len(label_list)
        false_pos = get_false(1, label_list, pred_list)
        false_neg = get_false(0, label_list, pred_list)
        true_pos = get_true(1, label_list, pred_list)
        true_neg = get_true(0, label_list, pred_list)
        print("fp" , false_pos)
        print("tp" , true_pos)
        print("fn" , false_neg)
        print("tn" , true_neg)
        fnr = get_rate(false_neg, true_pos)
        f5 = get_f(5, true_pos, true_neg, false_pos, false_neg)
        f1 = get_f(1, true_pos, true_neg, false_pos, false_neg)
        accuracy = get_accuracy(true_pos, true_neg, total_pop)
        
        print("\nF1", f1)
        print("F5", f5)
        print("FNR", fnr)
        print("acc:", accuracy)
    
                
                
                
                
                
                