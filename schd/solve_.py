from itertools import permutations


def totalprobability(T):  
    r = 1
    for _,p in T:
        r *= p
    return r   

def totaltime(T):  
    r = 0
    for t, p in T.reverse():
        r = t + p * r
    return r

def insert_task(task, T):
    t, p = task
    best_time = 10000
    best_idx = 0
    for i in range(len(T)+1):
        current_time = totaltime(T[:i]) + \
        totalprobability(T[:i]) * (t + p * totaltime(T[i:]))
        if current_time < best_time:
            best_time = current_time
            best_idx = i
    return T[:best_idx] + [task] + T[best_idx:]

def solve_dp(T):
    P =[]
    for e in T:
        P = insert_task(e, P)
    return totaltime(P)

def read_input():
    N = int(raw_input())
    tasks = []
    for n in range(N):
        s = raw_input().split()
        tasks += [(int(s[0]), float(s[1]))]
    return tasks

def main():
    
    #tasks = [(37, 0.01), (41, 0.33), (81, 0.95), (91, 0.5), (4, 0.64)]
    tasks = [(3, 0.1), (7, 0.5), (9, 0.2)]
    print tasks
    #solution = halve(tasks)
    #print len(solution), min(solution)

    #print solve_naive(tasks)
    #print recursive(tasks, 0)
    #print "-----"
    #print totalprobability(tasks)
    #print insert_task((9, 0.2), tasks)
    print solve_dp(tasks)

if __name__ == "__main__":
    main()
