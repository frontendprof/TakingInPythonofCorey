# B_R_R
# M_S_A_W


"""
Codes and snippets below is taken from the video of "Python Tutorial: Iterators and Iterables - What Are They and How Do They Work?" by
Corey Schafer.
So we look some logic behind some of built-in functions.

"""
What is the logic behind for loop, how do they work?

for num in nums:
    print(num)
a
b
c
d
e
...
Actually to grasp how it works, we have to get hang of how iterators, iterables and generators work.

Iterators have usually has to method __iter__ and __next__
Whereas iterables have only __iter__ method
"""


nums=[1,2,3,4,5,6,7,8]

i_nums=iter(nums) # Now it has become iterator
print((i_nums))

while True:
    try:
        item=next(i_nums) #As it is iteration, it knows how to handle next method.
        print(item)
    except StopIteration:
        break
