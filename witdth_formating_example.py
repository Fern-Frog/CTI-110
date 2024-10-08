# Width formattting using the f-string

print("Money is life.......")
print("^*" * 25)

# Display heading row
expense_name = "EXPEMSE NAME"
print(f"{expense_name:<18} {'MONTHY COST':<18} {'ANNUAL COST':<}\n")

# Display the rest of the rows
month_phone = 107.873521
annual_phone = month_phone * 12
print(f"{'Phone Bill':<18} ${month_phone:<17,.2f} ${annual_phone:<,.2f}")

month_rent = 500000.34325
annual_rent = month_rent * 12 
print(f"{'Rent':<18} ${month_rent:<17,.2f} ${annual_rent:<,.2f}")

month_electric = 5264.435
annual_electric = month_electric * 12
print(f"{'Electric':<18} ${month_electric:<17,.2f} ${annual_electric:<,.2f}")

print("^*" * 25)
