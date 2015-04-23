#!/usr/bin/python2.7

# turn a partional result (group index for each vertex) into the order of vertices
# a hype-graph modeling of matrix
# views each row as a vertex
# views each column as a hyper edge

import os
from os import listdir
filepath = "../graphfile/"
filelist = os.listdir(filepath)
num_parts = 4

for filename in filelist:
    if not filename.endswith(str(num_parts)):
        continue
    print "Processing " + filename
    fid = open(filepath + filename, 'r')

    orderlist = [[] for i in range(num_parts)]

    num_line = 0
    while 1:
        group = fid.readline()
        num_line += 1
        if not group:
            break
        orderlist[int(group)].append(str(num_line))


    outfilepath = "../vertex_order/"
    outfilename = filename + ".order"
    outfid = open(outfilepath + outfilename, 'w')
    print "Writing to file " + outfilepath + outfilename

    for group in orderlist:
        for vertex in group:
            outfid.write(str(vertex))
            outfid.write('\n')




