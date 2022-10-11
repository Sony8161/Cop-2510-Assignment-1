''' Duong lam #68618275 Runway length 

This program allows you to input take off speed, and acceleration in order to determine 
how much runway length is needed for takeoff.
'''
acceleration = int(input("Enter the plane's acceleration in m/s^2="))

take_off_speed = int(input("Enter the plane's take off speed in m/s="))


actual_speed = (take_off_speed * take_off_speed)

actual_acceleration = (acceleration * 2)

length = round(float(actual_speed / actual_acceleration), 4)

print (f"The minimum runway length needed for this airplane is {length} meters.")








