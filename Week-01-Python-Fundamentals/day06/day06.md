Day 6: While Loops in Python
What I Learned
Today, I learned about while loops in Python.
A while loop repeats a block of code as long as a given condition remains True.
Unlike a for loop, which is commonly used to iterate through a sequence or repeat a known number of times, a while loop is condition-based.
1. Basic While Loop
balance = 60000

while balance > 0:
    print("Customer still owes money")
    balance = balance - 10000
Explanation
while starts the loop.
balance > 0 is the condition.
Python executes the indented instructions while the condition is True.
balance = balance - 10000 reduces the balance after every repetition.
When the balance reaches zero, the condition becomes False and the loop stops.
2. Countdown Example
number = 10

while number > 0:
    print(number)
    number = number - 1
Output
10
9
8
7
6
5
4
3
2
1
3. Stock Management Example
blender_stock = 5

while blender_stock > 0:
    print("Blender sold")
    blender_stock = blender_stock - 1

print("Out of stock")
This program reduces the available stock each time a blender is sold.
When the stock reaches zero, the loop stops and displays Out of stock.
4. Infinite Loops
An infinite loop occurs when a loop continues running without reaching a stopping condition.
Example:
balance = 60000

while balance > 0:
    print("Customer still owes money")
The problem is that the balance never changes. Therefore, the condition remains True.
To stop a running Python program in the terminal, press Ctrl + C.
5. Important Things I Learned
A while loop repeats instructions based on a condition.
The loop stops when its condition becomes False.
Variables can be updated inside loops.
Forgetting to update a variable can cause an infinite loop.
Indentation determines which instructions belong inside the loop.
6. Practical Exercises
Create a countdown from 10 to 1.
Create a customer payment loop that reduces an outstanding balance.
Create a stock management loop that reduces product stock until it reaches zero.
Summary
Today, I learned how to use while loops to repeat instructions based on conditions. I also learned about infinite loops and why updating variables is important.
Next Topic: Day 7 — Functions in Python.