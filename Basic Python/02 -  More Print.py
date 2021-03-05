# Format String

first_name = "John"
second_name = "Doe"
city = "London"
age = 50 
height = 1.80 #m
weight = 90 #kg

print(f"Hello I'm {first_name} {second_name},\
 I'm {age} years old and I live in {city} I'm {height}m and weight {weight}kg") 
# a '\' breaks the line

# Concatenating "+"

she = "Jane Doe"
he = "John Doe"

print(she +" and "+ he,"live together")

# Format String

print(f"{she} e {he} are married")

# Format String

sched = "Did you scheduled the appointment? {}"
status = "I didn't"

print(sched.format(status))

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4)) 
