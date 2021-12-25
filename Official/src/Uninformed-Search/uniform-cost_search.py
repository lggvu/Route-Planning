import pandas as pd
import  numpy as np
import queue
import time
import random

class Graph:
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict
        self.path = []

    def neighbors(self, v):
        return self.graph_dict[v]

    def find_par(self, node):
        if node in par:
            self.find_par(par[node])
            self.path.append(node)
            # print(x,end=' ')

    def Uniform_cost_search(self, start, end):

        global par

        par=dict()
        visited=dict()

        frontier=queue.PriorityQueue()
        frontier.put( ( 0, start , -1, 1 ) ) # path_cost, current node, previous node, number of nodes in path
        par[start]=-1  # parent of node, -1 means start is root

        while frontier.qsize():

            ( path_cost , node , prev_node , number_of_nodes ) = frontier.get()

            if node in visited:
                continue

            visited[node]=1
            par[node]=prev_node

            if node == end: # print answer
                print('Cost:',path_cost)
                print('Numbers of nodes:',number_of_nodes)
                self.find_par(end) # get path
                return self.path

            for (next_node,cost) in self.graph_dict[node]:

                if next_node in visited:
                    continue

                frontier.put( ( path_cost+cost , next_node, node, number_of_nodes +1 ) )
        return 'Failture'

def toGraph(): # csv to graph

    df = pd.read_csv('C:\\Users\Helo\Downloads\\route-planning-main\\route-planning-main\Official\src\data\\route-info.csv')
    data = df.to_numpy()
    df1 = pd.read_csv('C:\\Users\Helo\Downloads\\route-planning-main\\route-planning-main\Official\src\data\\air-info.csv')
    data1 = df1.to_numpy()
    highway_data = data
    flight_fee = data1
    fee = highway_data[:, 2:3] * 1500 + highway_data[:, 3:4] * 1000
    highway_fee = np.hstack((highway_data[:, :2], fee))

    final_fee = highway_fee
    final_fee = np.vstack((final_fee, flight_fee))
    global map
    map = dict() #graph
    for i in final_fee:
        map[i[0]] = map.get(i[0], [])
        map[i[0]].append((i[1], i[2]))
        map[i[1]] = map.get(i[1], [])
        map[i[1]].append((i[0], i[2]))

def Test():

    count = 0
    # cities_test = copy.deepcopy(list(cities_lst))
    while count < 50:
        start_test = random.choice(list(map.keys()))
        end_test = random.choice(list(map.keys()))
        if start_test == end_test:
            break
        start_time = time.time()
        solver = Graph(map)
        path = solver.Uniform_cost_search(start_test, end_test)
        print(*path, sep=' --> ')
        end_time = time.time()
        print('Total execution time:', end_time - start_time)
        count += 1

toGraph()
Test()
