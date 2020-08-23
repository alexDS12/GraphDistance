import networkx as nx

def show_distance(graph, start, end):
    #Check if start isn't the end neither start nor end aren't in graph
    if start is not end and (start in graph and end in graph):
        #Get every path from source to target
        paths = list(nx.all_simple_paths(graph, source=start, target=end))
        #Print paths and sum their weight
        for path in paths:
            print(path)
            path_sum = 0
            for i in range(len(path) - 1):
                path_sum += graph[path[i]][path[i+1]]['weight']
                #Check if it's the antepenult element (to print distance)
                if(i == (len(path) - 2)):
                    print("distance: {}".format(path_sum))

def main():
    graph_dict = {
            'A':['B', 'C', 'D', 'E', 'F'],
            'B':['A', 'C', 'D', 'E', 'F'],
            'C':['A', 'B', 'D', 'E', 'F'],
            'D':['A', 'B', 'C', 'E', 'F'],
            'E':['A', 'B', 'C', 'D', 'F'],
            'F':['A', 'B', 'C', 'D', 'E']
            }

    #Create a nx graph object
    graph = nx.Graph()
    #Populate the nx graph with a dictionary of paths
    graph = nx.DiGraph(graph_dict)
    place_weights(graph)
    
    start = (input("Point of beginning: ")).upper()
    end = (input("Point of ending: ")).upper()

    show_distance(graph, start, end)

if __name__ == '__main__':
    main()
