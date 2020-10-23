vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
graphs = (vertexList, edgeList)

def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex

print(dfs(graphs, 0))


X = [((4, 2), 'East', 1), ((2, 2), 'West', 1)]
st = list()

[st.append(x) for x in X]

current = st.pop()
layers = {(5, 5): 0, (5, 4): 1, (4, 5): 1, (3, 5): 2, (2, 5): 3, (1, 5): 4, (1, 4): 5, (1, 3): 6, (2, 3): 7, (2, 2): 8, (2, 1): 9, (3, 2): 9, (4, 2): 10, (4, 3): 11, (5, 3): 12, (1, 1): 13}


direction = {(5, 5): 0, (5, 4): 'South', (4, 5): 'West', (3, 5): 'West', (2, 5): 'West', (1, 5): 'West', (1, 4): 'South', (1, 3): 'South', (2, 3): 'East', (2, 2): 'South', (2, 1): 'South', (3, 2): 'East', (4, 2): 'East', (4, 3): 'North', (5, 3): 'East', (1, 1): 'West'}
goal_state: (1, 1)
layers: {(5, 5): 0, (5, 4): 1, (4, 5): 1, (3, 5): 2, (2, 5): 3, (1, 5): 4, (1, 4): 5, (1, 3): 6, (2, 3): 7, (2, 2): 8, (2, 1): 9, (3, 2): 9, (4, 2): 10, (4, 3): 11, (5, 3): 12, (1, 1): 13}
path_to_goal = [(5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (5, 3), (1, 1)]
[direction[path_to_goal[i]] for i in range(len(path_to_goal))]




path_to_goal=  [(((5, 5), 'NA', 0), 0),

                (((5, 4), 'South', 1), 1),      # ***
                (((4, 5), 'West', 1), 1),       # ***

                (((3, 5), 'West', 1), 2),       # ***
                (((2, 5), 'West', 1), 3),       # ***
                (((1, 5), 'West', 1), 4),       # ***
                (((1, 4), 'South', 1), 5),      # ***
                (((1, 3), 'South', 1), 6),      # ***
                (((2, 3), 'East', 1), 7),       # ***
                (((2, 2), 'South', 1), 8),      # ***

                (((2, 1), 'South', 1), 9),      # *** GIVEN AWAY BY REPEAT!
                (((3, 2), 'East', 1), 9),

                (((4, 2), 'East', 1), 10),
                (((4, 3), 'North', 1), 11),
                (((5, 3), 'East', 1), 12),
                (((5, 4), 'North', 1), 13),

                (((1, 1), 'West', 1), 15)]      # ***

problem_visitedlist = [(5, 5),
                       (4, 5),
                       (3, 5),
                       (2, 5),
                       (1, 5),
                       (1, 4),
                       (1, 3),

                       (2, 3),
                       (2, 2),

                       (3, 2),
                       (4, 2),
                       (4, 3),
                       (5, 3),
                       (5, 4), #** NA JUMP POINTS

                       (2, 1),
                       (1, 1), (1, 1)]

final_path = []

max_depth = max([i[1] for i in path_to_goal])
print('max_depth', max_depth)



for i in range(max_depth+1):
    sub = [x for x in path_to_goal if x[1] == i]
    if not not sub:
        #print('sub', sub)
        if len(sub) > 1:
            # backtrack to prior node

            final_path.append(sub[-1][0][1])

        else:
            final_path.append(sub[0][0][1])


22[0]


path_to_goal

visited = problem_visitedlist
visited.reverse()


test = [1,2,3,4]
if 1 in test:
    print('index', test.index(1))

v1 = [1,2,3,4]
v2 = v1.copy()
v2.reverse()
v2
v1




final_path = [(((6, 1), [(1, 1), (1, 6), (6, 6), (6, 1)]), 'East', 1)]



final_path[-1][0][0]
[i for i in final_path[-1][0][1] if i != final_path[-1][0][0]]

neigh = [((5, 1), [(1, 1), (1, 6), (6, 6), (6, 1)])]


[i[0] for i in neigh]

xx = [(((4, 5), []), 0, 0), (((3, 5), []), 'West', 1), (((2, 5), []), 'West', 1), (((1, 5), []), 'West', 1), (((1, 4), []), 'South', 1), (((1, 3), []), 'South', 1), (((1, 2), []), 'South', 1), (((1, 1), [(1, 1)]), 'South', 1), (((1, 2), [(1, 1)]), 'North', 1), (((1, 3), [(1, 1)]), 'North', 1), (((1, 4), [(1, 1)]), 'North', 1), (((1, 5), [(1, 1)]), 'North', 1), (((1, 6), [(1, 1), (1, 6)]), 'North', 1), (((2, 6), [(1, 1), (1, 6)]), 'East', 1), (((3, 6), [(1, 1), (1, 6)]), 'East', 1), (((4, 6), [(1, 1), (1, 6)]), 'East', 1), (((5, 6), [(1, 1), (1, 6)]), 'East', 1), (((6, 6), [(1, 1), (1, 6), (6, 6)]), 'East', 1), (((6, 5), [(1, 1), (1, 6), (6, 6)]), 'South', 1), (((6, 4), [(1, 1), (1, 6), (6, 6)]), 'South', 1), (((6, 3), [(1, 1), (1, 6), (6, 6)]), 'South', 1), (((5, 3), [(1, 1), (1, 6), (6, 6)]), 'West', 1), (((4, 3), [(1, 1), (1, 6), (6, 6)]), 'West', 1), (((3, 3), [(1, 1), (1, 6), (6, 6)]), 'West', 1), (((3, 2), [(1, 1), (1, 6), (6, 6)]), 'South', 1), (((3, 1), [(1, 1), (1, 6), (6, 6)]), 'South', 1), (((4, 1), [(1, 1), (1, 6), (6, 6)]), 'East', 1), (((5, 1), [(1, 1), (1, 6), (6, 6)]), 'East', 1), (((6, 1), [(1, 1), (1, 6), (6, 6), (6, 1)]), 'East', 1)]

[x[1] for x in xx]



current_state = (((4, 5), []), 0, 0)


current_state = ((4, 5), 0, 0)
type(current_state[0][0])


[] + ((2,3), (3,2))

cnrs = ((1, 1), (1, 12), (28, 1), (28, 12))
state = ((3, 12), [(1, 1)])


[i for i in state[1]]


remaining_corners = [c for c in cnrs if c not in state[1]]

# closed manhatten distance
corners = ((1, 1), (1, 12), (28, 1), (28, 12))
state = ((5, 8), [(1, 12)])
remaining_corners = [(1, 1), (28, 1), (28, 12)]


distances = [(abs(state[0][0] - i[0]) + abs(state[0][1] - i[1])) for i in remaining_corners]

# ---- nearest corner index ----x
nearest_corner_index = distances.index(min(distances))

# ---- remaining distances -----x
nearest_distance = distances.pop(nearest_corner_index)
nearest_corner = remaining_corners.pop(nearest_corner_index)

# ---- Manhattan distance between nearest corner & other corners ----x
distances_to_remaining_corners = \
    [(abs(nearest_corner[0] - i[0]) + abs(nearest_corner[1] - i[1])) for i in remaining_corners]


# ---- nearest to current node ----

# ---- total Min Manhattan distance from state to all corners ----x
min_distance = sum(distances_to_remaining_corners) + nearest_distance







# -------- recursive ---------x

# closed manhatten distance
corners = ((1, 1), (1, 12), (28, 1), (28, 12))
state = ((5, 8), [(1, 12)])
remaining_corners = [(1, 1), (28, 1), (28, 12)]


cur_state = state[0]
total_distances = []
for s in range(len(remaining_corners)):
    print('s', s)
    print('cur_state', cur_state)
    print('remaining_corners ', remaining_corners)
    distances = [(abs(cur_state[0] - i[0]) + abs(cur_state[1] - i[1])) for i in remaining_corners]

    print('distances ', distances)
    print('remaining_corners, ', remaining_corners)
    # ---- nearest corner index ----x
    nearest_corner_index = distances.index(min(distances))

    # ---- remaining distances -----x
    nearest_distance = distances.pop(nearest_corner_index)
    nearest_corner = remaining_corners.pop(nearest_corner_index)

    # ---- add to nearest distance ----x
    total_distances.append(nearest_distance)

    # ---- update current state & remaining corners (auto updated with .pop()) ----x
    cur_state = nearest_corner
    print('s', s)
    print('distances ', distances)
    print('remaining_corners, ', remaining_corners)

sum(total_distances)


foodGrid2 = [[False,
              False,
              False,
              False,
              False], [False, False, False, True, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]

h=5-1; w=5
for y in range(5):
    for x in range(5):
        xcor = x+1; ycor = y+1
        print('foodGrid: ', foodGrid2[x][abs(y-h)])
        print(xcor,ycor)





[abs(i-4) for i in range(5)]
[print(i) for i in reversed(range(5))]







foodGrid = [[False, False, False, False, False, False, False], [False, True, False, False, True, True, False], [False, True, False, False, False, False, False], [False, True, False, False, False, False, False], [False, True, False, False, True, False, False], [False, True, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, True, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, True, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, True, True, False], [False, False, False, False, False, True, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False]]

height = len(foodGrid[0])
height = 7-1


width = len(foodGrid)
width = 20



# -------- convert to coordinates ---------x
food_location = []
for y in range(height):
    for x in range(width):
        xcor = x+1; ycor = y+1
        coord = (xcor,ycor)
        food = foodGrid[x][abs(y-height)]
        if food:
            # food_location.append((coord, food))
            food_location.append(coord)



# ---- food locations ----x
foodGrid = [(1, 1), (1, 4), (1, 5), (2, 1), (3, 1), (4, 1), (4, 4), (5, 1), (7, 4), (10, 4), (13, 4), (13, 5), (14, 5)]
position = (9, 3)

curr_loc = position
total_dist = 0
for i in range(len(foodGrid)):
    print('----------------------------')
    print('total_dist: ', total_dist)
    # ---- find nearest food ----x
    dists = [(abs(x[0]-curr_loc[0]) + abs(x[1] - curr_loc[1])) for x in foodGrid]
    # index of next item
    next_index = dists.index(min(dists))
    # add to total distance
    total_dist += min(dists)
    curr_loc = foodGrid.pop(next_index)


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x.pop(2)
