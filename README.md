# code
One problem we have had to deal with in the Singular Spectrum Analysis implementation was Hankelization of a matrix. A Hankel matrix has constant skew diagonal values. 
Objective
We would like to take any matrix and Hankelize it (i.e. convert it to a Hankel matrix). The way we do it is by replacing each element by its diagonal average.
See the example below for a 3 x 6 matrix:

A(0,0) = 2/1
A(0,1) = (A(0,1) + A(1,0))/2 = (7 + 5)/2 = 6
A(1,0) = (A(1,0) + A(0,1))/2 = (5 + 7)/2 = 6
….
A(2,0) = (A(2,0) + A(1,1) + A(0,2))/3 = (3 + 4 – 1)/3 = 2

