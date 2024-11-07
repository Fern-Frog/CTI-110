# Alta Schwab
# 11/7/2024
# P4HW2
# Add stuff to P3HW2

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
#The Incrementer variables
total_employees = 0
total_overtime = 0
total_reg = 0
total_gross = 0


# Get the input from the user
name = input('Enter employee\'s name or "Done" to terminate: ')

while name.lower() != "done":
    
    total_employees += 1

    total_hours = int(input(f"How many hours did {name} work: "))

    pay_rate = float( input (f"Enter {name} pay rate: "))

    print()

    # The if else with the cal.

    if total_hours > 40:
        OT_hours = total_hours - 40
        OT_pay = OT_hours * (pay_rate * 1.5)
        total_overtime += OT_pay
        reg_pay = 40 * pay_rate
        total_reg += reg_pay
        gross_pay = OT_pay + reg_pay
        total_gross += gross_pay
    else: # employee work 40 or less hours
        OT_hours = 0
        OT_pay = 0
        total_overtime += OT_pay
        reg_pay = total_hours * pay_rate
        total_reg += reg_pay
        gross_pay = reg_pay
        total_gross += gross_pay
    

    # display name 
    print(f"Employee name: {name}\n")

    # display tiles
    print(f"{'Hours Worked':<15} {'Pay Rate':<15} {'OverTime':<15} {'OverTime Pay':<15} {'RegHour Pay':<15} {'Gross Pay':<15}")
    print("--"*50)

    # display numbers
    print(f"{total_hours:<15} {pay_rate:<15} {OT_hours:<15} ${OT_pay:<15.2f} ${reg_pay:<15.2f} ${gross_pay:<15.2f}")

    print()
    name = input('Enter employee\'s name or "Done" to terminate: ')

#End of loop

print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_reg:.2f}")
print(f"Total amount paid for gross: ${total_gross:.2f}")
    
    



