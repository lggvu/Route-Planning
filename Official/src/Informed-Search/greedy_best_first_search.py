import queue
import time
import numpy as np
import pandas as pd
from random import randint
import copy


class Node:
    def __init__(self, name, h=0, g=0,par=None):
        self.name = name
        self.h = h
        self.g = g
        self.par=par

    def __lt__(self, other):
        if other == None:
            return False
        return self.h < other.h

    # def __eq__(self, other):
    #     if other == None:
    #         return False
    #     return self.name == other.name

class Graph:
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict
        self.Path=[]

    def neighbors(self, v):
        return self.graph_dict[v]

    def h(self, n):
        return heuristic[n]

    def getPath(self, node):
        if node.par != None:
            self.getPath(node.par)
            self.Path.append(node.name)

    def BestFirst_Search(self,start, stop):

        Open = queue.PriorityQueue()
        Closed = queue.PriorityQueue()

        Open.put( Node(start) )

        while True:
            if Open.empty() == True:
                print('Can not found!')
                return []

            node = Open.get() # current node
            Closed.put(node)

            if node.name == stop:
                print('\nSuccessfull! The solution of Greedy Best-First-Search algorithm is:')
                print('Total cost: {}'.format(node.g))
                self.getPath(node)

                return self.Path

            for (child, cost) in self.graph_dict[node.name]:
                g = node.g + cost
                h = heuristic[child]

                tmp = Node(name=child, h=h, g=g)

                if (tmp not in Open.queue) and (tmp not in Closed.queue):
                    tmp.par= node

                    Open.put(tmp)



def Input():
    global start
    global  destination

    start = 'HaNoi'
    destination = 'HoChiMinh'

def ToGraph():

    global cities_lst
    global map
    global heuristic
    global label
    global data1

    # travelling cost between adjacent cities
    df = pd.read_csv('../data/route-info.csv')
    highway_data = df.to_numpy()
    df1 = pd.read_csv('../data/air-info.csv')
    flight_fee = df1.to_numpy()
    fee = highway_data[:, 2:3] * 1500 + highway_data[:, 3:4] * 1000
    highway_fee = np.hstack((highway_data[:, :2], fee))

    final_fee = highway_fee
    final_fee = np.vstack((final_fee, flight_fee))

    map = dict()
    for i in final_fee:
        map[i[0]] = map.get(i[0], [])
        map[i[0]].append((i[1], i[2]))
        map[i[1]] = map.get(i[1], [])
        map[i[1]].append((i[0], i[2]))

    cities_lst = map.keys()

    # getting heuristics data
    df2 = pd.read_csv(
        '../data/city-label.csv',
        header=None)
    da = df2.to_numpy()
    da = da.reshape((2, -1))
    label = dict()
    da = list(da)
    for i in range(len(da[0])):
        label[da[0][i]] = i
    df1 = pd.read_csv(
        '../data/heuristics.csv',
        header=None)
    data1 = df1.to_numpy()



def Solver(): # for a single test with input
    solver = Graph(map)
    path = solver.BestFirst_Search(start, destination)
    print(*path, sep=' --> ')

def Test():
    # randomise 50 different instances
    count = 0
    cities_test = copy.deepcopy(list(cities_lst))
    time_lst = []  # list of running time for analysis
    while count < 10:
        start_indx = randint(0, 31)
        end_indx = randint(0, 31)
        if start_indx == end_indx:
            continue
        start_test = cities_test[start_indx]
        end_test = cities_test[end_indx]
        Heuristic(start_test,end_test)
        print(f'Test {count + 1}: {cities_test[start_indx]} -> {cities_test[end_indx]}')

        start_time = time.time()
        solver = Graph(map)
        path = solver.BestFirst_Search(start_test, end_test)
        print('Number of nodes:', len(path))
        print(*path, sep=' --> ')
        end_time = time.time()
        time_lst.append(end_time - start_time)
        print('Total execution time:', end_time - start_time)
        count += 1
def Heuristic(start,destination):
    global heuristic
    def find_heuristic(start, destination):
        if destination not in cities_lst:
            raise Exception("this city is not included in the map")
        data3 = []
        index = label[destination]
        for i in label:
            data3.append([i, data1[index, label[i]]])
        return data3
    data4 = find_heuristic(start, destination)
    heuristic = dict()
    for i in data4:
        heuristic[i[0]] = heuristic.get(i[0], 0) + float(i[1] * 1500)

# Input()
ToGraph()
# Heuristic(start,destination)
# Solver()
Test()