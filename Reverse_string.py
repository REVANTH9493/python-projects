# using string slicing with very less time complexity is one of the solution for reversing a string

def rev_str(string):
    new_string = string[::-1]
    return new_string

# using for loop for reversing a string

def loop(string):
    loop_string = ""
    for char in string:
        loop_string= char + loop_string
    return loop_string

string = input("")
# string = input("Enter any string: ")
print("using string slicing method: ",rev_str(string))
str = loop(string)
print("using loop method: ",str)

