# B_R_R
# M_S_A_W


"""
What is the logic behind for loop and range functions, how do they work?

nums=my_range(1,15)
for num in nums:
    print(num)
1
2
3
4
5
...
Actually to grasp how they work we have to get hang of how iterators, iterables and generators work.
We will have a look on iterator first
then generator
"""


# nums=my_range(1,15)
# for num in nums:
#     print(num)



# In order the above code to function we have to define my_range by creation class
class MyRange:

    def __init__(self, start, end):
        self.value=start
        self.end=end


    def __iter__(self):
        return self

    def __next__(self):
        if self.value>=self.end:
            raise StopIteration
        current=self.value
        self.value+=1
        return current


nums=MyRange(1,15)
for num in nums:
    print(num)

print("""
Now
Let's
Take
A 
Look
of
Generators
""")

def my_range(start,end):
    current=start
    while current<end:
        yield current
        current+=1

nums_2=my_range(15,25)
for numb in nums_2:
    print(numb)
