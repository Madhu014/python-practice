#Write a program to separate positive and negative number from a list.

num_list=[1,2,67,8,4,-3,-7-55,-100]
positive_list=[]
negative_list=[]
for i in num_list:
    if i>0:
        positive_list.append(i)
    else:
        negative_list.append(i)
print("positive_numbers:",positive_list)
print("negative_numbers:",negative_list)