# Given a list of courses and a list of prerequisites for each course
# (in a form of a dict) output the list of courses sorted in such a way
# that each course appears in this list only after all it's prerequisites.
# If it is not possible, output -1.
#
# HINT: use the DFS algorithm
visited = []
order = []

def dfs(v, prerequisites_dict):
    global visited, order
    visited[v] = True
    print(visited)
    prerequisites = prerequisites_dict[v] \
        if v in prerequisites_dict else []
    for u in prerequisites:
        if not visited[u]:
            dfs(u, prerequisites_dict)
    order.append(v)
    print(order)



def sortCourses(course_list, prerequisites_dict):
    global visited, order
    order = []
    n = len(course_list)
    course_order = []
    visited = [False for _ in range(n)]
    for course in course_list:
        if not visited[course]:
            print("run dfs:", course)
            dfs(course, prerequisites_dict)
    course_order = order
    if len(course_order) == 0:
        return -1
    return course_order


course_list = [0, 1, 2]
prerequisites_dict = {2: [1], 1: [0]}
# check that your code works correctly on provided example
assert sortCourses(course_list, prerequisites_dict) == [0, 1, 2], 'Wrong answer'

print("second case")
course_list = [0, 1, 2]
prerequisites_dict = {2 : [1, 2], 1: [0, 2], 0: [1, 2]}
print("ans:",sortCourses(course_list, prerequisites_dict))

print("third case")
course_list = [0, 1, 2]
prerequisites_dict = {0: [0,1,2], 1: [0,1,2], 2:[0,1,2]}
print("ans:",sortCourses(course_list, prerequisites_dict))