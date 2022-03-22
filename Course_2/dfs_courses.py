# Given a list of courses and a list of prerequisites for each course
# (in a form of a dict) output the list of courses sorted in such a way
# that each course appears in this list only after all it's prerequisites.
# If it is not possible, output -1.
#
# HINT: use the DFS algorithm
visited = []
order = []


def iterativeDFS(adjList, v, discovered):
    path = []
    stack = []
    stack.append(v)

    while len(stack) > 0:
        v = stack.pop()
        if discovered[v]:
            continue
        discovered[v] = True
        #print(v, end=' ')
        path.append(v)
        neighbours = adjList[v]
        for u in neighbours:
            if not discovered[u]:
                stack.append(u)
    return path


def sortCourses2(course_list, prerequisites_dict):
    n = len(course_list)
    course_order = []
    adjacency_list = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for key in prerequisites_dict.keys():
        for prerequisite in prerequisites_dict[key]:
            adjacency_list[prerequisite].append(key)
    #print("adj_list:", adjacency_list)
    for edge in course_list:
        if not visited[edge]:
            cur_path = iterativeDFS(adjacency_list, edge, visited)[::-1]
            #print("cur_path:", cur_path)
            for visited_edge in cur_path:
                visited[visited_edge] = True
            course_order.extend(cur_path)

    if len(course_order) == 0:
        return -1
    return course_order[::-1]

def dfs(v, prerequisites_dict):
    global visited, order
    visited[v] = True
    #print(visited)
    prerequisites = prerequisites_dict[v] \
        if v in prerequisites_dict else []
    for u in prerequisites:
        if not visited[u]:
            dfs(u, prerequisites_dict)
    order.append(v)
    #print(order)



def sortCourses(course_list, prerequisites_dict):
    global visited, order
    order = []
    n = len(course_list)
    course_order = []
    visited = [False for _ in range(n)]
    for course in course_list:
        if not visited[course]:
            #print("run dfs:", course)
            dfs(course, prerequisites_dict)
    course_order = order
    if len(course_order) == 0:
        return -1
    return course_order

print("1st case")
course_list = [0, 1, 2]
prerequisites_dict = {2: [1], 1: [0]}
# check that your code works correctly on provided example
assert sortCourses(course_list, prerequisites_dict) == [0, 1, 2], 'Wrong answer'
assert sortCourses2(course_list, prerequisites_dict) == [0, 1, 2], 'Wrong answer'
print("ans11:",sortCourses(course_list, prerequisites_dict))
print("ans12:",sortCourses2(course_list, prerequisites_dict))

print()
print("2nd case")
course_list = [0, 1, 2]
prerequisites_dict = {0 : [1], 2: [1]}
print("ans21:",sortCourses(course_list, prerequisites_dict))
print("ans22:",sortCourses2(course_list, prerequisites_dict))

print()
print("3rd case")
course_list = [0, 1, 2, 3]
prerequisites_dict = {1: [0, 2], 3: [1]}
print("ans:",sortCourses(course_list, prerequisites_dict))
print("ans:",sortCourses2(course_list, prerequisites_dict))

print()
print("4th case")
course_list = [0, 1, 2, 3, 4, 5]
prerequisites_dict = {0: [2], 1: [3, 0], 2: [3], 5: [4, 3]}
print("ans41:",sortCourses(course_list, prerequisites_dict))
print("ans42:",sortCourses2(course_list, prerequisites_dict))

print()
print("5th case")
course_list = []
prerequisites_dict = {}
print("ans41:",sortCourses(course_list, prerequisites_dict))
print("ans42:",sortCourses2(course_list, prerequisites_dict))