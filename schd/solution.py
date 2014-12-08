def totalprobability(tasks):  
    """ Calculate overal probability of a set of tasks """
    r = 1
    for _,p in tasks:
        r *= p
    return r   

def totaltime(tasks):  
    """ Calculate total time of a sequence of tasks """
    r = 0
    for t, p in reversed(tasks):
        r = t + p * r
    return r

def insert_task(task, T):
    t, p = task
    best_time = 10001
    best_idx = 0
    for i in range(len(T)+1):
        current_time = totaltime(T[:i]) + \
        totalprobability(T[:i]) * (t + p * totaltime(T[i:]))
        if current_time < best_time:
            best_time = current_time
            best_idx = i
    return T[:best_idx] + [task] + T[best_idx:]

def solve_dp(T):
    """ Solve the problem using dynamic programming """
    ordered_list =[]
    for e in T:
        ordered_list = insert_task(e, ordered_list)
    return totaltime(ordered_list)

def read_input():
    """ Reads input """
    N = int(raw_input())
    tasks = []
    for n in range(N):
        s = raw_input().split()
        tasks += [(int(s[0]), float(s[1]))]
    return tasks

def main():
    tasks = read_input()
    print solve_dp(tasks)

if __name__ == "__main__":
    main()
