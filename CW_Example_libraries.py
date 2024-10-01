# In-class example of using built-in libraries

# Import datatime librarys so it can be used in the program
import datetime

import random

# Get current date and time
curr_time = datetime.datetime.now()

# Display data and time
print(f"The current date and time is {curr_time}")

# Generate random numbers
random_1 = random.randint(1, 10)
random_2 = random.randint(1, 10)

#Display the random values
print(f"{random_1} plus {random_2} equals {random_1 + random_2}")
