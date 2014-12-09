import unittest, random, solution

class TestSequenceFunctions(unittest.TestCase):
    def naive(self ,N, K, List):
        R = []
        for n in range(N-K+1):
            total_increasing, total_decreasing = 0, 0
            increasing, decreasing = 0, 0

            for k in range(n, n+K-1):
                if List[k+1] >= List[k]:
                    increasing += 1
                    total_increasing += increasing
                else:
                    increasing = 0

                if List[k+1] <= List[k]:
                    decreasing += 1
                    total_decreasing += decreasing
                else:
                    decreasing = 0
            R += [total_increasing - total_decreasing]
        return R

    def setUp(self):
        self.MAX = 10000
        self.MAXLEN = 10

    def setSequence(self, N, K, List):
        self.N, self.K, self.seq = N, K, List

    def randomSequence(self):
        self.N = random.randint(1, self.MAXLEN)
        self.K = random.randint(1, self.N)
        self.seq = [random.randint(1, self.MAX) for _ in range(self.N)]
        

    def test_shuffle(self):
        return 
        self.randomSequence()
        try:
            dp = solution.dp(self.N, self.K, self.seq)
            naive = self.naive(self.N, self.K, self.seq)
            self.assertEqual(dp, naive)
        except Exception, e:
            print (self.N, self.K, self.seq)
            print dp, naive
        #print 
        #print 
        #print 
    def test_manual(self):
        N, K, L = (5, 4, [9141, 8643, 4445, 6639, 2641])

        self.setSequence(N, K, L)
        print self.naive(self.N, self.K, self.seq)

        self.setSequence(N, K, L)
        print solution.dp(self.N, self.K, self.seq)

if __name__ == '__main__':
    unittest.main()