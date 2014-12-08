from itertools import permutations


def totalprobability(T):  
    r = 1
    for _,p in T:
        r *= p
    return r   

def totaltime(T):  
    if len(T) == 0:
        return 0
    t, p = T[0]
    if len(T) == 1:
        return t
    return t + p * totaltime(T[1:])

def remlist(L, i):
    temp = list(L)
    del temp[i]
    return temp

def solve_naive(T):
    mintime = 10000
    for order in permutations(T):                
        t = totaltime(order)
        if mintime > t:
            mintime = t
            best_order = order
    return mintime

def recursive(T, i):
    print T, i
    t, p = T[i]
    l = len(T)
    if l == 1:
        return t
    smaller = remlist(T,i)
    mintime = 10000
    for j in range(len(smaller)):
        subprob = recursive(smaller, j) 
        print smaller, j, subprob
        if mintime > subprob:
            mintime = subprob
    return t+p * mintime

def solve_recursive(T):
    return min([ recursive(T,i) for i in range(len(T))])

def insert_task(task, T):
    #print T
    t, p = task
    #print t, p
    best_time = 10000
    best_idx = 0
    for i in range(len(T)+1):
        #print totaltime(T[:i]), totalprobability(T[:i]), t, p,  totaltime(T[i:])
        current_time = totaltime(T[:i]) + \
        totalprobability(T[:i]) * (t + p * totaltime(T[i:]))
        if current_time < best_time:
            best_time = current_time
            best_idx = i
    result = T[:best_idx] + [task] + T[best_idx:]
    #print result
    return result

def solve_dp(T):
    P =[]
    for e in T:
        P = insert_task(e, P)
    return totaltime(P)
    
    #print M

def summerize(T):
    n = len(T)
    print T
    if n == 1:        
        return T    
    max_product = 0
    for i in range(n-1):
        t1, p1 = T[i]
        for j in range(i+1,n):            
            (t2, p2) = T[j]            
            val = min([t1 + p1 * t2, t2 + p2 * t1])
            if val > max_product:
                max_product = val
                max_idx1, max_idx2 = i, j            

    print T[max_idx1], T[max_idx2]
    replacement = (max_product, T[max_idx1][1] * T[max_idx2][1])
    del_first, del_second = max([max_idx1, max_idx2]), min([max_idx1, max_idx2])
    del T[del_first]
    del T[del_second]
    T += [replacement]
    return summerize(T)

def halve(T):
    n = len(T)
    halved_lists = []
    #print T
    if n == 1:        
        return T    
    for i in range(n):
        halved_list = []
        (t1, p1) = T[i]
        for j in range(n):            
            if j == i:
                continue
            (t2, p2) = T[j]            
            halved_list += [(t1+p1*t2, p1*p2)]
        halved_lists += halve(halved_list)                
    return halved_lists

def solve_dp_exp(T):
    """ solve the problem by replacement """
    Tcopy = list(T)
    return summerize(Tcopy)[0][0]

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
