# username = input("what is your username")
# passion_one = input("what is your first passion")
# passion_two = input("what is your second passion")
# passion_three = input("what is your third passion")
# my_passion = [passion_one, passion_two, passion_three]

# print(f"welcom to your python code{username}.\nHere is list of your passion:\nPassion one:{my_passion[0]}\nPassion two: {my_passion[1]}\nPassion three: {my_passion[2]}")

# my_wins = 5
# my_loes = 10 

# while my_wins =
#     promt= ("weldone")

# the_road = 5 
# my_id = "ronny"

# while the_road == 5:
#     if the_road == 5:
#        print("great option dude")
#     elif the_road != 5:
#        print("rubbish") 
#     break



the_road = 5 
my_id = "ronny"

while True:  # Infinite loop (until we break)
    if the_road == 5:
        print("great option dude")
        the_road = 4  # Change value so the next condition can be checked
    elif the_road != 5:
        print("rubbish")
        the_road = 5  # Change it back so the loop alternates
    break
    # Pause so output is readable (optional)
    import time
    time.sleep(1)  # Wait 1 second before the next loop iteration
