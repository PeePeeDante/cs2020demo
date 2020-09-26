import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/contact_trace', methods=['POST'])
def evaluateTrace(): # cannot have same method name 
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");

    infect_n = data["infected"]["name"]
    infect_g = data["infected"]["genome"]

    paths = []

    child_list = []
    child_list.append(data["origin"])
    for clu in data["cluster"]:
        child_list.append(clu)

    paths += back_track(data["infected"], child_list)

    logging.info("My result: {}".format(paths))
    return paths

def addToPath():
    

def back_track(parent, child_list, cum_path):
    path = []

    if (child_list==[]):
        

    m_index = []
    d_list = []
    sil_list = []
    for i in range(len(child_list)):
        d, s = difference(child_list[i])
        d_list.append(d)
        sil_list.append(s)

    min_diff = min(d_list)

    # find index of possible trace routes
    while min_diff in d_list:
        m_index.append(d_list.index(min_diff))
        d_list[d_list.index(min_diff)]+=1
    
    for index in m_index:
        # origin
        if (index == 0):
            path.append(cum_path)
            return += pat
            path = path_list.append([child_list[index],sil_list[index]])
            continue

        p = child_list[index]
        temp = child_list
        temp.pop(index)
        path_list.append([child_list[index], sil_list[index]])
        path += back_track(p,temp,path_list)

    return path

def difference(g1,g2):
    score = 0
    head_count = 0
    silent = 1

    for i in range(len(g1)):
        if (g1[i]!=g2[i]):
            score += 1
            if (i%3==0):
                head_count+=1

    if (head_count>1):
        silent = 0

    return score, silent

        






