#!/usr/bin/env python
# coding: utf-8
# Q1. Create one variable containing following type of data:
(i) string
(ii) list
(iii) float
(iv) tuple

# In[13]:


#1 string
A = "welcome to PW skills "
type(A)


# In[10]:


#2. list
B = [1,2,3,2.3,(3+5j),True,"Honey"]
type(B)


# In[11]:


#3 float 
C = 2.3455
type(C)


# In[12]:


#4 tuple
D = (1,2,3,4)
type(D)


# Q2. Given are some following variables containing data:
# (i) var1 = ‘ ‘
# (ii) var2 = ‘[ DS , ML , Python]’
# (iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
# (iv) var4 = 1.
# 
# Answer
# 1. String
# 2. String
# 3. List
# 4. Integer
# 
Q3. Explain the use of the following operators using an example:
(i) /
(ii) %
(iii) //
(iv) ** 
# In[16]:


#1. / = It is known as Division Operator.It gives us Quotient(in float form).
E= 5/3
E


# In[17]:


# 2. % = It is Known as Modulus Operator .it gives us remainder.
F = 5%3
F


# In[18]:


#3. // = It is known as Floor Operator.It gives Quotient (in Integer form).
G = 5//3
G


# In[21]:


#4. ** = It is known as power Operator.it is used when we have to put power on a Number
H = 5**3
H

Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
element and its data type.
# In[29]:


List = [0,1,2,3,4,5,6,7,22,9]
for i in List:
    print(i)


# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

# In[7]:


I = int(input("Enter your dividend: "))
print("Your dividend is:", I)
J = int(input("Enter your divisor: "))
print("your Divisor is: ", J)
count = 0
while I%J ==0:
    count+=1
    I//=J
if count >0:
    print(I, "is Divisible by",J, "in", count,"times")
else:
    print(I, "is not Absolute divisible by ",J)
    


# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.

# In[3]:


List = []
for i in range(25) :
    K = int(input("Enter numbers: "))
    List.append(K)
    if K % 3 == 0:
        print(K,"is divisible by 3")
    else:
        print(K ,"is not Divisible by 3")
print(List)
 
    


#  Q7. What do you understand about mutable and immutable data types? Give examples for both showing this property.
# 
# Answer:
# Mutable Data Type = A Mutable object can be changed after it's creation.
# Example : List, Set etc.
# 
# Immutable Data Type = A Immutable Object cannot be changed after it's creation.
# Example: string, Tuple etc.
# 
# 

# In[10]:


##Mutable Data type
k = [1,3,2,5,32,444,5]
k[2] = 9
k


# In[11]:


##Immutable Data type
x= (1,3,2,5,32,444,5)
x[2] = 9
x


# In[ ]:




