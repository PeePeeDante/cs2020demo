import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def evaluateCluster(): # cannot have same method name 
    data = request.get_data()
    graph = json.loads(data)
    logging.info("data sent for evaluation {}".format(graph))
    #inputValue = data.get("input");
    
    mark = []
    for i in range(len(graph)):
        mark.append([False]*len(graph[0]))

    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if (graph[i][j] == '1' and mark[i][j]==False):
                mark = dfs([i,j], graph, mark, "1")
                count+=1

    #logging.info("My mark: {}".format(mark))
    answer = {"answer":count}
    logging.info("My result: {}".format(answer))
    return jsonify(answer)

def neighbor(v,graph):
    adj0 = []
    adj1 = []
    i = v[0]
    j = v[1]

    if (i-1 >= 0):
        if(graph[i-1][j] == "0"):
            adj0.append((i-1, j))
        elif(graph[i-1][j] == "1"):
            adj1.append((i-1, j))
        if (j-1 >= 0):
            if(graph[i-1][j-1] == "0"):
                adj0.append((i-1, j-1))
            elif(graph[i-1][j-1] == "1"):
                adj1.append((i-1, j-1))
        if (j+1 < len(graph[0])):
            if(graph[i-1][j+1] == "0"):
                adj0.append((i-1, j+1))
            elif(graph[i-1][j+1] == "1"):
                adj1.append((i-1, j+1))

    
    if (i+1 < len(graph)):
        if(graph[i+1][j] == "0"):
            adj0.append((i+1, j))
        elif(graph[i+1][j] == "1"):
            adj1.append((i+1, j))
        if (j-1 >= 0):
            if(graph[i+1][j-1] == "0"):
                adj0.append((i+1, j-1))
            elif(graph[i+1][j-1] == "1"):
                adj1.append((i+1, j-1))
        if (j+1< len(graph[0])):
            if(graph[i+1][j+1] == "0"):
                adj0.append((i+1, j+1))
            elif(graph[i+1][j+1] == "1"):
                adj1.append((i+1, j+1))
            
    if(j-1>=0):
        if(graph[i][j-1] == "0"):
            adj0.append((i, j-1))
        elif(graph[i][j-1] == "1"):
            adj1.append((i, j-1))
            
    if(j+1<len(graph[0])):
        if(graph[i][j+1] == "0"):
            adj0.append((i, j+1))
        elif(graph[i][j+1] == "1"):
            adj1.append((i, j+1))
    logging.info("ADJS:({},{})".format(adj0, adj1))
    return adj0,adj1

def dfs(u, graph, mark, T):
    mark[u[0]][u[1]] = True
    logging.info("My mark:{},{} {}".format(u[0],u[1],mark))
    adj0, adj1 = neighbor(u, graph)

    
    for v in adj0:
        if (mark[v[0]][v[1]]==False):
            mark = dfs(v, graph, mark, "0")

    for v in adj1:
        if (mark[v[0]][v[1]] == False):
            mark = dfs(v, graph, mark, "1")
    
    return mark

