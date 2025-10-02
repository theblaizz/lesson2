def is_year_leap(year):

 def is_year_leap(year):
   return year % 4 == 0
 else: 
   return False
 
# Пример вызова функции 
year_to_check = 2000
result = is_year_leap(year_to_check)
print(f"год {year_to_check}: {result}")

# Пример вызова функции 
year_to_check = 2003 
result = is_year_leap(year_to_check)

print(f"год {year_to_check}: {result}")

# Пример вызова функции 
year_to_check = 2007 
result = is_year_leap(year_to_check)

print(f"год {year_to_check}: {result}")