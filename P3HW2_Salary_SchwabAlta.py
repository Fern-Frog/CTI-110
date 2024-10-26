# Alta Schwab
# 10/24/2024
# P3HW2
# Calculate reg and OT pay, given an employees hours worked

'''
OT is more than 40 hours work
any OT hours paid is 1.5 time the reg pay rate

Input: get the name as a string
Input: get the hours as a Integer
Input: get the pay rate as a float

Output: print the employee name

If hours is greater than 40
    Calculate any OT hours work (OT hours = toal hours - 40)
    Calculate OT pay (OT pay = OT hours *(pay rate  * 1.5) )
    Calculate reg pay (40 * pay rate )
    Calculate gross pay (OT pay + reg pay)
    
Else (employee work 40 or less hours)
    OT hours = 0
    Ot pay = 0
    Calculate reg pay = hours * pay rate
    gross pay = reg pay

Output:
Display toal hours work
Display regular pay rate
Dipay overtime hours work
Display overtime pay (OT * OT pay rate)
Display regular pay for regular hours
Display gross pay (OT pay + reg pay)

'''

# Get the input from the user
name = input("Enter employee's name: ")

total_hours = int(input("Enter number of hours worked: "))

pay_rate = float( input ("Enter employee's pay rate: "))

print()

# The if else with the cal.

if total_hours > 40:
    OT_hours = total_hours - 40
    OT_pay = OT_hours * (pay_rate * 1.5)
    reg_pay = 40 * pay_rate
    gross_pay = OT_pay + reg_pay
else: # employee work 40 or less hours
    OT_hours = 0
    OT_pay = 0
    reg_pay = total_hours * pay_rate
    gross_pay = reg_pay
    

print("--"*20)
# display name 
print(f"Employee name: {name}\n")



# display tiles
print(f"{'Hours Worked':<15} {'Pay Rate':<15} {'OverTime':<15} {'OverTime Pay':<15} {'RegHour Pay':<15} {'Gross Pay':<15}")
print("--"*50)

# display numbers
print(f"{total_hours:<15} {pay_rate:<15} {OT_hours:<15} ${OT_pay:<15.2f} ${reg_pay:<15.2f} ${gross_pay:<15.2f}")


    
    



