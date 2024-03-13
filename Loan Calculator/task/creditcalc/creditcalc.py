import sys
import math

mode = False
principal = False    
payment = False      
periods = False      
interest = False     
overpayment = False

list_array = len(sys.argv)

for x in range(list_array):

    if "--type=" in sys.argv[x]:
        input_1 = sys.argv[x]
        mode = input_1.split('=')[1]
    if "--payment=" in sys.argv[x]:
        input_2 = sys.argv[x]
        payment = float(input_2.split('=')[1])
    if "--principal=" in sys.argv[x]:
        input_3 = sys.argv[x]
        principal = float(input_3.split('=')[1])
    if "--periods=" in sys.argv[x]:
        input_4 = sys.argv[x]
        periods = int(input_4.split('=')[1])
    if "--interest=" in sys.argv[x]:
        input_5 = sys.argv[x]
        interest = float(input_5.split('=')[1]) / (12 * 100)

if len(sys.argv) < 5:
    print("Incorrect Parameter")
elif principal < 0 or payment < 0 or periods < 0 or interest <= 0 or mode != "annuity" and mode != "diff":
    print("Incorrect Parameter")
elif mode == 'diff' and payment:
    print("Incorrect Parameter")

elif mode == 'diff' and principal and interest and periods:
    overpayment = -principal

    for current_payment in range(1, periods + 1):
        D = math.ceil((principal / periods) + (interest * (principal - (principal * (current_payment - 1)) / periods)))
        print(f"Month {current_payment}: payment is {D}")
        overpayment += D
    print(f"\nOverpayment = {overpayment}")

elif mode == "annuity" and periods and interest and payment:
    principal = math.ceil(payment / ((interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1)))
    print("Your loan principal =", principal)
    print("Overpayment = ", math.ceil((payment * periods) - principal))

elif mode == "annuity" and periods and interest and principal:
    payment = math.ceil(principal * (interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))
    print("Your monthly payment = ", payment)
    print("Overpayment = ", math.ceil((payment * periods) - principal))

elif mode == "annuity" and principal and interest and payment:
    periods = math.ceil(math.log(payment / (payment - interest * principal), interest + 1))
    if periods % 12 == 0:
        print("It will take ", int(periods / 12), " years to repay this loan")
    else:
        if periods < 12:
            print("It will take ", int(periods), " months to repay this loan")
        else:
            print("It will take ", math.floor(periods / 12), " years and ", periods % 12, " months to repay this loan")
    print("Overpayment = ", math.ceil((payment * periods) - principal))

else:
    print("Invalid Parameter")
