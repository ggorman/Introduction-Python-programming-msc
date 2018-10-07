
# coding: utf-8

# In[1]:


from lecture import *


# # Introduction to programming in Python
# ### [Gerard Gorman](http://www.imperial.ac.uk/people/g.gorman)
# 
# # Lecture 7: Strings, and dictionaries

# Learning objectives: You will learn how to:
# 
# * Parse strings to extract specific data of interest.
# * Use dictionaries to index data using any type of key.

# ## Python dictionaries
# Suppose we need to store the temperatures in Oslo, London and Paris. The Python list solution might look like:

# In[2]:


temps = [13, 15.4, 17.5]
# temps[0]: Oslo
# temps[1]: London
# temps[2]: Paris


# In this case we need to remember the mapping between the index and the city name. It would be easier to specify name of city to get the temperature. Containers such as lists and arrays use a continuous series of integers to index elements. However, for many applications such an integer index is not useful.
# 
# **Dictionaries** are containers where any Python object can be used
# as an index. Let's rewrite the previous example using a Python dictionary:

# In[3]:


temps = {"Oslo": 13, "London": 15.4, "Paris": 17.5}
print("The temperature in London is", temps["London"])


# Add a new element to a dictionary:

# In[4]:


temps["Madrid"] = 26.0
print(temps)


# Loop (iterate) over a dictionary:

# In[5]:


for city in temps:
    print("The temperature in %s is %g" % (city, temps[city]))


# The index in a dictionary is called the **key**. A dictionary is said to hold key–value pairs. So in general:
# ```python
# for key in dictionary:
#     value = dictionary[key]
#     print(value)```

# Does the dictionary have a particular key (*i.e.* a particular data entry)?

# In[6]:


if "Berlin" in temps:
    print("We have Berlin and its temperature is ", temps["Berlin"])
else:
    print("I don't know Berlin' termperature.")


# In[7]:


print("Oslo" in temps) # i.e. standard boolean expression


# The keys and values can be reached as lists:

# In[8]:


print("Keys = ", temps.keys())
print("Values = ", temps.values())


# Note that the sequence of keys is **arbitrary**! Never rely on it, if you need a specific order of the keys then you should explicitly sort:

# In[9]:


for key in sorted(temps):
    value = temps[key]
    print(key, value)


# Remove Oslo key:value:

# In[10]:


del temps["Oslo"] # remove Oslo key w/value
print(temps, len(temps))


# Similarly to what we saw for arrays, two variables can refer to the same dictionary:

# In[11]:


t1 = temps
t1["Stockholm"] = 10.0
print(temps)


# So we can see that while we modified *t1*, the *temps* dictionary was also changed.

# Let's look at a simple example of reading the same data from a file and putting it into a dictionary. We will be reading the file [data/deg2.dat](data/deg2.dat).

# In[12]:


infile = open("data/deg2.dat", "r")
# Start with empty dictionary
temps = {}             
for line in infile:
    # If you examine the file you will see a ':' after the city name,
    # so let's use this as the delimiter for splitting the line.
    city, temp = line.split(":") 
    temps[city] = float(temp)
infile.close()
print(temps)


# ## Exercise 7.1: Make a dictionary from a table
# 
# The file [data/constants.txt](data/constants.txt) contains a table of the values and the dimensions of some fundamental constants from physics. We want to load this table into a dictionary *constants*, where the keys are the names of the constants. For example, *constants['gravitational constant']* holds the value of the gravitational constant (6.67259 $\times$ 10$^{-11}$) in Newton's law of gravitation. Make a function `read_constants(file_path)`  that that reads and interprets the text in the file passed as argument, and thereafter returns the dictionary.

# In[13]:


#OKPY_SOLUTION

def read_constants(file_path):
    infile = open(file_path, "r")
    constants = {} # An empty dictionary to store the constants that are read in from the file
    infile.readline(); infile.readline() # Skip the first two lines of the file, since these just contain the column names and the separator.
    for line in infile:
        words = line.split() # Split each line up into individual words
        dimension = words.pop() # pop is a list operation that removes the last element from a list and returns it
        value = float(words.pop()) # Again, use pop to obtain the constant itself.
        name = " ".join(words) # After the two 'pop' operations above, the words remaining in the 'words' list must be the name of the constant. Join the individual words together, with spaces inbetween, using .join.
        constants[name] = value # Create a new key-value pair in the dictionary
    return constants

print(read_constants('data/constants.txt'))


# In[14]:


ok.grade('question-7_1')


# ## Exercise 7.2: Explore syntax differences: lists vs. dictionaries
# 
# Consider the following Python expression:
# ```python
# t1 = [-5, 10.5, -1, 4]
# ```
# Create a Python dictionary (call it *t2*) that only stores the values associated with the second and last elements of t1.

# In[15]:


#OKPY_SOLUTION
t1 = [-5, 10.5, -1, 4]
t2 = {1:t1[0], 3:t1[3]}


# In[16]:


ok.grade('question-7_2')


# What must be done in the last code snippet to make it work properly?

# ## Exercise 7.3: Compute the area of a triangle
# 
# An arbitrary triangle can be described by the coordinates of its three vertices: $(x_1, y_1), (x_2, y_2), (x_3, y_3)$, numbered in a counterclockwise direction. The area of the triangle is given by the formula:
# 
# $A = \frac{1}{2}|x_2y_3 - x_3y_2 - x_1y_3 + x_3y_1 + x_1y_2 - x_2y_1|.$
# 
# Write a function `triangle_area(vertices)` that returns the area of a triangle whose vertices are specified by the argument vertices, which is a nested list of the vertex coordinates. For example, vertices can be [[0,0], [1,0], [0,2]] if the three corners of the triangle have coordinates (0, 0), (1, 0), and (0, 2).
# 
# Then, assume that the vertices of the triangle are stored in a dictionary and not a list. The keys in the dictionary correspond to the vertex number (1, 2, or 3) while the values are 2-tuples with the x and y coordinates of the vertex. For example, in a triangle with vertices (0, 0), (1, 0), and (0, 2) the vertices argument becomes:

# In[17]:


#OKPY_SOLUTION

def triangle_area(vertices):
    # nb. vertices = {v1: (x,y)}
    x2y3 = vertices[2][0] * vertices[3][1]
    x3y2 = vertices[3][0] * vertices[2][1]
    x1y3 = vertices[1][0] * vertices[3][1]
    x3y1 = vertices[3][0] * vertices[1][1]
    x1y2 = vertices[1][0] * vertices[2][1]
    x2y1 = vertices[2][0] * vertices[1][1]
    return .5*(x2y3 - x3y2 - x1y3 + x3y1 + x1y2 - x2y1)

print(triangle_area({1: (0,0), 2: (1,0), 3: (0,1)}))


# In[18]:


ok.grade('question-7_3')


# ## String manipulation

# In[19]:


s = "Berlin: 18.4 C at 4 pm"


# Strings behave much like lists/tuples - they are simply a sequence of characters:

# In[20]:


print("s[0] = ", s[0])
print("s[1] = ", s[1])


# Substrings are just slices of lists and arrays:

# In[21]:


# from index 8 to the end of the string
print(s[8:])


# In[22]:


# index 8, 9, 10 and 11 (not 12!)
print(s[8:12])


# In[23]:


# from index 8 to 8 from the end of the string
print(s[8:-8])


# You can also find the start of a substring:

# In[24]:


# where does "Berlin" start?
print(s.find("Berlin"))


# In[25]:


print(s.find("pm"))


# In[26]:


print (s.find("Oslo"))


# In this last example, Oslo does not exist in the list so the return value is -1.

# We can also check if a substring is contained in a string:

# In[27]:


print ("Berlin" in s)


# In[28]:


print ("Oslo" in s)


# In[29]:


if "C" in s:
    print("C found")
else:
    print("C not found")


# ### Search and replace
# Strings also support substituting a substring by another string. In general this looks like *s.replace(s1, s2)*, which replaces string *s1* in *s* by string *s2*, *e.g.*:

# In[30]:


s = s.replace(" ", "_")
print(s)


# In[31]:


s = s.replace("Berlin", "Bonn")
print(s)


# In[32]:


# Replace the text before the first colon by 'London'
s = s.replace(s[:s.find(":")], "London")
print(s)


# Notice that in all these examples we assign the new result back to *s*. One of the reasons we are doing this is strings are actually constant (*i.e* immutable) and therefore cannot be modified *inplace*. We **cannot** write for example:
# 
# ```python
# s[18] = '5'
# TypeError: "str" object does not support item assignment```

# We also encountered examples above where we used the split function to break up a line into separate substrings for a given separator (where a space is the default delimiter). Sometimes we want to split a string into lines - *i.e.* the delimiter is the [carriage return](http://en.wikipedia.org/wiki/Carriage_return). This can be surprisingly tricky because different computing platforms (*e.g.* Windows, Linux, Mac) use different characters to represent a carriage return. For example, Unix uses '\n'. Luckly Python provides a *cross platform* way of doing this so regardless of what platform created the data file, or what platform you are running Python on, it will do the *right thing*: 

# In[33]:


t = "1st line\n2nd line\n3rd line"
print ("""original t =
""", t)


# In[34]:


# This works here but will give you problems if you are switching
# files between Windows and either Mac or Linux.
print (t.split("\n"))


# In[35]:


# Cross platform (ie better) solution
print(t.splitlines())


# ### Stripping off leading/trailing whitespace
# When processing text from a file and composing new strings, we frequently need to trim leading and trailing whitespaces:

# In[36]:


s = "        text with leading and trailing spaces          \n"
print("-->%s<--"%s.strip())


# In[37]:


# left strip
print("-->%s<--"%s.lstrip())


# In[38]:


# right strip
print("-->%s<--"%s.rstrip())


# ### join() (the opposite of split())
# We can join a list of substrings to form a new string. Similarly to *split()* we put strings together with a delimiter inbetween:

# In[39]:


strings = ["Newton", "Secant", "Bisection"]
print(", ".join(strings))


# You can prove to yourself that these are inverse operations:
# ```python
# t = delimiter.join(stringlist)
# stringlist = t.split(delimiter)```

# As an example, let's split off the first two words on a line:

# In[40]:


line = "This is a line of words separated by space"
words = line.split()
print("words = ", words)
line2 = " ".join(words[2:])
print("line2 = ", line2)


# ## Exercise 7.4: Improve a program
# 
# The file [data/densities.dat](data/densities.dat) contains a table of densities of various substances measured in g/cm$^3$. The following program reads the data in this file and produces a dictionary whose keys are the names of substances, and the values are the corresponding densities.

# In[41]:


#OKPY_SOLUTION

def read_densities(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])
    
        if len(words[:-1]) == 2:
            substance = words[0] + ' ' + words[1]
        else:
            substance = words[0]
        
        densities[substance] = density
    
    infile.close()
    return densities

densities = read_densities('data/densities.dat')
print(densities)


# One problem we face when implementing the program above is that the name of the substance can contain one or two words, and maybe more words in a more comprehensive table. The purpose of this exercise is to use string operations to shorten the code and make it more general. Implement the following two methods in separate functions `read_densities_join` and `read_densities_substrings`, and control that they give the same result.
# 
# 1. Let *substance* consist of all the words but the last, using the join method in string objects to combine the words.
# 2. Observe that all the densities start in the same column file and use substrings to divide line into two parts. (Hint: Remember to strip the first part such that, e.g., the density of ice is obtained as *densities['ice']* and not *densities['ice     ']*.)

# In[42]:


def read_densities_join(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words.pop()) # pop is a list operation that removes the last element from a list and returns it
        substance = "_".join(words) # join the remaining words with _
        densities[substance] = density
    infile.close()
    return densities

def read_densities_substrings(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        density = float(line[12:]) # column 13 onwards
        substance = line[:12] # upto coumn 12
        substance = substance.strip() # remove trailing spaces
        substance = substance.replace(" ", "_") # replace spaces with _
        densities[substance] = density
    infile.close()
    return densities

densities_join = read_densities_join('data/densities.dat')
densities_substrings = read_densities_substrings('data/densities.dat')
print(densities_join)
print(densities_substrings)


# In[43]:


ok.grade('question-7_4')


# In[45]:


ok.score()

