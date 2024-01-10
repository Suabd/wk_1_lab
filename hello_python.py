"""
Write a program that asks for your name and the month you were born in.

Then, your program should print
A greeting to you, using your name
A message with the number of letters in your name
A 'Happy birthday month!' message if you were born in the current month
Easier - compare the user's input to "January" or "August" or whatever the current month is
Harder - use Python to figure out the current month and use that in the comparison. Check out the datetime library."""

from datetime import datetime

today_datetime = datetime.now()
print(today_datetime)
today_month_number = today_datetime.month # 1 for january
print(today_month_number)

current_month_text = today_datetime.strftime('%B') # will write the current month name "January"
print(current_month_text)

name = input('Please enter your name: ')
birthday_month = input('Enter the number of the month with your birthday: ')

print(f'Hello {name}!')

letters_in_name = len(name)

print(f'Your name {name} has {letters_in_name} letters.')  # this prints the name with the number of the letters it has

if birthday_month.lower() == current_month_text.lower():  # accepts lowercase & uppercase answer
    print('Happy birthday month!')
else:
    print('Your birthday is not this month.')


