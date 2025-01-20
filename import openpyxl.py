import openpyxl
r = 12
# Function to calculate modulus of increasing powers of 8 by 391
def calculate_mod():
    mod_list = []
    power = 1
    while power <= (176*2):  # Change 10 to desired number of powers
        mod = (r ** power) % 391
        mod_list.append(mod)
        power += 1
    return mod_list

# Create a new Excel workbook
wb = openpyxl.Workbook()

# Select the active worksheet
ws = wb.active

# Write the mod of increasing powers of 8 by 391
mod_values = calculate_mod()
for i, mod in enumerate(mod_values):
    ws.cell(row=i+1, column=1, value=mod)

# Save the workbook
wb.save("mod_values.xlsx")
