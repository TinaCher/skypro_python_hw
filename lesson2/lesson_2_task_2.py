is_year_leap_str=input("Year:")
is_year_leap=int(is_year_leap_str)
if (is_year_leap % 4 == 0):
    print("Year", is_year_leap,"True")
else: 
    print("Year", is_year_leap,"False")