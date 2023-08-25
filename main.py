import datetime
import paygroup

#input of pay date
print('Welcome to RenPay\nPress enter to begin')
input()
print('Enter a pay date(mm/dd/yyyy: ')
pay_date=input()
#input of employee number
print('Enter the employee identifier number: ')
emp_num=int(input())
#input of pay group
print('Enter the code for pay group the employee is in: ')
pay_group=input()
#input of hours
print('Enter the hours worked: ')
hours=int(input())
#input check type
print('Direct Deposit or Paper Check(D/C): ')
choice=input()
if choice == 'D':
    check_type = 'Direct Deposit'
else:
    check_type = 'Check'
#calc hours
reg_pay = float
ot_pay=float
if hours<40:
    reg_pay= 20 * hours

#calc ot hours
else:
    reg_pay= 800
    ot_pay = (hours-40)*30
full_pay=reg_pay+ot_pay

#print pay check
print('Pay Date: '+ pay_date + '                          Employee Number: '+ str(emp_num))
print('Pay Group: '+pay_group+'                             Check Type: '+check_type+'\n')
print('Hours: '+str(hours)+'.................................Earnings: '+str(full_pay))
