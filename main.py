import datetime
import paygroup

#input of pay date
print('Welcome to RenPay\nPress enter to begin')
input()
error = 0
while error == 0:
    print('Enter a pay date(yyyy/mm/dd): ')
    date_input = input()
    pay_year, pay_month, pay_day = map(int, date_input.split('/'))
    pay_date = datetime.date(pay_year, pay_month, pay_day)
    today_string = str(datetime.date.today())
    today_year, today_month, today_day = map(int, today_string.split('-'))
    today_date = datetime.date(today_year, today_month, today_day)

    quarter_one_month = 3
    quarter_two_month = 6
    quarter_three_month = 9
    quarter_four_month = 12

    month_diff = pay_month - today_month
    year_diff = pay_year - today_year
    day_diff = pay_day - today_day
    if year_diff == 0:
        if today_month > quarter_one_month:
            if today_month > quarter_two_month:
                if today_month > quarter_three_month:
                    if today_month > quarter_four_month:

        else:
            error += 0
            print('Prior quarter pays are invalid')

    else:
        error = 0
        print('Prior year pays are not valid')
#input of employee number
print('Enter the employee identifier number: ')
emp_num = int(input())
#input of pay group
print('Enter the code for pay group the employee is in: ')
pay_group = input()
#input of hours
print('Enter the hours worked: ')
hours = int(input())
#input check type
print('Direct Deposit or Paper Check(D/C): ')
choice = input()
if choice == 'D':
    check_type = 'Direct Deposit'
else:
    check_type = 'Check'
#calc hours

if hours < 40:
    reg_pay = 20.00 * hours
    ot_pay = 0.00

#calc ot hours
else:
    reg_pay = 800.00
    ot_pay = float(hours-40) * 30.00

full_pay = reg_pay + ot_pay

#print pay check
print('Pay Date: '+pay_date + '                          Employee Number: '+str(emp_num))
print('Pay Group: '+pay_group+'                             Check Type: '+check_type+'\n')
print('Hours: '+str(hours)+'.................................Earnings: '+'$'+'{:.2f}'.format(full_pay))

