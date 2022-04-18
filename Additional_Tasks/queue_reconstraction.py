# You are given an array of people, people, which are the attributes of some people in a queue
# (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi
# with exactly ki other people in front who have a height greater than or equal to hi.
#
# Reconstruct and return the queue that is represented by the input array people.
# The returned queue should be formatted as an array queue, where queue[j] = [hj, kj]
# is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).


def reconstructQueue(people: list[list[int]]) -> list[list[int]]:
    ans = [None for _ in range(len(people))]
    for person in (sorted(people, key=lambda x: (x[0], -x[1]))):
        pos = person[1]
        #print(person)
        i = 0
        while i < len(ans):
            if ans[i] == None:
                if pos == 0:
                    ans[i] = person
                    break
                pos -= 1
            i += 1
        #print(ans)
    return ans

def reconstructQueue2(people: list[list[int]]) -> list[list[int]]:
    ans = []
    #print(*reversed(sorted(people, key=lambda x: (x[0], -x[1]))))
    for h, k in reversed(sorted(people, key=lambda x: (x[0], -x[1]))):
        ans.insert(k, [h, k])
        #print(ans)
    return ans

p = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(p))
print(reconstructQueue2(p))