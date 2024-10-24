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

