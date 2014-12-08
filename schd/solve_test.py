import unittest, random, solve, solution

import time                                                

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed

class TestSequenceFunctions(unittest.TestCase):

    def makeSeq(self):
        P = range(100)
        T = range(100)
        random.shuffle(P)
        random.shuffle(T)
        T = T[:self.sequenceLen]
        P = map(lambda x:x/100.0, P[:self.sequenceLen])
        self.seq = zip(T,P)

    def setUp(self):
        self.sequenceLen = 100
        self.epsilon = 0.000001
        self.makeSeq()

    def test_recursive(self):
        
        while True:
            self.makeSeq()                
            print timeit(solve.solve_dp)(self.seq)
            #print timeit(solve.solve_naive)(self.seq)
        
            #self.assertTrue(abs(solve.solve_naive(self.seq) - solution.solve_dp(self.seq)) < self.epsilon)


if __name__ == '__main__':
    unittest.main()
