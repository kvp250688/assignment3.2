
# coding: utf-8

# In[5]:


#Write a function to compute 5/0 and use try/except to catch the exceptions

def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exceptionerr:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')


# In[6]:


subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

# Use list comprehension instead of looping over each of the predicates
sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
 print (sentence)

