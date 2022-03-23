visited = []
order = []

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



def sortCourses3(course_list, prerequisites_dict):
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

def sortCourses(course_list, prerequisites_dict):
    course_order = []
    for course in sorted(course_list):
                val = prerequisites_dict.get(course)
                if not val:
                    course_order.append(course)
                else:
                    if course > prerequisites_dict.get(course):
                        course_order.append(course)
    if len(course_order) == 0:
        return -1
    return course_order

if __name__ == "__main__":
    print()
    print("1st case")
    course_list = [0, 1, 2, 3]
    prerequisites_dict = {0: [1, 2], 3: [1, 2]}
    print("first solution:", sortCourses2(course_list, prerequisites_dict))
    print("second solution:", sortCourses3(course_list, prerequisites_dict))
    print("your solution:", sortCourses(course_list, prerequisites_dict))

