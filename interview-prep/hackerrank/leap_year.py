def is_leap(year):
    leap = False
    if year % 4 ==0 and year % 400 !=100:
        leap = True
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))