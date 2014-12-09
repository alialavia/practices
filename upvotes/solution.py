""" 
5 3
1 2 3 4 1 1 8  
0 1 2 3 0 1 2

"""
def D(N):
    return (N*(N+1))/2
def dp(N, K, List):
    R = []
    increasing, decreasing = [0]*N, [0]*N
    window_decreasing, window_increasing = [], []

    for i in range(1, N):
        if List[i] >= List[i-1]:
            increasing[i] = increasing[i-1] + 1        
        else:
            #window_increasing[i-1] = D(increasing[i-1])
            increasing[i] = 0

        if List[i] <= List[i-1]:
            decreasing[i] = decreasing[i-1] + 1
        else:
            #window_decreasing[i-1] = D(decreasing[i-1])
            decreasing[i] = 0
        #R += [window_increasing - window_decreasing]
    print increasing, decreasing
    window_increasing = map(D, increasing)
    window_decreasing = map(D, decreasing)

    print window_increasing, window_decreasing

    #for i in range(K-1, N):
    #    window_increasing = increasing[i]-increasing[i-(K-1)]
    #    window_decreasing = decreasing[i]-decreasing[i-(K-1)]
        
    return R


def readmyinput():
    N, K = map(int, raw_input().split())
    List = map(int, raw_input().split())
    return N, K, List

def main():
    #print "Enter number"
    N, K, List = readmyinput()

    #l = [1, 2, 3, 4, 5, 1, 1, 8] 
    #print dp(len(l), 3, l)
    print dp(N, K, List)
if __name__ == "__main__":
    main()