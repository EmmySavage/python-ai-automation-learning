total_amount= 60000
amount_paid= 60000
outstanding_balance= total_amount - amount_paid
if outstanding_balance==0:
    print("Fully paid")
elif amount_paid > 0:
    print("Partially paid")
else:
    print("No payment received")