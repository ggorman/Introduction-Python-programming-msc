
# coding: utf-8

# In[1]:


from lecture import *


# # Introduction to programming in Python
# ### [Gerard Gorman](http://www.imperial.ac.uk/people/g.gorman)
# 
# # Lecture 3: More on lists, tuples and if statements

# Learning objectives:
# 
# * Know how to modify elements in a list.
# * Be able iterate through different combinations of lists.
# * Know how to use a *tuple* to store data elements and understand how it differs from a *list*.
# * Know the difference between a locally-scoped and globally-scoped variables.
# * Be able to use an *if* statement to execute some code blocks conditionally.

# # Changing elements in a list
# Say we want to add $2$ to all the numbers in a list:

# In[2]:


v = [-1, 1, 10]
for e in v:
    e=e+2
print(v)


# We can see that the list *v* is unaltered! The reason for this is that inside the loop, *e* is an ordinary (int) variable. At the start of the iteration *e* is assigned a *copy* of the next element in the list. Inside the loop we can change *e* but *v* itself is unaltered. If we want to change *v* we have to use an index to access and modify its elements:

# In[3]:


v[1] = 4 # assign 4 to 2nd element (index 1) in v
print(v)


# To add 2 to all values we need a *for* loop over indices:

# In[4]:


for i in range(len(v)):
    v[i] = v[i] + 2
print(v)


# ## Exercise 3.1: Create a list and modify it.
# * Create a list of all integers in the range -10 to 10 (call the list *vector* for testing purposes).
# * Write a loop to multiple each element of the list by 2.

# In[5]:


#OKPY_SOLUTION
vector = [i for i in range(-10, 11)]

for i in range(len(vector)):
    vector[i] = 2*vector[i]

print(vector)


# In[6]:


ok.grade('question-3_1')


# ## Traversing multiple lists simultaneously - *zip(list1, list2, ...)*
# Consider how we can loop over elements in both Cdegrees and Fdegrees at the same time. One approach would be to use list indices:

# In[7]:


# First we have to recreate the data from the previous lecture
Cdegrees = [deg for deg in range(-20, 41, 5)]
Fdegrees = [(9/5)*deg + 32 for deg in Cdegrees]

for i in range(len(Cdegrees)):
    print(Cdegrees[i], Fdegrees[i])


# An alternative construct (regarded as more ”Pythonic”) uses the *zip* function:

# In[8]:


for C, F in zip(Cdegrees, Fdegrees):
    print(C, F)


# Another example with three lists:

# In[9]:


l1 = [3, 6, 1]; l2 = [1.5, 1, 0]; l3 = [9.1, 3, 2]
for e1, e2, e3 in zip(l1, l2, l3):
    print(e1, e2, e3)


# If the lists are of unequal length then the loop stops when the end of the shortest list is reached. Experiment with this:

# In[10]:


l1 = [3, 6, 1, 4, 6]; l2 = [1.5, 1, 0, 7]; l3 = [9.1, 3, 2, 0, 9]
for e1, e2, e3 in zip(l1, l2, l3):
    print(e1, e2, e3)


# ## Nested lists: list of lists
# A *list* can contain **any** object, including another *list*. To illustrate this, consider how to store the conversion table as a single Python list rather than two separate lists.

# In[11]:


Cdegrees = range(-20, 41, 5)
Fdegrees = [(9.0/5)*C + 32 for C in Cdegrees]
table1 = [Cdegrees, Fdegrees]  # List of two lists
print("table1 = ", table1)
print("table1[0] = ", table1[0])
print("table1[1] = ", table1[1])
print("table1[1][3] = ", table1[1][3])


# This gives us a table of two rows. How do we create a table of columns instead:

# In[12]:


table2 = []
for C, F in zip(Cdegrees, Fdegrees):
    row = [C, F]
    table2.append(row)
print(table2)


# We can use list comprehension to do this more elegantly:

# In[13]:


table2 = [[C, F] for C, F in zip(Cdegrees, Fdegrees)]
print(table2)


# And you can loop through this list as before:

# In[14]:


for C, F in table2:
    print(C, F)


# ## Tuples: lists that cannot be changed
# Tuples are **constant** lists, i.e. you can use them in much the same way as lists except you cannot modify them. They are an example of an [**immutable**](http://en.wikipedia.org/wiki/Immutable_object) type.

# In[15]:


t = (2, 4, 6, 'temp.pdf')               # Define a tuple.
t =  2, 4, 6, 'temp.pdf'                # Can skip parenthesis as it is assumed in this context.


# Let's see what happens when we try to modify the tuple like we did with a list:

# ```python
# t[1] = -1
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-3-593c03edf054> in <module>()
# ----> 1 t[1] = -1
# 
# TypeError: 'tuple' object does not support item assignment```

# ```python
# t.append(0)
# 
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-19-78592bf72d62> in <module>()
# ----> 1 t.append(0)
# 
# AttributeError: 'tuple' object has no attribute 'append'```

# ```python
# del t[1]
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-20-0193a527a912> in <module>()
# ----> 1 del t[1]
# 
# TypeError: 'tuple' object doesn't support item deletion```

# However, we can use the tuple to compose a new tuple:

# In[16]:


t = t + (-1.0, -2.0)
print(t)


# So, why would we use tuples when lists have more functionality?
# 
# * Tuples are constant and thus protected against accidental changes.
# * Tuples are faster than lists.
# * Tuples are widely used in Python software (so you need to know about tuples to understand other people's code!)
# * Tuples (but not lists) can be used as keys in dictionaries (more about dictionaries later).

# ## Exercise 3.2: Make a table (a list of lists) of function values
# * Write a loop that evaluates the expression $y(t) = v_0 t − 0.5gt^2$ for 11 evenly spaced values ranging from 0, to $2v_0/g$ (remember that dividing a range into n intervals results in n+1 values!) You can assume that $v_0 = 1$, $g=9.81 ms^{-2}$.
# * Store the time values and displacement ($y$) values as a nested list, i.e.
# ```python
# tlist = [t0, t1, t2, ...]
# ylist = [y0, y1, y2, ...]
# displacement = [tlist, ylist]
# ```
# * Use the variable names tlist, ylist and displacement as illustrated above example for testing purposes.

# In[17]:


#OKPY_SOLUTION
v0 = 1
g = 9.81
tlist = [i*2*v0/g/10 for i in range(11)]
ylist = [v0*t-0.5*g*t**2 for t in tlist]
displacement = [tlist, ylist]


# In[18]:


ok.grade('question-3_2')


# ## The *if* construct
# Consider this simple example:

# In[19]:


from math import sin, pi

def f(x):
    if 0 <= x <= pi:
        return sin(x)
    else:
        return 0
print(f(-pi/2), f(pi/2), f(3*pi/2))


# Sometimes it is clearer to write this as an *inline* statement:

# In[20]:


def f(x):
    return (sin(x) if 0 <= x <= pi else 0)
print(f(-pi/2), f(pi/2), f(3*pi/2))


# In general (the *else* block can be skipped if there are no statements to be executed when False) we can put together multiple conditions. Only the first condition that is True is executed.
# 
# ```
# if condition1:
#     <block of statements, executed if condition1 is True>
# elif condition2:
#     <block of statements>
# elif condition3:
#     <block of statements>
# else:
#     <block of statements>
#     
# <next statement of the program>
# ```

# ## Exercise 3.3: Express a step function as a Python function
# The following "step" function is known as the Heaviside function and
# is widely used in mathematics:
# $$H(x)=\begin{cases}0, & \text{if $x<0$}.\\\\
# 1, & \text{if $x\ge 0$}.\end{cases}$$
# Write a Python function heaviside(x) that computes H(x).

# In[21]:


# def heaviside(x):
#     ...


# In[22]:


#OKPY_SOLUTION
def heaviside(x):
    return 0 if x<0 else 1


# In[23]:


ok.grade('question-3_3')


# ## Exercise 3.4: Implement the factorial function
# 
# The factorial of $n$, written as $n!$, is defined as
# 
# $$n! = n(n − 1)(n − 2) \cdots 2 \cdot 1,$$
# 
# with the special cases
# 
# $$1! = 1,$$ $$0! = 1.$$
# 
# For example, $4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24$, and $2! = 2 \cdot 1 = 2$.
# 
# Implement your own factorial function to calculate $n!$. Return 1 immediately if $n$ is 1 or 0, otherwise use a loop to compute $n!$. You can use Pythons own [math.factorial(x)](https://docs.python.org/3/library/math.html) to check your code.

# In[24]:


# Uncomment and complete this code - keep the names the same for testing purposes. 

# def my_factorial(n):
#     ...


# In[25]:


#OKPY_SOLUTION
def my_factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        product = 1 # This variable keeps track of the product n * (n-1) * (n-2) * ... * 1
        while n > 1:
            product *= n
            n -= 1 # Keep decreasing n until we reach 1, then return the result held in the variable 'product'.
        return product


# In[26]:


ok.grade('question-3_4')


# ## Exercise 3.5: Compute the length of a path
# 
# Some object is moving along a path in the plane. At $n$ points of time we have recorded the corresponding $(x, y)$ positions of the object:
# $(x_0, y_0), (x_1, y_1), \ldots, (x_{n-1}, y_{n-1})$. The total length $L$ of the path from $(x_0, y_0)$ to $(x_{n-1}, y_{n-1})$ is the sum of all the individual line segments $(x_{i-1}, y_{i-1})$ to $(x_i, y_i)$, $i = 1, \ldots, n-1$:
# 
# $$L = \sum_{i=1}^{n-1}{\sqrt{(x_i - x_{i-1})^2 + (y_i - y_{i-1})^2}}.$$
# 
# Create a function *pathlength(x, y)* for computing $L$ according to the formula. The arguments $x$ and $y$ are two lists that hold all the $x_0, \ldots, x_{n-1}$ and $y_0, \ldots, y_{n-1}$ coordinates, respectively. Test the function on a triangular path with the four points (1, 1), (2, 1), (1, 2), and (1, 1).

# In[27]:


# Uncomment and complete this code - keep the names the same for testing purposes. 

# def path_length(x, y):
#     ...


# In[28]:


#OKPY_SOLUTION
from math import sqrt
def path_length(x,y):
    L = 0 
    for i in range(1, len(x)):
        L += sqrt( (x[i] - x[i-1])**2 + (y[i] - y[i-1])**2 )
    return L

_x = [1, 2, 1, 1]
_y = [1, 1, 2, 1]
path_length(_y, _x)


# In[29]:


ok.grade('question-3_5')


# In[30]:


ok.score()

