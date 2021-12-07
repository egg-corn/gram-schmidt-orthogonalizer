# gram-schmidt-orthogonalizer
----------

The code requires SymPy to work. If you don't have it already, run the command
```
pip install sympy
```
to install SymPy.

Example, I want to perform Gram-Schmidt Orthogonalization on the vectors (1, 2, 0), (1, 1, 0), (1, 0, 1).  We run the script, type 3 (number of vectors), key in our vectors as such:

```
Gram-Schmidt orthogonalizer ver 2.1.

Start by inputting the number of vectors, eg. 4
>>> 3
Next, enter your vectors one by one,  seperating entries with commas.
For example, "3, 4, 16/5, 3*sqrt(6)/2" for a 4D vector.
Do note that decimals (eg. 3.1) are NOT supported.
Also ensure that your vectors are independent.
Type 'delete' to remove the previous entry.

0/3 >>> 1,2,0
Keyed-in vectors:
(1, 2, 0)

1/3 >>> 1,1,0
Keyed-in vectors:
(1, 2, 0)
(1, 1, 0)

2/3 >>> 1,0,1
```

and this will appear:

```
Let a1, ..., a3 be the vector(s) (1, 2, 0), (1, 1, 0), (1, 0, 1) respectively.

Step 0:

Define:
    w1 := a1 
        = (1, 2, 0) 

Step 1:

Calculating:
    ||w1||^2 = 5
    a2.w1 = (1, 1, 0).(1, 2, 0) = 3

Define:
    w2 := a2 - (a2.w1)/(||w1||^2)*w1 
        = (1, 1, 0) - (3)/(5)*(1, 2, 0) 
        = (2/5, -1/5, 0)

Step 2:

Calculating:
    ||w2||^2 = 1/5
    a3.w1 = (1, 0, 1).(1, 2, 0) = 1
    a3.w2 = (1, 0, 1).(2/5, -1/5, 0) = 2/5

Define:
    w3 := a3 - (a3.w1)/(||w1||^2)*w1 - (a3.w2)/(||w2||^2)*w2 
        = (1, 0, 1) - (1)/(5)*(2/5, -1/5, 0) - (2/5)/(1/5)*(2/5, -1/5, 0) 
        = (0, 0, 1)

Step 3:

Calculating:
    ||w3||^2 = 1

Define:
    v1 := w1/||w1|| = (sqrt(5)/5, 2*sqrt(5)/5, 0)
    v2 := w2/||w2|| = (2*sqrt(5)/5, -sqrt(5)/5, 0)
    v3 := w3/||w3|| = (0, 0, 1)

to obtain a basis T := {v1, ..., v3} of orthonormal vectors with the same column space as {a1,...,a3}.

```
