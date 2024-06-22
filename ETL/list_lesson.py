#the conditional expression you are trying to use in the key part of the dictionary comprehension is not allowed. 
# In Python, the ternary conditional operator can only be used for values, not keys.
dict3 = {key2: key2**2 if key2 % 2==0 else key2**3 for key2 in range(1,15)}
dict4 = {key2: (key2**2 if key2 % 2==0 else key2**3) for key2 in range(1,15)}
print(dict4)
print(dict3)

tup1_0 = ("welcome", "to", "the", "world", "of", "python")
print(tup1_0[-2:0:-1])
print(tup1_0[-2:-6:-1])
print(tup1_0[1:5])
