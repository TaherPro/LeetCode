Big O Notation 
is a way to measure the time and space complexity of an algorithm. It describes the upper bound of the complexity in the worst-case scenario.

* Describes the asymptotic behavior (order of growth of time or space in terms of input size) of a function, not its exact value.
* Allows programmers to compare different algorithms and choose the most efficient one for a specific problem.
* Enables developers to optimize code and improve overall performance.

Quick Way to find Big O of an Expression
* Ignore the lower order terms and consider only highest order term.
* Ignore the constant associated with the highest order term.
* Ex: f(n) = 3n2 + 2n + 1000Logn +  5000 => The Big O is O(n2)

Worst Case Analysis (Mostly used) 
* In the worst-case analysis, we calculate the upper bound on the running time of an algorithm. We must know the case that causes a maximum number of operations to be executed.
* For Linear Search, the worst case happens when the element to be searched (x) is not present in the array. When x is not present, the search() function compares it with all the elements of arr[] one by one.
* This is the most commonly used analysis of algorithms. Most of the time we consider the case that causes maximum operations.

Best Case Analysis (Rarely used)
* In the best-case analysis, we calculate the lower bound on the running time of an algorithm. We must know the case that causes a minimum number of operations to be executed.
* For linear search, the best case occurs when x is present at the first location. The number of operations in the best case is constant (not dependent on n). So the order of growth of time taken in terms of input size is constant.
