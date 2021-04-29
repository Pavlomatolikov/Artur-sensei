""" Task 2: Create function to print numbers which contains specific digit 
the function must support top and bottom range
"""

print("This program prints numbers which contains specified number in specified range")
def magic(a = input("Enter start of range, needed number and end of range separated by white space: ").split()):
    try:
        b = list(map(int, a))
    except:
        print ("You are a piece of shit, you were asked to enter numbers!!!")
        a = input("Enter start of range, needed number and end of range separated by white space: ").split()
    else:
        my_list = [str(i) for i in range(b[0], b[2])]
        list_to_print = []
        for i in my_list:
            if a[1] in i: list_to_print.append(i)
        list_to_print = list(map (int, list_to_print))
        print(list_to_print)
    
magic()