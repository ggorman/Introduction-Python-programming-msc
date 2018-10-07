
# coding: utf-8

# In[1]:


from lecture import *


# # Introduction to programming in Python
# ### [Gerard Gorman](http://www.imperial.ac.uk/people/g.gorman)
# 
# # Lecture 1: Computing with formulas

# ## Learning objectives:
# 
# * You will understand that Python will help you defy gravity.
# * You will know how to execute Python statements from within Jupyter.
# * Learn what a program variable is and how to express a mathematical expression in code.
# * Print program outputs.
# * Access mathematical functions from a Python module.
# * Be able to write your own *function*.

# ```python
# import antigravity
# ```

# ![import antigravity](https://imgs.xkcd.com/comics/python.png)

# ## Programming a mathematical formula
# 
# Here is a formula for the position of a ball in vertical motion, starting at ground level (i.e. $y=0$) at time $t=0$:
#      $$ y(t) = v_0t- \frac{1}{2}gt^2 $$
# 
# where:
# 
# * $y$ is the height (position) as a function of time $t$
# * $v_0$ is the initial velocity (at $t=0$)
# * $g$ is the acceleration due to gravity
# 
# The computational task is: given $v_0$, $g$ and $t$, compute the value $y$. 

# **How do we program this task?** A program is a sequence of instructions given to the computer. However, while a programming language is much **simpler** than a natural language, it is more **pedantic**. Programs must have correct syntax, i.e., correct use of the computer language grammar rules, and no misprints.
# 
# So let's execute a Python statement based on this example. Evaluate $y(t) = v_0t- \frac{1}{2}gt^2$ for $v_0=5$, $g=9.81$ and $t=0.6$. If you were doing this on paper you would probably write something like this: $$ y = 5\cdot 0.6 - {1\over2}\cdot 9.81 \cdot 0.6^2.$$ Happily, writing this in Python is very similar:

# In[2]:


# Comment: This is a 'code' cell within Jupyter notebook.
# Press shift-enter to execute the code within this kind of
# cell, or click on the 'Run' widget on the Jupyter tool bar above.

print(5*0.6 - 0.5*9.81*0.6**2)


# ## Exercise 1.1: Open a code cell and write some code.
# * Navigate the [Jupyter](http://jupyter.org/) tool bar to "Insert"->"Insert Cell Below". Note from the tool bar that you can select a cell to be one of 'Code' (this is the default), 'Markdown' (this cell is written in [markdown](https://en.wikipedia.org/wiki/Markdown) - double click this cell to investigate further), 'Raw NBConvert' or 'Heading' (decrepit).
# * Cut&paste the code from the previous cell into your newly created code cell below. Make sure it runs!
# * To see how important it is to use the correct [syntax](https://en.wikipedia.org/wiki/Syntax), replace `**` with `^` in your code and try running the cell again. You should see something like the following:
# 
# ```python
# >>> print(5*0.6 - 0.5*9.81*0.6^2)
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-3-40e93484ac5e> in <module>()
# ----> 1 print(5*0.6 - 0.5*9.81*0.6^2)
# 
# TypeError: unsupported operand type(s) for ^: 'float' and 'int'
# ```
# * Undo that change so your code is working again; now change 'print' to 'write' and see what happens when you run the cell. You should see something like:
# 
# ```python
# >>> write(5*0.6 - 0.5*9.81*0.6**2)
# 
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-5-492c3eff3ad9> in <module>()
# ----> 1 write(5*0.6 - 0.5*9.81*0.6**2)
# 
# NameError: name 'write' is not defined
# ```
# 
# While a human might still understand these statements, they do not mean anything to the Python interpreter. Rather than throwing your hands up in the air whenever you get an error message like the above (you are going to see many during the course of these lectures!!!) train yourself to read error messages carefully to get an idea what it is complaining about and re-read your code from the perspective of the Python interpreter.
# 
# Error messages can look bewildering and even frustrating at first, but it gets much **easier with practise**.

# ## Storing numbers in variables
# From mathematics you are already familiar with variables (e.g. $v_0=5,\quad g=9.81,\quad t=0.6,\quad y = v_0t -{1\over2}gt^2$) and you already know how important they are for working out complicated problems. Similarly, you can use variables in a program to make it easier to read and understand.

# In[3]:


v0 = 5
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2
print(y)


# This program spans several lines of text and uses variables, otherwise the program performs the same calculations and gives the same output as the previous program.
# 
# In mathematics we usually use one letter for a variable, resorting to using the Greek alphabet and other characters for more clarity. The main reason for this is to avoid becoming exhausted from writing when working out long expressions or derivations. However, when programming you should use more descriptive names for variable names. This might not seem like an important consideration for the trivial example here but it becomes increasingly important as the program gets more complicated and if someone else has to read your code.

# ### Good variable names make a program easier to understand!
# 
# Permitted variable names include:
# 
# * One-letter symbols.
# * Words or abbreviation of words.
# * Variable names can contain a-z, A-Z, underscore ("'_'") and digits 0-9, **but** the name cannot start with a digit.
# 
# Variable names are case-sensitive (i.e. "'a'" is different from "'A'"). Let's rewrite the previous example using more descriptive variable names:

# In[4]:


initial_velocity = 5
acceleration_of_gravity = 9.81
TIME = 0.6
VerticalPositionOfBall = initial_velocity*TIME - 0.5*acceleration_of_gravity*TIME**2
print(VerticalPositionOfBall)


# Certain words have a **special meaning** in Python and **cannot be used as variable names**. These are: *and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, with, while,* and *yield*.

# ## Adding comments to code
# 
# Not everything written in a computer program is intended for execution. In Python anything on a line after the '#' character is ignored and is known as a **comment**. You can write whatever you want in a comment. Comments are intended to be used to explain what a snippet of code is intended for. It might for example explain the objective or provide a reference to the data or algorithm used. This is both useful for you when you have to understand your code at some later stage, and indeed for whoever has to read and understand your code later.

# In[5]:


# Program for computing the height of a ball in vertical motion.
v0 = 5    # Set initial velocity in m/s.
g = 9.81  # Set acceleration due to gravity in m/s^2.
t = 0.6   # Time at which we want to know the height of the ball in seconds.
y = v0*t - 0.5*g*t**2 # Calculate the vertical position
print(y)


# ## Exercise 1.2: Convert from meters to British length units
# Here in the UK we are famous for our love of performing mental arithmetic. That is why we still use both imperial and metric measurement systems - hours of fun entertainment for the family switching back and forth between the two.
# 
# Make a program where you set a length given in meters and then compute and write out the corresponding length measured in:
# * inches (one inch is 2.54 cm)
# * feet (one foot  is 12 inches)
# * yards (one foot is 12 inches, one yard is 3 feet)
# * miles (one British mile is 1760 yards)
# 
# Note: In this course we are using [okpy](https://okpy.org/) to automated assessment scoring. Therefore, while it is important to always carefully follow the instructions of a question, it is particularly important here so that okpy can recognize the validity of your answer. The conversion to inches are done for you to illustrate what is required.

# In[6]:


meters = 640

# 1 inch = 2.54 cm. Remember to convert from 2.54 cm to 0.0254 m here.
inches = meters/0.0254

# Uncomment and complete the following code.
# feet =

# yards =

# miles =


# In[7]:


#OKPY_SOLUTION

meters = 640

# 1 inch = 2.54 cm. Remember to convert from 2.54 cm to 0.0254 m here.
inches = meters/0.0254 
print("%.4f meters = %.4f inches" % (meters, inches))

feet = inches/12.0 # 1 foot = 12 inches
print("%.4f meters = %.4f feet" % (meters, feet))

yards = feet/3.0 # 1 yard = 3 feet
print("%.4f meters = %.4f yards" % (meters, yards))

miles = yards/1760.0 # 1 yard = 1760 miles
print("%.4f meters = %.6f miles" % (meters, miles))


# In[8]:


grade = ok.grade('question-1_2')


# ## Formatted printing style
# Often we want to print out results using a combination of text and numbers, e.g. "'At t=0.6 s, y is 1.23 m'". Particularly when printing out floating point numbers we should **never** quote numbers to a higher accuracy than they were measured. Python provides a *printf formatting* syntax exactly for this purpose. We can see in the following example that the *slot* `%g` was used to express the floating point number with the minimum number of significant figures, and the *slot* `%.2f` specified that only two digits are printed out after the decimal point.

# In[9]:


print("At t=%g s, y is %.2f m." % (t, y))


# Notice in this example how the values in the tuple `(t, y)` are inserted into the *slots*.

# Sometimes we want a multi-line output. This is achieved using a triple quotation (*i.e.* `"""`):

# In[10]:


print("""At t=%f s, a ball with
initial velocity v0=%.3E m/s
is located at the height %.2f m.
""" % (t, v0, y))


# ## Exercise 1.3: Compute the air resistance on a football
# The drag force, due to air resistance, on an object can be expressed as
# $$F_d = \frac{1}{2}C_D\rho AV^2$$
# where:
# * $\rho$ is the density of the air,
# * $V$ is the velocity of the object,
# * $A$ is the cross-sectional area (normal to the velocity direction),
# * and $C_D$ is the drag coefficient, which depends on the shape of the object and the roughness of the surface.
# 
# Complete the following code that computes the drag force. 

# In[11]:


# Football example

# import pi from Python's math library
from math import pi

density = 1.2      # units of kg m^{−3}$
ball_radius = 0.11 # m
A = pi*ball_radius # Cross sectional area of a sphere
mass = 0.43        # kg
C_D = 0.2          # Drag coefficient

V = 50.8           # m/s (fastest recorded speed of football)

# Uncomment and complete the following code.
# F_d = 

# Challenge yourself to use the formatted print statement
# units of Newton ($N = kgm/s^2$).


# In[12]:


#OKPY_SOLUTION

# Football example

# import pi from Python's math library
from math import pi

density = 1.2         # units of kg m^{−3}$
ball_radius = 0.11    # m
A = pi*ball_radius**2 # Cross sectional area of a sphere
mass = 0.43           # kg
C_D = 0.2             # Drag coefficient

V = 50.8              # m/s (fastest recorded speed of football)

# Uncomment and complete the following code.
# F_d = 

# Challenge yourself to use the formatted print statement
# units of Newton ($N = kgm/s^2$).


# Solution
F_d = 0.5*C_D*density*A*V**2 

print("The drag force acting on the ball after a hard kick is %.1f N" % F_d)


# In[13]:


grade = ok.grade('question-1_3')


# ## How are arithmetic expressions evaluated?
# Consider the random mathematical expression, ${5\over9} + 2a^4/2$, implemented in Python as `5.0/9 + 2*a**4/2`.
# 
# The rules for evaluating the expression are the same as in mathematics: proceed term by term (additions/subtractions) from the left, compute powers first, then multiplication and division. Therefore in this example the order of evaluation will be:
# 
# 1. `r1 = 5.0/9`
# 2. `r2 = a**4`
# 3. `r3 = 2*r2`
# 4. `r4 = r3/2`
# 5. `r5 = r1 + r4`
# 
# Use parenthesis to override these default rules. Indeed, many programmers use parenthesis for greater clarity.

# ## Exercise 1.4: Compute the growth of money in a bank
# Let *p* be a bank's interest rate in percent per year. An initial amount $A_0$ has then grown to $$A_n = A_0\left(1+\frac{p}{100}\right)^n$$ after *n* years. Write a program for computing how much money 1000 euros have grown to after three years with a 5% interest rate.

# In[14]:


# Complete the code commented out below (don't change variable names!)

# p = ...
# A_0 = ... 

# A_n = ...

# print("The amount of money in the account after %d years is: %.2f euros" % (n, A_n))


# In[15]:


#OKPY_SOLUTION

p = 5 # Interest rate in percent per year
A_0 = 1000.0 # Initial amount of money in euros
n = 3 # Number of years since initial deposit

A_n = A_0*(1 + p/100.0)**n

print("The amount of money in the account after %d years is: %.2f euros" % (n, A_n))


# In[16]:


grade = ok.grade('question-1_4')


# ## Standard mathematical functions
# What if we need to compute $\sin x$, $\cos x$, $\ln x$, etc. in a program? Such functions are available in Python's *math module*. In fact there is a vast universe of functionality for Python available in modules. We just *import* in whatever we need for the task at hand.
# 
# In this example we compute $\sqrt{2}$ using the *sqrt* function in the *math* module:

# In[17]:


import math
r = math.sqrt(2)
print(r)


# or:

# In[18]:


from math import sqrt
r = sqrt(2)
print(r)


# or:

# In[19]:


from math import *   # import everything in math
r = sqrt(2)
print(r)


# Another example:

# In[20]:


from math import sin, cos, log
x = 1.2
print(sin(x)*cos(x) + 4*log(x))   # log is ln (base e)


# ## Exercise 1.5: Evaluate a Gaussian function
# The bell-shaped Gaussian function,
# $$f(x)=\frac{1}{\sqrt{2\pi}s}\exp\left(-\frac{1}{2} \left(\frac{x-m}{s}\right)^2\right)$$
# is one of the most widely used functions in science and technology. The parameters $m$ and $s$ are real numbers, where $s$ must be greater than zero. Write a program for evaluating this function when $m = 0$, $s = 2$, and $x = 1$. Verify the program's result by comparing with hand calculations on a calculator.

# In[21]:


# Uncomment and complete the code below (don't change variable names!)

# from math import pi, ...

# f_x = 


# In[22]:


#OKPY_SOLUTION

from math import exp, pi, sqrt

# Parameters.
m = 0.0 # The mean
s = 2.0 # The standard deviation
x = 1.0
coefficient = 1.0/(sqrt(2*pi)*s)

f_x = coefficient*exp(-0.5*((x - m)/s)**2)

print("The value of the Gaussian function with x = %.2f is %.4f" % (x, f_x))


# In[23]:


grade = ok.grade('question-1_5')


# ## Exercise 1.6: Find errors in the coding of a formula
# Given a quadratic equation,
# $$ax^2 + bx + c = 0,$$
# $$x1 = \frac{−b + \sqrt{b^2 −4ac}}{2a},$$ and
# $$x2 = \frac{−b − \sqrt{b^2 −4ac}}{2a}.$$
# 
# Uncomment and fix the errors in the following code.

# In[24]:


# a = 2; b = 1; c = -2
# from math import sqrt
# q = sqrt(b*b + 4*a*c)
# x1 = (-b + q)/2*a
# x2 = (-b - q)/2*a
# print(x1, x2)


# In[25]:


#OKPY_SOLUTION

a = 2; b = 1; c = -2
from math import sqrt

q = sqrt(b**2 - 4*a*c)
x1 = (-b + q)/(2*a)
x2 = (-b - q)/(2*a)
print(q, x1, x2)


# In[26]:


grade = ok.grade('question-1_6')


# ## Functions
# 
# We have already used Python functions, e.g. `sqrt` from the `math` module above. In general, a function is a collection of statements we can execute wherever and whenever we want. For example, consider any of the formula you implemented above. 
# 
# Functions can take any number of inputs (called *arguments*) to produce outputs. Functions help to organize programs, make them more understandable, shorter, and easier to extend. Wouldn't it be nice just to implement it just once and be able to use it again any time you need rather than having to write out the whole formula again?
# 
# For our first example we will use again the formula above for the height of a ball in vertical motion.

# In[27]:


# Function to compute height of ball.
def ball_height(v0, t, g=9.81):
    """Function to calculate height of ball.
    
    Parameters
    ----------
    v0 : float
        Set initial velocity (units, m/s).
    t : float
        Time at which we want to know the height of the ball (units, seconds).
    g : float, optimal
        Acceleration due to gravity, by default 9.81 m/s^2.

    Returns
    -------
    float
        Height of ball in meters.
    """

    height = v0*t - 0.5*g*t**2
    
    return height


# Lets break this example down:
# * Function header:
#  * Functions start with *def* followed the name you want to give the function (ball_height in this case).
#  * Following the name you have `(...):` containing some number of function `arguments`.
#  * In this case `v0` and `t` are *position arguments* while `g` is known as a *keyword argument* (more about this later).
# * Function body.
#  * The first thing to notice is that the body of the function is indented one level.
#  * Best practice is to include a [docstring](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html) to explain to others (or remind your future self) how the function should be used.
#  * The function output is passed back via the `return` statement
#  
# Notice that this just defines the function. Nothing is actually executed until you actually *use* the function:

# In[28]:


print("Ball height: %g meters."%ball_height(5, 0.6))


# No return value implies that `None` is returned. `None` is a special Python object that represents an ”empty” or undefined value. It is surprisingly useful and we will use it a lot later.
# 
# Functions can also return multiple values. Let's extend the previous example to calculate the ball velocity as well as the height:

# In[29]:


# Function to compute height of ball.
def ball_height_velocity(v0, t, g=9.81):
    """Function to calculate height and velocity of ball.
    
    Parameters
    ----------
    v0 : float
        Set initial velocity (units, m/s).
    t : float
        Time at which we want to know the height of the ball (units, seconds).
    g : float, optimal
        Acceleration due to gravity, by default 9.81 m/s^2.

    Returns
    -------
    float
        Height of ball in meters.
    float
        Velocity of ball in m/s.
    """

    height = v0*t - 0.5*g*t**2
    velocity = v0 - g*t
    
    return height, velocity

h, v = ball_height_velocity(5, 0.6)

print("Ball height: %g meters."%h)
print("Ball velocity: %g m/s."%v)


# ## Scope: Local and global variables
# 
# Variables defined within a function are said to have *local scope*. That is to say that they can only be referenced within that function. Consider the example function defined above where we used the *local* variable *height*. You can see that if you try to print the variable height outside the function you will get an error.
# 
# ```python
# print(height)
# 
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-8-aa6406a13920> in <module>()
# ----> 1 print(height)
# 
# NameError: name 'height' is not defined
# ```

# ## Keyword arguments and default input values
# 
# Functions can have arguments of the form variable_name=value and are called keyword arguments:

# In[30]:


def somefunc(arg1, arg2, kwarg1=True, kwarg2=0):
    print(arg1, arg2, kwarg1, kwarg2)

somefunc("Hello", [1,2])   # Note that we have not specified inputs for kwarg1 and kwarg2


# In[31]:


somefunc("Hello", [1,2], kwarg1="Hi")


# In[32]:


somefunc("Hello", [1,2], kwarg2="Hi")


# In[33]:


somefunc("Hello", [1,2], kwarg2="Hi", kwarg1=6)


# If we use variable_name=value for all arguments, their sequence in the function header can be in any order.

# In[34]:


somefunc(kwarg2="Hello", arg1="Hi", kwarg1=6, arg2=[2])


# ## Exercise 1.7: Implement a Gaussian function
# 
# Create a Python function to compute the Gaussian: 
# $$f(x)=\frac{1}{s\sqrt{2\pi}}\exp\left(-\frac{1}{2} \left(\frac{x-m}{s}\right)^2\right)$$

# In[35]:


# Uncomment and complete this code - keep the names the same for testing purposes. 

# def gaussian(x, m=0, s=1):
#     ...


# In[36]:


#OKPY_SOLUTION
from math import sqrt, exp, pi
def gaussian(x, m=0, s=1):
    return 1/(s*sqrt(2*pi))*exp(-0.5*((x-m)/s)**2)


# In[37]:


ok.grade('question-1_7')


# In[38]:


ok.score()

