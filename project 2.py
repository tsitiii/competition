print("welcome to tip calculator!")
bill=float(input("how much is ur total bill? $"))
tip=int(input("what percentage of tip u want to give?"))
freinds= int(input("to how many ppl are u going to split the bill?"))    
total_tip=bill*tip/100
total_bill= total_tip + bill
each=total_bill/freinds      
print("total bill is", total_bill)
print("each person pays",round(each,2))
print("relation is complication"[4])
