''' Duong Lam U68618275 Wind Chill Temperature
This app allows you to input temperature, wind speed inorder to calculate 
Wind-chill temperatures.
'''


#windspeed = int(input("Enter the Wind speed:"))
temp = int(input("Enter the temperature in Fahrenheit:"))

if temp not in range(-58,42):
  while temp not in range(-58,42):
    print("Temperature must be between -58F and 41F")
    temp = int(input("Re-enter the temperature in Fahrenheit:"))
if temp in range(-58,42):
  windspeed = int(input("Enter the speed of wind in mph:"))

while windspeed < 2:
  print("Speed must be greater than or equal to 2mph")
  windspeed = int(input("Re-enter the speed of wind in mph:"))

if windspeed >= 2:
  twe = 35.74 + (0.6215 * temp) - (35.75 * (windspeed**0.16)) +(0.4275 * temp * (windspeed ** (0.16)))
  twe = f'{twe:.1f}'                                                                      
  print(f'The wind chill index is {twe} mph!')


 
      
  


    







  
    
    



     
    
