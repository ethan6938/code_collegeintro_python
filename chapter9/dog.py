# class Dog:
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over!")

# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 3)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()



# class team:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         return f"Hello, my name is {self.name}!"
    
#     def have_birthday(self):
#         self.age += 1
#         return f"Happy Birthday! You are now {self.age} years old."

# # Example usage
# person1 = team("Alice", 25)
# print(person1.greet())  # Output: Hello, my name is Alice!
# print(person1.have_birthday())  # Output: Happy Birthday! You are now 26 years old.



class Team:
    team_name = "404 Avengers"  # Fixed team name

    def __init__(self):
        self.members = []  # List to store team members

    def add_member(self, name, role):
        """Adds a new member to the team."""
        self.members.append({"name": name, "role": role})
        print(f"{name} has joined {self.team_name} as a {role}!")

    def show_roster(self):
        """Displays the team members."""
        if not self.members:
            print(f"{self.team_name} has no members yet!")
        else:
            print(f"\n🏆 {self.team_name} Roster:")
            for i, member in enumerate(self.members, start=1):
                print(f"{i}. {member['name']} - {member['role']}")

    def battle_cry(self):
        """Prints the team's battle cry!"""
        print(f"{self.team_name} assembles! 💥 'We debug the chaos!'")

# Example Usage
team = Team()
team.add_member("Ethan", "Researcher")
team.add_member("Ronny", "Strategist")
team.add_member("Marvelous", "Tester")
team.add_member("Pierre", "Tech Wizard")

team.show_roster()
team.battle_cry()





# class Person:
#     def __init__(self, name, age, team):  
#         self.name = name
#         self.age = age
#         self.team = team

#     def greet(self):
#         return f"Hello, {self.name} here! Nice to meet you ✌🏽!"

#     def how_old_are_you(self):
#         return f"WOW, you're old! You're {self.age} years old."

#     def team_name(self, new_team):
#         old_team = self.team
#         self.team = new_team
#         return f"{self.name} has switched from {old_team} to {new_team}."

# # Example usage
# person1 = Person("Pierre", 218, "404 Avengers")

# print(person1.greet())
# print(person1.how_old_are_you())
# print(person1.team_name("Stack overflow"))
# print(person1.team_name("Function Junction"))
# print(f"Current Team: {person1.team}")
