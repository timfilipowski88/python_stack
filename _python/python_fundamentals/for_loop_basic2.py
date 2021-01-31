# Assignment: For Loop Basic II
# Objectives:
# Get comfortable writing functions only using basic building blocks of Python(i.e. using your own skills rather than relying on built-ins)
# Get comfortable using for loops, functions, lists, and other data types

#1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now[-1, "big", "big", -5]
def biggie_size(big_list):
    for x in range(len(big_list)):
        if big_list[x] > 0:
            big_list[x] = "big"
    return big_list


biggie_size([-1, 3, 5, -5])

#2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1, 1, 1, 1]) changes the original list to[-1, 1, 1, 3] and returns it
# Example: count_positives([1, 6, -4, -2, -7, -2]) changes the list to[1, 6, -4, -2, -7, 2] and returns it
def count_positives(org_list):
    pos_list = []
    for x in range(len(org_list)):
        if org_list[x] > 0:
            pos_list.append(org_list[x])
    org_list.pop()
    org_list.append(len(pos_list))
    return org_list

count_positives([-1, 1, 1, 1])


#3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1, 2, 3, 4]) should return 10
# Example: sum_total([6, 3, -2]) should return 7
def sum_total(start):
    total = 0
    for x in start:
        total += start[x]
    return total


sum_total([1, 2, 3, 4])
sum_total([6, 3, -2])

#4 Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1, 2, 3, 4]) should return 2.5
def Average(list):
    total = 0
    for x in list:
        total += x
    return float(total) / float(len(list))


print(Average([1, 2, 3, 4]))

#5 Length - Create a function that takes a list and returns the length of the list.
# Example: length([37, 2, 1, -9]) should return 4
# Example: length([]) should return 0
def length(list):
    count = 0
    for x in list:
        count +=1
    return count


length([37, 2, 1, -9])
length([])

#6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37, 2, 1, -9]) should return -9
# Example: minimum([]) should return False
def minimum(list):
    if len(list) > 0:
        min = 0
        for x in list:
            if x < min:
                min = x
        return min
    else:
        return False

minimum([37, 2, 1, -9])
minimum([])

#7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37, 2, 1, -9]) should return 37
# Example: maximum([]) should return False
def maximum(list):
    if len(list) > 0:
        max = 0
        for x in list:
            if x > max:
                max = x
        return max
    else:
        return False


maximum([37, 2, 1, -9])
maximum([])


#8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37, 2, 1, -9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4}
def ultimate_analysis(lst):
    ult_list = {
        'sumTotal': 0,
        'average': None,
        'minimum': lst[0],
        'maximum': lst[0],
        'length': 0
    }
    if len(lst) < 1:
        return 
    else:    
        for x in lst:
            ult_list['length'] +=1
            ult_list['sumTotal'] += x
            ult_list['average'] = ult_list['sumTotal'] / ult_list['length']
            if x > ult_list['maximum']:
                ult_list['maximum'] = x
            elif x < ult_list['minimum']:
                ult_list['minimum'] = x
        return ult_list


ultimate_analysis([37, 2, 1, -9])



#9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37, 2, 1, -9]) should return [-9, 1, 2, 37]
def reverse_list(lst):
    lst_len = len(lst)
    for x in range(int(lst_len/2)):
        temp = lst[x]
        lst[x] = lst[lst_len-1-x]
        lst[lst_len-1-x] = temp
    return lst

reverse_list([37, 2, 1, -9])

