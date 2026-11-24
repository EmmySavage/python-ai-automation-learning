Customer_name= "Tobi"
Product_name= "Microwave"
Unit_price= 35000
Quantity =2
Payment_status = True
Total=Unit_price*Quantity
print("Customer:",Customer_name)
print("Total amount:",Total)
print(type(Customer_name))
print(type(Product_name))
print(type(Unit_price))
print(type(Payment_status))

balance = 5000
paid= False
print(balance > 0 and paid==False)