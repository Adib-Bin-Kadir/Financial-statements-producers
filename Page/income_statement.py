# print('Answer the following questions. If you do not have any answers, just type none.')
# currency = input('What is the currency you business operates in?')
# revenue = input('Enter the revenue from the trial balance:')
# return_inwards = input('Enter the value of returns inwards:')
# opening_inventory = input('Enter the value of the opening inventory:')
# purchases = input('Enter the value of purchases:')
# return_outwards = input('Enter the value of the returns outwards:')
# closing_inventory = input('Enter the value of the closing inventory:')
# carriage_inwards = input('Enter the value of the carriage inwards:')
# carriage_outwards = input('Enter the value of the carrigae outwards:')
# expenses = []
# if_expenses = input('Enter any expense occuring in your business:')
# expenses.append(if_expenses)
# a = ''
# if if_expenses.lower() != 'none':
#     while a != 'end':
#         a = input('Type another(type end when done):')
#         expenses.append(a)
# expense_values = []
# for expense, expense_name in zip(range(len(expenses)-1), expenses):
#     expense_value = input('Enter the value of {}:'.format(expense_name))
#     expense_values.append(expense_value)


def calculation_and_output(
        revenue, return_inwards, opening_inventory, closing_inventory, purchases, carriage_inwards,
        carriage_outwards, expenses, expense_values, return_outwards
):
    try:
        details = []
        value_set1 = []
        value_set2 = []
        length_gap = 0
        details.append('Revenue')
        value_set1.append(revenue)
        length_gap += 1
        net_revenue = int(revenue)
        if return_inwards.lower() != 'none':
            details.append('Return inwards')
            value_set1.append('({})'.format(return_inwards))
            length_gap += 1
            net_revenue -= int(return_inwards)
        for index in range(length_gap):
            value_set2.append('')
        details.append('Net Revenue')
        value_set1.append('')
        value_set2.append(str(net_revenue))
        details.append('COST OF SALES')
        value_set1.append('')
        value_set2.append('')
        length_gap = 0
        cost_of_sales = 0
        if opening_inventory.lower() != 'none':
            details.append('Opening inventory')
            length_gap += 1
            cost_of_sales += int(opening_inventory)
            value_set1.append(opening_inventory)
        if closing_inventory.lower() != 'none':
            details.append('Closing inventory')
            length_gap += 1
            cost_of_sales -= int(closing_inventory)
            value_set1.append('({})'.format(closing_inventory))
        if purchases.lower() != 'none':
            details.append('Purchases')
            length_gap += 1
            cost_of_sales += int(purchases)
            value_set1.append(purchases)
        if carriage_inwards.lower() != 'none':
            details.append('Carriage inwards')
            length_gap += 1
            cost_of_sales += int(carriage_inwards)
            value_set1.append(carriage_inwards)
        if return_outwards.lower() != 'none':
            details.append('Returns outwards')
            length_gap += 1
            cost_of_sales -= int(return_outwards)
            value_set1.append(return_outwards)
        for gap in range(length_gap):
            value_set2.append('')
        details.append('Total Cost of Sales')
        value_set2.append('({})'.format(cost_of_sales))
        gross_profit = str(int(net_revenue) - int(cost_of_sales))
        value_set1.append('')
        value_set2.append(gross_profit)
        details.append('Gross Profit')
        value_set1.append('')
        details.append('OPERATING EXPENSES')
        value_set1.append('')
        value_set2.append('')
        length_gap = 0
        total_expenses = 0
        if carriage_outwards.lower() != 'none':
            details.append('Carriage outwards')
            length_gap += 1
            total_expenses += int(carriage_outwards)
            value_set1.append(carriage_outwards)
        if expenses[0].lower() != 'n':
            for item, value in zip(expenses, expense_values):
                details.append(item)
                length_gap += 1
                total_expenses += int(value)
                value_set1.append(value)
        details.append('Total Expenses')
        value_set1.append('')
        for length in range(length_gap):
            value_set2.append('')
        value_set2.append('({})'.format(total_expenses))
        profit_for_the_year = int(gross_profit) - total_expenses
        if profit_for_the_year > 0:
            details.append('PROFIT FOR THE YEAR')
            value_set2.append(str(profit_for_the_year))
            value_set1.append('')
        else:
            details.append('LOSS FOR THE YEAR')
            value_set2.append('({})'.format(str(profit_for_the_year)))
            value_set1.append('')
        return [details, value_set1, value_set2]
    except ValueError:
        return 'Value Error'
