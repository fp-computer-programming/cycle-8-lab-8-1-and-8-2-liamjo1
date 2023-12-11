"""
Create a Python file named lab_8-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***
Create a Python file named lab_8-1
Write a function in that uses the for loop and the range function to find the sum of all the numbers up to and including the number the user input
The function should return the final total of the sum of all of the items in the list
Add a statement that prompts the user to input an integer
Call the function from step 2 and store its output as a variable
Add a statement to print the variable to see the final sum

__________________________________________________________

Create a Python file named lab_8-2

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a function that will take a list of names and write the body of an email to invite them to a party
The body should be something like this: "Hi name, You're invited to my party on Friday!" Where name is the name of each person in the list.
The function should use a for loop and print each invitation after it is generated. There should be at least 3 names in the list.



"""
# Liam O'Hara

def calculate_sum(n):
    """
    Calculates the sum of numbers up to and including the given integer.
    """
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

# Input to get integer
user_input = int(input("Enter an integer: "))

# Find the sum using defined input
result_sum = calculate_sum(user_input)

# Print the answer or sum
print(f"The sum of numbers up to {user_input} is: {result_sum}")

def generate_party_invitations(names):
    """
    prints party invitation with the persons name in the email.

    """
    for name in names:
        invitation = f"Hi {name}, You're invited to my party on Friday!"
        print(invitation)

# list of names:
names_list = ["Matt", "Dylan", "Michael"]

# Generate party invites
generate_party_invitations(names_list)