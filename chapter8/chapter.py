# def my_name(user, age):
#     print(f"welocme back {user}! It must be nice to be {age} years old...")

# my_name(input("May I have your name please: "), input("How old are you: "))

# def my_laptop(open,cup):
#     print(f"it is awesome to  student in {open}, what was your teacher name{cup} ")
# my_laptop(input("where did you learn that?"), input("who is your teacher?" ))   

def my_laptop(open, cup):
    return f"It is awesome for students in {open}. What was your teacher's name? {cup}"

result = my_laptop(input("Where did you learn that? "), input("Who is your teacher? "))
print(result)



# def my_lyf(first_name, wud , outside, college, year = 2025):
#     return f"Name's {first_name}, right now I'm doing the {wud}. We gotta be {outside}. I'm in {college}, doing my first year in {year}."

# personal_info = my_lyf("ethan", "Doing the python", "inside", "code college", )

# print(personal_info)



# my_list = [1, 2, 3, 4, 5]

# copied_list = None

# def my_test_function(list):
#     copied_list = list.reverse()
#     print(list)

# my_test_function(my_list[:])

# print(my_list)
# print(copied_list)