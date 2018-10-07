
# coding: utf-8

# In[1]:


from lecture import *


# # Introduction to programming in Python
# ### [Gerard Gorman](http://www.imperial.ac.uk/people/g.gorman)
# 
# # Lecture 5: Plotting and error handling

# Learning objectives:
# 
# * Learn how to plot 2D graphs.
# * Read data from files.
# * Catch run-time errors and handle them gracefully rather than the program simply failing.

# ## Plotting curves - the basics
# 
# If you have programmed in Python before, or indeed when you start looking at coding examples online, you will notice that there are a few different modules that you can import to enable you to accomplish more or less the same objective. The three most common are [matplotlib](https://matplotlib.org/index.html), [pyplot](https://matplotlib.org/api/pyplot_api.html), and pylab. I will leave it to you to read the [official documentation to see how these three are related](https://matplotlib.org/faq/usage_faq.html#matplotlib-pyplot-and-pylab-how-are-they-related).
# 
# For this lecture series we will be importing matplotlib.pyplot as plt so that it is always clear where each function call is coming from. Lets start with a simple example by plotting the function $y = f(x)$.

# In[2]:


import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 3, 51)
y = t**2*np.exp(-t**2)
plt.plot(t, y)


# Plots also should have **labels** on the axis, a **title**, and sometimes a specific extent of the axis (perhaps you wish to easily compare two graphs side-by-side):

# In[3]:


def f(t):
    return t**2*np.exp(-t**2)

# Generates 51 points between 0 and 3
t = np.linspace(0, 3, 51)
y = f(t)
plt.plot(t, y)

# For added awesomeness you can use Latex syntax.
plt.legend(('$t^2\exp(-t^2)$',))

plt.xlabel('$t$')
plt.ylabel('$y$')

# Specify the extent of the axes [tmin, tmax, ymin, ymax]
plt.axis([0, 3, -0.05, 0.6]) 

plt.title('My second graph')


# ## Exercise 5.1: Plot a formula
# 
# `NOTE: We have found that automated assessment is too unreliable for assessing plots. For feedback on the plots compare with your peers or ask one of the TA's to give you feedback.`
# 
# * Make a plot of the function $$y(t) = v_0t − 0.5gt^2$$ for $v_0 = 10$, $g = 9.81$, and $t \in [0, 2v_0/g]$. The label on the *x* axis should be 'time (s)' and the label on the *y* axis should be 'height (m)'.

# In[4]:


# OKPY_SOLUTION

v0 = 10.
g = 9.81

n = 50 # number of points to be plotted on the graph
t = np.linspace(0,2*v0/g,n) # generate n points between 0 and 2*v0/g
y = v0*t - 0.5*g*t**2

plt.plot(t, y)
plt.xlabel('time (s)')
plt.ylabel('height (m)')


# ## Exercise 5.2: Plot another formula
# 
# The function
# 
# $$f(x, t) = \exp(-(x - 3t)^2)\sin(3\pi(x - t)).$$
# 
# describes, for a fixed value of *t*, a wave localized in space. Make a program that visualizes this function as a function of *x* on the interval [−4, 4] when *t* = 0.

# In[5]:


# OKPY_SOLUTION

def f(x,t):
    return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))

n=500 # number of points to be plotted on the graph
x=np.linspace(-4., 4., n) 
y=f(x,0.0)

# plot graph
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('f')


# ## Multiple curves in one plot
# 
# We can also plot several curves in one plot:

# In[6]:


def f1(t):
    return t**2*np.exp(-t**2)

def f2(t):
    return t**2*f1(t)

t = np.linspace(0, 3, 51)
y1 = f1(t)
y2 = f2(t)

# Matlab-style syntax:
plots = plt.plot(t, y1, t, y2)
plt.legend(plots, ('$t^4\exp(-t^2)$', '$t^4\exp(-t^2)$'), loc='best')
plt.xlabel('$t$')
plt.ylabel('$y$')
plt.title('Plotting two curves in the same plot')


# When plotting multiple curves in the same plot, PyLab usually does a good job in making sure that the different lines actually look different. However, sometimes you need to take action yourself (*e.g.* if you need to print your graph out in black&white). To do this we can add an extra argument to the plot command where we specify what we want - *e.g.* "r-" means a *red line*, while "bo" means *blue circles*:

# In[7]:


plt.plot(t, y1, 'r-', t, y2, 'bo')


# For further examples check out the [matplotlib](https://matplotlib.org/) documentation.

# ## Exercise 5.3: Plot a formula for several parameters
# 
# Write a program in which you generate 10 uniformly spaced values for $v_0$ range from 1 to 20, and plots the function $y(t) = v_0t − 0.5gt^2$ within the time range $t \in [0, 2v_0/g]$. Assume $g = 9.81$.

# In[8]:


# OKPY_SOLUTION

g = 9.81

for v0 in np.linspace(1., 10., 10):
    n = 50 # Number of points to be plotted on the graph
    t = np.linspace(0,2*v0/g,n) # Generate n points between 0 and 2*v0/g
    y = v0*t - 0.5*g*t**2

    plt.plot(t, y)

plt.xlabel('Time (s)')
plt.ylabel('Height (m)')


# ## Handling errors gracefully
# 
# I expect you have seen plenty of run-time errors. When an error occurs an *exception* is *raised*. These exceptions tend to be very specific and it is worth familiarizing yourself with them.
# 
# https://docs.python.org/3/library/exceptions.html#concrete-exceptions
# 
# Lets take a look at an example of an out of bounds reference - this raises an exception called an `IndexError`.
# 
# ```python 
# places_to_visit = ("Pompeii",
#                    "Fernanda de Noronha",
#                    "Dolomites",
#                    "Bourbon Street")
# print(places_to_visit[4])
# 
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-6-6a516db87396> in <module>()
#       1 places_to_visit = ("Pompeii", "Fernanda de Noronha", "Dolomites", "Bourbon Street")
#       2 option = 4 # lets assume that the user has given the input option 4
# ----> 3 print(places_to_visit[option])
# 
# IndexError: tuple index out of range```

# Here we have an **IndexError** (i.e. a reference out of bounds) with the clarification that it is the **tuple index out of range**.
# 
# The general way we deal with this issue in Python (and in many other programming languages) is to try to do what we indend to, and if it fails, we recover from the error. This is implemented using the *try-except* block:
# ```
# try:
#     <statements we indend to do>
# except:
#     <statements for handling errors>
# ```

# If something goes wrong in the **try** block, Python raises an **exception** and the execution jumps immediately to the **except** block. If you use an `except` by itself as above then it will catch all exceptions raised but this is generally considered bad practice as it can hide errors that you might have not anticipated - the last thing we want is to hid a bug!
# 
# Let's try an example:

# In[9]:


def get_location(index):
    places_to_visit = ("Pompeii",
                       "Fernanda de Noronha",
                       "Dolomites",
                       "Bourbon Street")

    try:
        return places_to_visit[index]
    except TypeError:
        raise TypeError("The index should be an integer.")
    except IndexError:
        raise IndexError("Values must be between 0-3.")

    return None

print("Test case 1: ", get_location(1))


# If we pass in 4 as an argument, an *IndexError* ia raised.
# ```python
# print("Test case 2: ", get_location(4))
# 
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-9-9d82aff2337b> in get_location(index)
#       7     try:
# ----> 8         return places_to_visit[index]
#       9     except TypeError:
# 
# IndexError: tuple index out of range
# 
# During handling of the above exception, another exception occurred:
# 
# IndexError                                Traceback (most recent call last)
# <ipython-input-10-baa17f0505ab> in <module>()
#       1 # If we pass in 4 as an argument, an *IndexError* ia raised.
# ----> 2 print("Test case 2: ", get_location(4))
# 
# <ipython-input-9-9d82aff2337b> in get_location(index)
#      10         raise TypeError("The index should be an integer.")
#      11     except IndexError:
# ---> 12         raise IndexError("Values must be between 0-3.")
#      13 
#      14     return None
# 
# IndexError: Values must be between 0-3.```

# In the above example the expected input is an integer. If the user types a string, e.g. "four", then a **TypeError** is raised, and the approperiate except block is executed.
# 
# ```python
# print("Test case 3: ", get_location("four"))
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-9-9d82aff2337b> in get_location(index)
#       7     try:
# ----> 8         return places_to_visit[index]
#       9     except TypeError:
# 
# TypeError: tuple indices must be integers or slices, not str
# 
# During handling of the above exception, another exception occurred:
# 
# TypeError                                 Traceback (most recent call last)
# <ipython-input-10-a8af82536957> in <module>()
#       2 # If the user types a string, e.g. "four", then a **TypeError** is raised,
#       3 # and the approperiate except block is executed.
# ----> 4 print("Test case 3: ", get_location("four"))
# 
# <ipython-input-9-9d82aff2337b> in get_location(index)
#       8         return places_to_visit[index]
#       9     except TypeError:
# ---> 10         raise TypeError("The index should be an integer.")
#      11     except IndexError:
#      12         raise IndexError("Values must be between 0-3.")
# 
# TypeError: The index should be an integer.```

# This is still not perfect. What happens if you enter -1...?

# In[10]:


print("Test case 4: ", get_location(-1))


# Recall that negative indices traverse the list from the end to the beginning. We can deal with this issue more elegantly/robustly if we **raise** our own error:

# In[11]:


def get_location(index):
    places_to_visit = ("Pompeii",
                       "Fernanda de Noronha",
                       "Dolomites",
                       "Bourbon Street")

    try:
        if not 0 <= index < len(places_to_visit):
            raise IndexError
        
        return places_to_visit[index]
    except TypeError:
        raise TypeError("The index should be an integer.")
    except IndexError:
        raise IndexError("Values must be between 0-3.")

    return None


# ```python
# print("Test case 5: ", get_location(-1))
# 
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-11-d29b7f03e343> in get_location(index)
#       8         if not 0 <= index < len(places_to_visit):
# ----> 9             raise IndexError
#      10 
# 
# IndexError: 
# 
# During handling of the above exception, another exception occurred:
# 
# IndexError                                Traceback (most recent call last)
# <ipython-input-11-d29b7f03e343> in <module>()
#      17     return None
#      18 
# ---> 19 print("Test case 5: ", get_location(-1))
# 
# <ipython-input-11-d29b7f03e343> in get_location(index)
#      13         raise TypeError("The index should be an integer.")
#      14     except IndexError:
# ---> 15         raise IndexError("Values must be between 0-3.")
#      16 
#      17     return None
# 
# IndexError: Values must be between 0-3.```

# ## Exercise 5.4: Test more in the program
# 
# Consider the equation of motion in exercise 5.1.
# 
# * Implement this as a Python function - call the function *y* and specify two positional arguments $t$, $v0$.
# * The function should raise a ValueError if either $t$ or $v0$ are negative.

# In[12]:


# OKPY_SOLUTION

def y(t, v0):
    g = 9.81 # Assigns g value

    if t < 0:
        raise ValueError("Time, t, must be greater or equal to 0.")

    if v0 < 0:
        raise ValueError("Initial velocity, v0, must be greater or equal to 0.")
    
    return v0*t - 0.5*g*t**2


# In[13]:


ok.grade('question-5_4')


# ## Exercise 5.5: Implement the factorial function with exception handling
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
# 
# An exception should be thrown/raised if the number *n* is negative. If an exception occurs, your program should print a helpful error message and quit.

# In[14]:


# Uncomment and complete this code - keep the names the same for testing purposes. 

# def my_factorial(x):
#     ...


# In[15]:


# OKPY_SOLUTION
def my_factorial(n):
    try:
        if(n < 0):
            raise ValueError
        elif(n == 1 or n == 0):
            return 1
        else:
            product = 1 # This variable keeps track of the product n * (n-1) * (n-2) * ... * 1
            while n > 1:
                product *= n
                n -= 1 # Keep decreasing n until we reach 1, then return the result held in the variable 'product'.
            return product
    except ValueError:
        raise ValueError("n must be greater than or equal to 0.")


# In[16]:


ok.grade('question-5_5')


# ## Exercise 5.6: Wave speed
# 
# The longitudinal wave velocity in a material is given by the equation:
# $$V_p = \sqrt{\frac{k+4\mu/3}{\rho}},$$
# where $V_p$ is the longitudinal wave velocity, $k$ is the bulk modulus, $\mu$ is the shear modulus and $\rho$ is the density. The shear wave velocity is given by the equation:
# $$V_s = \sqrt{\frac{\mu}{\rho}},$$
# where $V_s$ is the shear velocity.
# 
# 1. Write a *function* that takes as arguments $k$, $\mu$ and $\rho$, and returns $V_p$ and $V_s$.
# 2. Ensure your function raises a ValueError if any of the input arguments have a non-physical value (ie cannot have negative density).
# 
# | Material               | Shear modulus (GPa) | Bulk modulus (GPa) | Density (kg/m^3)|
# |------------------------|---------------------|--------------------|-----------------|
# |Quartz                  | 44                  | 38                 | 2650            | 
# |Clay                    | 6.85                | 20.9               | 2580            |
# |Water                   | 0                   | 2.29               | 1000            |
# 

# In[17]:


# Uncomment and complete this code - keep the names the same for testing purposes. 

# mu: Shear modulus (GPa), k: Bulk modulus (GPa), rho:Density (kg/m^3)
# def calc_material_velocity(mu, k, rho):
#     ...
#     return vp, vs


# In[18]:


# OKPY_SOLUTION

from math import sqrt
def calc_material_velocity(mu, k, rho):
    k *= 1.0e9
    mu *= 1.0e9
    
    if k<0:
        raise ValueError("Bulk modulus should be a positive real in units of GPa.")
        
    if mu<0:
        raise ValueError("Shear modulus should be a positive real in units of GPa.")
        
    if rho<0:
        raise ValueError("Density should be a positive real in units of kg/m^3.")
    
    # Divide to 1000 to convert to km/s
    vp = sqrt((k+4*mu/3.0)/rho)/1000.0
    vs = sqrt(mu/float(rho))/1000.0
    
    return vp, vs


# In[19]:


ok.grade('question-5_6')


# In[20]:


ok.score()

