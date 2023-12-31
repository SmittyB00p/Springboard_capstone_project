#function that takes in a number greater than 1 and makes it into a list of that length
def create_num_list(num=1):
    #returns 0 if the input was 0
    if num == 0:
        return num
    
    num_list = []

    #while the number is greater than 0 the while loop will add the number to the num_list, decrease the number and do that until it is less than 0
    while num > 0:
        num_list.append(num)
        num -= 1

    reversed_list = sorted(num_list)
    return reversed_list


print(create_num_list(10))