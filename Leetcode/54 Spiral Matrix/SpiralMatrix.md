# Spiral Matrix

Return the elements of a matrix in spiral order. (see spiral1.jpg)

Key #1, assuming we have a matrix (and not an array), our first step is always to take the top m elements, add them to our return list and then continue the problem.
This implies a recursive approach, but the sprial pattern requires that we take the remainder of our input matrix, rotate it 90 degrees counter clockwise, and recur.

Key #2, the base case is an array. Either vertical, horisontal, or empty. Simply return this array.
