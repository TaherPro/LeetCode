HERE WE GONNA FOCUS ON BIG O AND TIME-SPACE COMPLICITY
______________________
Big O Notation 
is a way to measure the time and space complexity of an algorithm. It describes the upper bound of the complexity in the worst-case scenario.

What Big O Notation does?
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
----------------------------
Why is Analysis of Algorithm important?
performance is like currency through which we can buy the user-friendliness, modularity, security, maintainability. performance == scale
  
Asymptotic Analysis is the big idea that handles the above issues in analyzing algorithms. In Asymptotic Analysis, we evaluate the performance of an algorithm in terms of input size (we don’t measure the actual running time). We calculate, order of growth of time taken (or space) by an algorithm in terms of input size. For example linear search grows linearly and Binary Search grows logarithmically in terms of input size.

Order of Growth
Is an approximation of the time required to run a computer program as the input size increases. 

How do we Quickly find order of Growth?
When n >= 0, f(n) >= 0 and g(n) >= 0, we can use the below steps.
* Ignore the order terms.
* Ignore the constants
----------------------------
Analysing Loops for Complexity Analysis of Algorithms

Constant Time Complexity O(1):
The time complexity of a function (or set of statements) is considered as O(1) if it doesn’t contain a loop, recursion, and call to any other non-constant time function.   i.e. set of non-recursive and non-loop statements

Linear Time Complexity O(n):
The Time Complexity of a loop is considered as O(n) if the loop variables are incremented/decremented by a constant amount.

Quadratic Time Complexity denoted as O(n^2):
The time complexity is defined as an algorithm whose performance is directly proportional to the squared size of the input data, as in nested loops it is equal to the number of times the innermost statement is executed. For example, the following sample loops have O(n2) time complexity 

Logarithmic Time Complexity O(Log n):
The time Complexity of a loop is considered as O(Logn) if the loop variables are divided/multiplied by a constant amount. And also for recursive calls in the recursive function, the Time Complexity is considered as O(Logn).




