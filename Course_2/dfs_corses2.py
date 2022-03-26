def sortCourses(course_list, prerequisites_dict):
    n = len(course_list)
    course_order = []
    visited = [False for _ in range(n)]
    for course in range(n):
        if not visited[course]:
            cur_path = []
            stack = []
            stack.append(course)
            visited[course] = True
            while len(stack) > 0:
                cur_course = stack.pop()
                cur_path.append(cur_course)
                neighbours = prerequisites_dict[cur_course] \
                    if cur_course in prerequisites_dict else []
                for neighbour in neighbours:
                    if not visited[neighbour]:
                        stack.append(neighbour)
                        visited[neighbour] = True
            course_order.extend(cur_path[::-1])


    if len(course_order) == 0:
        return -1
    return course_order

if __name__ == "__main__":
    print("1st case")
    course_list = [0, 1, 2]
    prerequisites_dict = {2: [1], 1: [0]}
    # check that your code works correctly on provided example
    assert sortCourses(course_list, prerequisites_dict) == [0, 1, 2], 'Wrong answer'
    print("ans11:", sortCourses(course_list, prerequisites_dict))


    print()
    print("2nd case")
    course_list = [0, 1, 2]
    prerequisites_dict = {0: [1], 2: [1]}
    print("ans21:", sortCourses(course_list, prerequisites_dict))

    print()
    print("3rd case")
    course_list = [0, 1, 2, 3]
    prerequisites_dict = {1: [0, 2], 3: [1]}
    print("ans:", sortCourses(course_list, prerequisites_dict))

    print()
    print("4th case")
    course_list = [0, 1, 2, 3, 4, 5]
    prerequisites_dict = {0: [2], 1: [3, 0], 2: [3], 5: [4, 3]}
    assert sortCourses(course_list, prerequisites_dict) == [3, 2, 0, 1, 4, 5], 'Wrong answer'

    print()
    print("5th case")
    course_list = []
    prerequisites_dict = {}
    assert sortCourses(course_list, prerequisites_dict) == -1, 'Wrong answer'

    print()
    print("6th case")
    course_list = [0, 1, 2, 3]
    prerequisites_dict = {0: [1], 2: [3], 3: [1]}
    print(sortCourses(course_list, prerequisites_dict))
    assert sortCourses(course_list, prerequisites_dict) == [1, 0, 3, 2], 'Wrong answer'

    print()
    print("6th case")
    course_list = [0, 1, 2, 3]
    prerequisites_dict = {0: [1], 3: [2]}
    print(sortCourses(course_list, prerequisites_dict))
    assert sortCourses(course_list, prerequisites_dict) == [1, 0, 2, 3], 'Wrong answer'
