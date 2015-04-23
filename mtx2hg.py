#!/usr/bin/python2.7

# Created on April 23 2015
# Authored by Jianwei Cui

# This script assumes a hyper-graph modeling of matrix
# Views each row as a vertex
# Views each column as a hyper edge

# This script will take input of mtx file storing matrix in COO format
# The output file will be a text file containing a hyper edge each time


import os
from os import listdir
print "This is CJW!"
filepath = "../mtx/"
filelist = os.listdir(filepath)

class entry:
    def __init__(self):
        self.r_idx = 0;
        self.c_idx = 0;
        self.value = 0.0;

for filename in filelist:
    print "Processing " + filename
    fid = open(filepath + filename, 'r');
    #raw_input("pause");
    #print fid
    line_num = 0;
    info_flag = 0;
    num_r = 0;
    num_c = 0;
    num_nz = 0;

    nzlist = list();

    while 1:
        line = fid.readline();
        line_num += 1;
        #print "line #" + str(line_num);
        if (not line) or line.isspace():
            print line;
            print "Reached end of file"
            break;
        elif line.startswith("%"):
            print line;
            print "This line starts with %, will skip"
            continue;
        elif (not info_flag):
            print line
            info_flag = 1
            ele = line.split()
            num_r = ele[0]
            num_c = ele[1]
            num_nz = ele[2]
        else:
            #print "New nz"
            ele = line.split()
            ientry = entry()
            ientry.r_idx = ele[0]
            ientry.c_idx = ele[1]
            ientry.value = ele[2]
            nzlist.append(ientry)

    print "The length of nz list is " + str(len(nzlist))

    # hyper edge list
    helist = [[] for i in range(int(num_c)+1)]

    for nz in nzlist:
        #print nz.r_idx + " " + nz.c_idx
        helist[int(nz.c_idx)].append(nz.r_idx);
        #print "The length of hyper edge " + str(nz.c_idx) + " is " + str(len(helist[int(nz.c_idx)]))
        #raw_input("pause");

    print "The length of hyper edge list is " + str(len(helist))

    #raw_input("pause");

    hg_filename = filename + ".hg"
    hg_filepath = "../graphfile/"
    fid_hg = open(hg_filepath + hg_filename, "w");

    num_he = 0
    num_vertex = num_r

    # because the first element in hyper edge list is always empty
    for he in helist:
        if len(he) > 0:
            num_he += 1

    fid_hg.write(str(num_he));

    fid_hg.write(" ");
    fid_hg.write(str(num_vertex));
    fid_hg.write("\n");

    for hedge in helist:
        if len(hedge) == 0:
            continue;
        #print "This hyper edge's length is " + str(len(hedge))
        for vertex in hedge:
            #print vertex
            fid_hg.write(str(vertex) + " ")
        fid_hg.write("\n")




