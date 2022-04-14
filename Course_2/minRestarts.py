# There is a faulty server, that can work without restarting no longer than t minutes.
# Restarting a server takes exactly 1 minute. You're given a list of times when there will
# be no requests to the server for a minute in the form of integers representing difference
# between no-request start time and current time, sorted increasingly from the current moment.
#
# You should output the minimum time of restarts needed for server to work for m minutes starting from now.
# If the server would have to restart when there are requests sent to it, output -1 instead.

def minRestarts(m, t, no_request_times):
    min_restarts = 0
    cur_time = 0
    server_run_time = 0
    if no_request_times[0] <= t:
        cur_time = no_request_times[0]
        server_run_time = no_request_times[0]
        if cur_time + t - server_run_time >= m:
            return min_restarts
        elif cur_time + t + 1 >= m:
            return min_restarts + 1
    else:
        return -1
    for pause_time in no_request_times[1:]:
        if min(pause_time - cur_time, m) > t + 1:
            return -1
        elif min(pause_time - cur_time - 1, m) <= t - server_run_time - 1:
            server_run_time += pause_time - cur_time
            cur_time = pause_time
        else:
            server_run_time = pause_time - cur_time - 1
            cur_time = pause_time
            min_restarts += 1
        if cur_time + t - server_run_time >= m:
            return min_restarts
        elif cur_time + t + 1 >= m:
            return min_restarts + 1
    return -1

if __name__ == "__main__":
    m = 100
    t = 20
    no_request_times = [50]
    # check that your code works correctly on provided example
    assert minRestarts(m, t, no_request_times) == -1, 'Wrong answer'

    m = 100
    t = 20
    no_request_times = [20, 41, 62, 83]
    # check that your code works correctly on provided example
    print()
    print("second case:")
    print(minRestarts(m, t, no_request_times))
    assert minRestarts(m, t, no_request_times) == 4, 'Wrong answer'

    m = 105
    t = 20
    no_request_times = [20, 41, 62, 83]
    # check that your code works correctly on provided example
    print()
    print("second case:")
    print(minRestarts(m, t, no_request_times))
    assert minRestarts(m, t, no_request_times) == -1, 'Wrong answer'


    m =100
    t = 50
    no_request_times = [50]
    print()
    print("second case:")
    print(minRestarts(m, t, no_request_times))
    assert minRestarts(m, t, no_request_times) == 1, 'Wrong answer'