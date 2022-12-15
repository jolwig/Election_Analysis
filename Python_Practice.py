#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county, voters in counties_dict.items():
    #print(county + "county has " + str(voters) + " registered voters")



# Create a variable called 'name' that holds a string
name = "jake"

# Create a variable called 'country' that holds a string
country = "USA"

# Create a variable called 'age' that holds an integer

age = 250

# Create a variable called 'hourly_wage' that holds an integer

hourly_wage = 15

# Calculate the daily wage for the user

workday = 8
daily_wage = hourly_wage * workday 

# Create a variable called 'satisfied' that holds a boolean

satisfied = True

# Print out "Hello <name>!"

print(f"Hello {name}!")

# Print out what country the user entered

print(country)

# Print out the user's age

print(age)

# With an f-string, print out the daily wage that was calculated

print(f"your daily wage is {daily_wage}")

# With an f-string, print out whether the users were satisfied


# Create a Python list to store your grocery list

grocery_list = ["bananas", "bacon", "butter", "eggs"]

# Print the grocery list

print(grocery_list)

# Change "Peanut Butter" to "Almond Butter" and print out the updated list

grocery_list[2] = "Almond Butter"

# Remove "Jelly" from grocery list and print out the updated list

grocery_list.remove("eggs")
print(grocery_list)

# Add "Coffee" to grocery list and print the updated list

grocery_list.append("Coffee")
print(grocery_list)


my_dict = {"name" : "Bean", 
            "hobbies" : ["meowing", "scratching", "jumping"],
            "age" : 2 
            "fav hobby" : "meowing", 
            "wake up" : "2AM"
        }

print(f'{my_dict.values(name)} is my pets name and {my_dict.values(age)} is her age')