'''
write a python program 
Demonstrate - ATM Pin Number validation.
initialize - pin number is 1234
use while loop 
   - limit is 3 attempts
   - read a input pin number from <STDIN>
   - test - if pin number is correct - display "Pin Number is Valid" - display count
- if all 3 attempts are failed - display "Pin is blocked"
'''

pin = 1234
attempts = 0
while(attempts < 3):
    input_pin = int(input("Enter your ATM pin number: "))
    attempts += 1

    if(input_pin == pin):
        print(f"Pin Number is Valid and count is:{attempts}")
        break

    else:
        print(f"Invalid pin and Attempt count: {attempts}")
        
if pin != input_pin:
    print("Pin is blocked")
