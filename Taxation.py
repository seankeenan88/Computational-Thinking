income = float(input("Enter your annual income: "))

tax = 0.0

if income >= 55000:
    tax = income*0.2
    print('Your gross pay is: ', income)
    print('The full tax rate in Ireland is 20%, so your tax paid is: ', tax)
    print("Your final net pay (after tax) is:", income - tax)

elif income<= 25000:
    tax == 0
    print('Your income is too low to qualify for standard tax rate.')


#else:
   # tax=(income-30000)*0.2 
#tax = round(tax,0) 









