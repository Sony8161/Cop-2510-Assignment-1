#Duong Lam U#68618275 Ingredient Adjuster
''' This program allows you to input a certain amount of cookies you would like to make, and the script will run 
to give you exactly measurements for the ingredients needed to make the number of cookies you want.

'''
main_sugar = (1.5)
main_butter = (1)
main_flour = (2.75)
pre_total_cookies = (48)

Cookies_main = int(input("Enter the number of cookies you want to make: "))
print (f'To make {Cookies_main} cookies, you will need:')


sugar1 = (main_sugar / 48)
butter1 = (main_butter / 48)
flour1 = (main_flour / 48)

needed_sugar = round((sugar1 * Cookies_main),2)

needed_butter = round((butter1 * Cookies_main),2)

needed_flour = round((flour1 * Cookies_main),2)

print (f'{needed_sugar} cups of sugar')
print (f'{needed_butter} cups of butter')
print (f'{needed_flour} cups of flour')
 