# my_person = {
#     "name": "ethan",
#     "age": "16",
#     "language": "english"
# }

# for person in my_person:
#     print("who are you" ),
# if my_person =="name":
#     print("hello ethan" ),


# avengers_404 = {
#     "Ethan": "Mac",
#     "Marvelous": "Asus",
#     "Pierre": 'Lenovo',
#     "Ronny": "Asus"
# }

# for class_mate in avengers_404.items():
#     if class_mate == "Mac":
#         print(f"{class_mate} the apple guy.")
#     elif class_mate == "Asus":
#         print(f"{class_mate}, I heard it's a good brand.")
#     elif class_mate == 'Lenovo':
#         print(f"{class_mate}, you got something unique.")
#     elif class_mate == "Asus":
#         print(f"{class_mate}, is a copy cat.")

avengers_404 = {
    "Ethan": "Mac",
    "Marvelous": "Asus",
    "Pierre": "Lenovo",
    "Ronny": "Asus"
}

for name, brand in avengers_404.items():  # Unpacking key-value pair
    if brand == "Mac":
        print(f"{name} uses {brand}, the apple guy.")
    elif brand == "Asus":
        print(f"{name} uses {brand}, I heard it's a good brand.")
    elif brand == "Lenovo":
        print(f"{name} uses {brand}, you got something unique.")

       