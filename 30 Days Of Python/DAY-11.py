def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(1,1))




def area_of_circle(radius:float):
    return 3.14 * (radius * radius)
print(area_of_circle(5))



#I'm still confused in this part
def add_all_nums(*args):
    #only integer values are accepted in this return value 
    #when string is mixed in the parameter value it will cause error in the code.
    return sum(args)
print(add_all_nums(1, 2, 3, 4, 5))



def convert_celsius_to_farenheit (celsius):
    return celsius * (9 / 5) + 32
print(convert_celsius_to_farenheit(38))




summer = ['January', 'February', 'March', 'April', 'May']
rain = ['June', 'July', 'August', 'September', 'October', 'November', 'December']
def check_season(month):
    if month in summer:
        return 'Summer'
    elif month in rain:
        return 'Rainy'
    else:
        return 'Wrong Month, Please Try Again. '
print(check_season('December'))   


