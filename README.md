practices
=========

Practices

# How to solve (programming) problems

This is essentially my interpretation of George Polya's probelm solving techniques, applied to programming problems.
## Understand the problem
1. Clarify the problem
2. Think about the inputs, their bounds and types. 
  * Make sure if you can assume valid input, or if you should sanitize/throw exceptions for invalid/out-of-range inputs. Write them down.
  * Note down if the input is sorted or not.
3. Find some good examples and some bad examples.
4. Find edge cases. These are typical edge cases:
  * Empty list, string, array, null, ...
  * Max and mins. Sometimes there are the input type's bounds (e.g. INT_MAX and INT_MIN), but often these are problem specific (e.g. in a digit manipulation problem, 0 <= d <= 9), or when passed size of the array > size of the array
  * Zero
  * Negative numbers
  * Differently sized inputs (e.g. for string comparison, whewn inputs have different sizes)
  * Any input that leads to invalid results (zero for denominator of a division, negatives and zero for log, ...)
  * Duplicated values (e.g. in an array)
  * Invalid input (e.g. startIndex > endIndex)
  
4. Model the problem:
  * See if you can model the problem as a linked-list, tree, or graph.

## Devise a plan

This is the most challenging part, and can take some creativity. But, for the majority of the programming problems (in interviews, for example), you can use a step by step approach and find an optimal solutin.


### Classes of solution

I would like to think about the following classes of solutions:

1. Naive: 
  * The solution is based on the word-by-word definition of the problem. 
  * This usually is not the optimal solution. But is a first step.

2. Known solutions:
  * Quit often, the problem is simply restatement of a well-known problem, maybe with a small change.
  * Depeneding on how you model your problem, you might figure a well-know solution would solve your problem. For example, if you model your problem as a tree, an infix tree traversal might be all you need to solve your problem.
  
3. Solved Subproblems:
  * Assume you have solved smaller problems. Think how you can use those solved problems to solve the original problem.
  * Generally you can use recursion (optimally dynamic programming), or divide and conquer.
  * Assume you have a T function that solves the problem.
  * Find the proper signature of T. This is a very important step, as sometimes this alone reveals the solution or gives you new ideas about how to look at the problem.
  * Find a way to solve a bigger problem using the **smaller** solution(s). This is usually done by increasing the input by 1, or by doubling the input size. For example, if your solution has 1 input parameter, try to write a formula for T(n) based on T(n-1)...T(1).

4. Creative ways:
  * Sorting inputs: See if you can solve the problem if you first sort the input.
  * Elimination: Try to find situations where specific inputs cannot lead to a solution. Eliminating those can lead to a simpler/faster solution
  * Invariants: Sometimes there are things that won't change with the change in the input. Identifying these invariants can  lead to a good solution
  * Changing/Combining inputs: In some cases, changing and combining inputs and solving for those changed inputs lead to a better solution. For example, subtracting two inputs and use that as the new problem input.
  * Symmetry: Is there any symmetry in the problem? Can you use symmetry to get to a solution?
  
### Finding the solution

1. Create a table, first column is name of the solution, second and third column time and memory complexities.
2. Start with the solution class 1.
3. Give your solution a name, and note down its time and space complexity in the table. 
4. See if you can trade off memory for time. I.e. store some extra information and use them to get to a faster solution.
5. Identify the basic operations in your solution and use the best data structures and algorithms for each:
  * Use a hash based ds random access of unique inputs, in pyhon: dict (or set if you only care about existence of an element). In C++: unordered_map and unordered_set respectively. All operations are O(1) on average.
  * sort: Use quicksort (mergesort for data on disk).
  * find_max or find_min: use a heap
  * For stack or queue, use a linked list or collections.deque in Python (O(1) for append, append_left, pop, and pop_left. O(n) for random index).
6. If you haven't got to the optimal solution, go move on to the next solution class and jump to step 3.
  * Usually, you are expected to find an O(n) solution. Typically any quadratic (O(n^2)) or worse solution can be still optimized.
  * If using recursion, see if caching (dynamic programming) can improve the runtime.

## Carrying out the plan
1. Write the solution in the form of (pseudo-)code. 
2. Go through all the steps after you are done with the code.   
  * Make sure you use the right ds for the job.
  * For recursion and interation, go through some examples step by step. Use a table with iteration/recursion variable in one colum and rest of operations in another.
3. Test your code for edge cases and invalid input.
 


  
