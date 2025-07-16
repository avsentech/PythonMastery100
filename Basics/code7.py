# Code 7: Collect Multiple Inputss in a List
# Goal: Store 5 numbers entered by the user

nums = []
for _ in range(5):
    num = int(input("Enter a number: "))
    nums.append(num)
print("You entered:", nums)

# Conecepts: List, loop, appened
# Flow: [Input 5 times → Append to list → Print full list]