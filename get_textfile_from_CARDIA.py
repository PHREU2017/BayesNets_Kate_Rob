# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:47:23 2017

@author: Katie Bug
"""

import statistics

all_people = []
sex_dict = {}
race_dict = {}
age_dict = {}
bmi_dict = {}
# systolic bp - during beat
sbp_dict = {}
# diastolic bp - btw beats
dbp_dict = {}
chol_dict = {}
# "bad" cholesterol
ldl_dict = {}
# "good" cholesterol
hdl_dict = {}
# triglycerides 
trig_dict = {}
# glucose
glu_dict = {}
heavy_dict = {}
moder_dict = {}
edu_dict = {}
smoker_dict = {}
hbp_dict = {}
value_dict = {}

def initialize_temporal_list(person_name, dict_name):
    dict_name[person_name] = [-1, -1, -1, -1, -1, -1]
    
def add_temporal_data(person_name, data, time, dict_name):
    index = 0 
    time = int(time)
    if time == 5:
        index = 1
    elif time == 7:
        index = 2
    elif time == 10:
        index = 3
    elif time == 15:
        index = 4
    elif time == 20:
        index = 5
    dict_name[person_name][index] = float(data)

def add_to_appropriate_dict(classifier, args):
    if classifier == "sex":
        sex_dict[args[0]] = args[1]
    elif classifier == "race":
        race_dict[args[0]] = args[1]
    elif classifier == "age":
        if args[0] not in age_dict: 
            initialize_temporal_list(args[0], age_dict)
        add_temporal_data(args[0], args[1], args[2], age_dict)
    elif classifier == "bmi":
        if args[0] not in bmi_dict: 
            initialize_temporal_list(args[0], bmi_dict)
        add_temporal_data(args[0], args[1], args[2], bmi_dict)
    elif classifier == "sbp":
        if args[0] not in sbp_dict: 
            initialize_temporal_list(args[0], sbp_dict)
        add_temporal_data(args[0], args[1], args[2], sbp_dict)
    elif classifier == "dbp":
        if args[0] not in dbp_dict: 
            initialize_temporal_list(args[0], dbp_dict)
        add_temporal_data(args[0], args[1], args[2], dbp_dict)
    elif classifier == "chol":
        if args[0] not in chol_dict: 
            initialize_temporal_list(args[0], chol_dict)
        add_temporal_data(args[0], args[1], args[2], chol_dict)
    elif classifier == "ldl":
        if args[0] not in ldl_dict: 
            initialize_temporal_list(args[0], ldl_dict)
        add_temporal_data(args[0], args[1], args[2], ldl_dict)
    elif classifier == "hdl":
        if args[0] not in hdl_dict: 
            initialize_temporal_list(args[0], hdl_dict)
        add_temporal_data(args[0], args[1], args[2], hdl_dict)
    elif classifier == "trig":
        if args[0] not in trig_dict: 
            initialize_temporal_list(args[0], trig_dict)
        add_temporal_data(args[0], args[1], args[2], trig_dict)
    elif classifier == "glu":
        if args[0] not in glu_dict: 
            initialize_temporal_list(args[0], glu_dict)
        add_temporal_data(args[0], args[1], args[2], glu_dict)
    elif classifier == "heavy":
        if args[0] not in heavy_dict: 
            initialize_temporal_list(args[0], heavy_dict)
        add_temporal_data(args[0], args[1], args[2], heavy_dict)
    elif classifier == "moder":
        if args[0] not in moder_dict: 
            initialize_temporal_list(args[0], moder_dict)
        add_temporal_data(args[0], args[1], args[2], moder_dict)
    elif classifier == "edu":
        if args[0] not in edu_dict: 
            initialize_temporal_list(args[0], edu_dict)
        add_temporal_data(args[0], args[1], args[2], edu_dict)
    elif classifier == "smoker":
        if args[0] not in smoker_dict: 
            initialize_temporal_list(args[0], smoker_dict)
        add_temporal_data(args[0], args[1], args[2], smoker_dict)
    elif classifier == "hbp":
        if args[0] not in hbp_dict: 
            initialize_temporal_list(args[0], hbp_dict)
        add_temporal_data(args[0], args[1], args[2], hbp_dict)
        
def file_reader(file):
    for line in file:
        first_split = line.split("(")
        classifier = first_split[0]
        second_split = first_split[1].split(").")
        args = second_split[0].split(",")
        if classifier == "person" and args[0] not in all_people:
            all_people.append(args[0])
        elif all_people[-1] == args[0]:
            add_to_appropriate_dict(classifier, args)
            
def initialize_value_dict():
    for p in all_people:
        value_dict[p] = [0, 0, 0, 0, 0, 0]
            
def pos_file_reader(file):
    for line in file:
        first_split = line.split("(")
        second_split = first_split[1].split(").")
        args = second_split[0].split(",")
        add_temporal_data(args[0], 1, args[1], value_dict)

def make_text_file_mean(file):
    header = "key\tsex\trace\tage\tbmi\tsbp\tdbp\tchol\tldl\thdl\t"
    header+="trig\tglu\theavy\tmoder\tedu\tsmoker\thbp\tcac\n"
    file.write(header)
    for p in all_people:
        val = [p]
        val.append(sex_dict[p])
        val.append(race_dict[p])
        if p in age_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, age_dict[p])))
        else:
            val.append(-1)
        if p in bmi_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, bmi_dict[p])))
        else:
            val.append(-1)
        if p in sbp_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, sbp_dict[p])))
        else:
            val.append(-1)
        if p in dbp_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, dbp_dict[p])))
        else:
            val.append(-1)
        if p in chol_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, chol_dict[p])))
        else:
            val.append(-1)
        if p in ldl_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, ldl_dict[p])))
        else:
            val.append(-1)
        if p in hdl_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, hdl_dict[p])))
        else:
            val.append(-1)
        if p in trig_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, trig_dict[p])))
        else:
            val.append(-1)
        if p in glu_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, glu_dict[p])))
        else:
            val.append(-1)
        if p in heavy_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, heavy_dict[p])))
        else:
            val.append(-1)
        if p in moder_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, moder_dict[p])))
        else:
            val.append(-1)
        if p in edu_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, edu_dict[p])))
        else:
            val.append(-1)
        if p in smoker_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, smoker_dict[p])))
        else:
            val.append(-1)
        if p in hbp_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, hbp_dict[p])))
        else:
            val.append(-1)
        if p in value_dict:
            val.append(statistics.mean(filter(
                    lambda a: not a == -1, value_dict[p])))
        line = ""
        for v in val:
            line += str(v) + "\t"
        line+="\n"
        file.write(line)  
        
        
def make_text_file_max(file):
    header = "key\tsex\trace\tage\tbmi\tsbp\tdbp\tchol\tldl\thdl\t"
    header+="trig\tglu\theavy\tmoder\tedu\tsmoker\thbp\tcac\n"
    file.write(header)
    for p in all_people:
        val = [p]
        val.append(sex_dict[p])
        val.append(race_dict[p])
        if p in age_dict:
            val.append(max(age_dict[p]))
        else:
            val.append(-1)
        if p in bmi_dict:
            val.append(max(bmi_dict[p]))
        else:
            val.append(-1)
        if p in sbp_dict:
            val.append(max(sbp_dict[p]))
        else:
            val.append(-1)
        if p in dbp_dict:
            val.append(max(dbp_dict[p]))
        else:
            val.append(-1)
        if p in chol_dict:
            val.append(max(chol_dict[p]))
        else:
            val.append(-1)
        if p in ldl_dict:
            val.append(max(ldl_dict[p]))
        else:
            val.append(-1)
        if p in hdl_dict:
            val.append(max(hdl_dict[p]))
        else:
            val.append(-1)
        if p in trig_dict:
            val.append(max(trig_dict[p]))
        else:
            val.append(-1)
        if p in glu_dict:
            val.append(max(glu_dict[p]))
        else:
            val.append(-1)
        if p in heavy_dict:
            val.append(max(heavy_dict[p]))
        else:
            val.append(-1)
        if p in moder_dict:
            val.append(max(moder_dict[p]))
        else:
            val.append(-1)
        if p in edu_dict:
            val.append(max(edu_dict[p]))
        else:
            val.append(-1)
        if p in smoker_dict:
            val.append(max(smoker_dict[p]))
        else:
            val.append(-1)
        if p in hbp_dict:
            val.append(max(hbp_dict[p]))
        else:
            val.append(-1)
        if p in value_dict:
            val.append(max(value_dict[p]))
        line = ""
        for v in val:
            line += str(v) + "\t"
        line+="\n"
        file.write(line)       

def make_text_file(file):
    header = "key\tsex\trace\tage0\tage5\tage7\tage10\tage15\tage20\t"
    header+="bmi0\tbmi5\tbmi7\tbmi10\tbmi15\tbmi20\t"
    header+="sbp0\tsbp5\tsbp7\tsbp10\tsbp15\tsbp20\t"
    header+="dbp0\tdbp5\tdbp7\tdbp10\tdbp15\tdbp20\t"
    header+="chol0\tchol5\tchol7\tchol10\tchol15\tchol20\t"
    header+="ldl0\tldl5\tldl7\tldl10\tldl15\tldl20\t"
    header+="hdl0\thdl5\thdl7\thdl10\thdl15\thdl20\t"
    header+="trig0\ttrig5\ttrig7\ttrig10\ttrig15\ttrig20\t"
    header+="glu0\tglu5\tglu7\tglu10\tglu15\tglu20\t"
    header+="heavy0\theavy5\theavy7\theavy10\theavy15\theavy20\t"
    header+="moder0\tmoder5\tmoder7\tmoder10\tmoder15\tmoder20\t"
    header+="edu0\tedu5\tedu7\tedu10\tedu15\tedu20\t"
    header+="smoker0\tsmoker5\tsmoker7\tsmoker10\tsmoker15\tsmoker20\t"
    header+="hbp0\thbp5\thbp7\thbp10\thbp15\thbp20\t"
    header+="cac0\tcac5\tcac7\tcac10\tcac15\tcac20\n"
    file.write(header)
    for p in all_people:
        val = [p]
        # if you don't want p#:
        # val[p[1:]]
        val.append(sex_dict[p])
        val.append(race_dict[p])
        if p in age_dict:
            val.extend(age_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in bmi_dict:
            val.extend(bmi_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in sbp_dict:
            val.extend(sbp_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in dbp_dict:
            val.extend(dbp_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in chol_dict:
            val.extend(chol_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in ldl_dict:
            val.extend(ldl_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in hdl_dict:
            val.extend(hdl_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in trig_dict:
            val.extend(trig_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in glu_dict:
            val.extend(glu_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in heavy_dict:
            val.extend(heavy_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in moder_dict:
            val.extend(moder_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in edu_dict:
            val.extend(edu_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in smoker_dict:
            val.extend(smoker_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in hbp_dict:
            val.extend(hbp_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        if p in value_dict:
            val.extend(value_dict[p])
        else:
            val.extend([-1, -1, -1, -1, -1, -1])
        line = ""
        for v in val:
            line += str(v) + "\t"
        line+="\n"
        file.write(line)
        
                          
def make_text_file_for_year(year_index, file):
    i = year_index
    header = "key\tsex\trace\tage\tbmi\tsbp\tdbp\tchol\tldl\thdl\t"
    header+="trig\tglu\theavy\tmoder\tedu\tsmoker\thbp\tcac\n"
    file.write(header)
    for p in all_people:
        val = [p[1:]]
        val.append(sex_dict[p])
        val.append(race_dict[p])
        if p in age_dict:
            val.append(age_dict[p][i])
        else:
            val.append(-1)
        if p in bmi_dict:
            val.append(bmi_dict[p][i])
        else:
            val.append(-1)
        if p in sbp_dict:
            val.append(sbp_dict[p][i])
        else:
            val.append(-1)
        if p in dbp_dict:
            val.append(dbp_dict[p][i])
        else:
            val.append(-1)
        if p in chol_dict:
            val.append(chol_dict[p][i])
        else:
            val.append(-1)
        if p in ldl_dict:
            val.append(ldl_dict[p][i])
        else:
            val.append(-1)
        if p in hdl_dict:
            val.append(hdl_dict[p][i])
        else:
            val.append(-1)
        if p in trig_dict:
            val.append(trig_dict[p][i])
        else:
            val.append(-1)
        if p in glu_dict:
            val.append(glu_dict[p][i])
        else:
            val.append(-1)
        if p in heavy_dict:
            val.append(heavy_dict[p][i])
        else:
            val.append(-1)
        if p in moder_dict:
            val.append(moder_dict[p][i])
        else:
            val.append(-1)
        if p in edu_dict:
            val.append(edu_dict[p][i])
        else:
            val.append(-1)
        if p in smoker_dict:
            val.append(smoker_dict[p][i])
        else:
            val.append(-1)
        if p in hbp_dict:
            val.append(hbp_dict[p][i])
        else:
            val.append(-1)
        if p in value_dict:
            val.append(value_dict[p][i])
        else:
            val.append(-1)
        line = ""
        for v in val:
            line += str(v) + "\t"
        line+="\n"
        file.write(line)        
        
        

f1 = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_1.txt', 'r')
f2 = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_2.txt', 'r')
f3 = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_3.txt', 'r')
f4 = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_4.txt', 'r')
f5 = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_5.txt', 'r')

f1p = open('C:/Users/Katie Bug/Desktop/ProHealth/train_pos_1.txt', 'r')
f2p = open('C:/Users/Katie Bug/Desktop/ProHealth/train_pos_2.txt', 'r')
f3p = open('C:/Users/Katie Bug/Desktop/ProHealth/train_pos_3.txt', 'r')
f4p = open('C:/Users/Katie Bug/Desktop/ProHealth/train_pos_4.txt', 'r')
f5p = open('C:/Users/Katie Bug/Desktop/ProHealth/train_pos_5.txt', 'r')
fmean = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_tst_mean.txt', 'w')
fmax = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_tst_max.txt', 'w')
fw = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_tst.txt', 'w')

wf0 = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_year0.txt', 'w')
wf5 = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_year5.txt', 'w')
wf7 = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_year7.txt', 'w')
wf10 = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_year10.txt', 'w')
wf15 = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_year15.txt', 'w')
wf20 = open('C:/Users/Katie Bug/Desktop/ProHealth/train_facts_year20.txt', 'w')

file_reader(f1)
file_reader(f2)
file_reader(f3)
file_reader(f4)
file_reader(f5)
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

initialize_value_dict()
pos_file_reader(f1p)
pos_file_reader(f2p)
pos_file_reader(f3p)
pos_file_reader(f4p)
pos_file_reader(f5p)
f1p.close()
f2p.close()
f3p.close()
f4p.close()
f5p.close()

print(len(all_people))

make_text_file(fw)
make_text_file_for_year(0, wf0)
make_text_file_for_year(1, wf5)
make_text_file_for_year(2, wf7)
make_text_file_for_year(3, wf10)
make_text_file_for_year(4, wf15)
make_text_file_for_year(5, wf20)
make_text_file_mean(fmean)
make_text_file_max(fmax)
fmax.close()
fmean.close()
fw.close()
        
