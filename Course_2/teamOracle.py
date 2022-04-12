# You were tasked with designing a team oracle. It is an oracle, that given a size of a team,
# and a list of tasks with their start and finishing times, determines if those tasks can be performed
# by this team without them overlapping. Each member of a team can only work on one task at a time.
import heapq

def teamOracle(team_size, start_times, finish_times):
    can_do = True
    team_free = [0]
    tasks = sorted(zip(start_times, finish_times), key=lambda x: (x[0], x[1]))
    heapq.heapify(team_free)
    for task_start, task_end in tasks:
        if team_free[0] <= task_start:
            heapq.heapreplace(team_free, task_end)
        else:
            heapq.heappush(team_free, task_end)
            if len(team_free) > team_size:
                return False


    return can_do

if __name__ == "__main__":
    team_size = 4
    start_times = [1, 5, 10]
    finish_times = [3, 7, 15]
    # check that your code works correctly on provided example
    assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'

    team_size = 1
    start_times = [11, 11, 10]
    finish_times = [13, 12, 15]
    # check that your code works correctly on provided example
    assert not teamOracle(team_size, start_times, finish_times), 'Wrong answer'

    team_size = 2
    start_times = [11, 11, 10]
    finish_times = [13, 12, 11]
    # check that your code works correctly on provided example
    assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'

    team_size = 2
    start_times = [11, 11, 11]
    finish_times = [13, 12, 12]
    # check that your code works correctly on provided example
    assert not teamOracle(team_size, start_times, finish_times), 'Wrong answer'