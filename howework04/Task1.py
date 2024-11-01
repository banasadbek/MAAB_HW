def convert_cel_to_far(celcius: float):
 fahrenheit = celcius * 9/5 + 32
 return fahrenheit

def convert_far_to_cel(fahrenheit: float):
 celcius = (fahrenheit - 32) * 5/9
 return celcius

degree_in_fahrenheit = float(input('Enter the degrees in fahrenheit: '))
print(f'{degree_in_fahrenheit} degrees F = {round(convert_far_to_cel(degree_in_fahrenheit), 2)} degrees C')

degree_in_celcius = float(input('Enter the degrees in celcius: '))
print(f'{degree_in_celcius} degrees C = {round(convert_cel_to_far(degree_in_celcius), 2)} degrees F')
