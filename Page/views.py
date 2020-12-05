from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .income_statement import calculation_and_output
from .balance_sheet import calculate_balance
from .trial_balance import add_row
from .models import Account


def index(request):
    return HttpResponseRedirect('/income_statement/first/')


def income_statement(request, id):
    details_list = ['Currency', 'Revenue', 'Returns inwards', 'Opening inventory', 'Purchases',
                    'Returns outwards', 'Closing inventory', 'Carriage inwards', 'Carriage outwards']
    return render(request, 'income_statement.html', {
        'id': id,
        'details_list': details_list
    })


def balance_sheet(request, id):
    balance_list = ['Currency', 'Non-current Asset names', 'Values for Non-current assets',
                    'Accumulated depreciation', 'Closing Inventory', 'Trade Receivable', 'Cash at Bank',
                    'Cash in Hand', 'Other current assets', 'Values for assets', 'Equity',
                    'Profit for the year', 'Drawings', 'Trade payable', 'Other current liabilities',
                    'Values for liabilities', 'Non-current loan names', 'Values for loan names']
    return render(request, 'balance_sheet.html', {
        'id': id,
        'balance_list': balance_list
    })


def trial_balance(request, id):
    return render(request, 'trial_balance.html', {
        'id': id
    })


def income_statement_form(request, id):
    currency = request.POST['Currency']
    revenue = request.POST['Revenue']
    return_inwards = request.POST['Returns inwards']
    opening_inventory = request.POST['Opening inventory']
    purchases = request.POST['Purchases']
    return_outwards = request.POST['Returns outwards']
    closing_inventory = request.POST['Closing inventory']
    carriage_inwards = request.POST['Carriage inwards']
    carriage_outwards = request.POST['Carriage outwards']
    expenses = request.POST['expenses'].split(',')
    expense_values = request.POST['values'].split(',')
    final_list = calculation_and_output(
        revenue, return_inwards, opening_inventory, closing_inventory, purchases, carriage_inwards,
        carriage_outwards, expenses, expense_values, return_outwards
    )
    if final_list[0] != 'Value Error':
        details = final_list[0]
        value_set1 = final_list[1]
        value_set2 = final_list[2]
        zipped_list = zip(details, value_set1, value_set2)
        if len(expenses) == len(expense_values):
            return render(request, 'income_statement_result.html', {
                'zipped_list': zipped_list,
                'currency': currency,
                'id': id
            })
        else:
            return HttpResponse('The number of expenses and values did not match.')
    else:
        return HttpResponse('You entered an invalid value somewhere.')


def balance_sheet_form(request, id):
    currency = request.POST['Currency']
    NAssets = request.POST['Non-current Asset names'].split(', ')
    NValues = request.POST['Values for Non-current assets'].split(', ')
    accumulated_depreciation = request.POST['Accumulated depreciation']
    closing_inventory = request.POST['Closing Inventory']
    trade_receivable = request.POST['Trade Receivable']
    cash_at_bank = request.POST['Cash at Bank']
    cash_in_hand = request.POST['Cash in Hand']
    current_assets = request.POST['Other current assets'].split(', ')
    current_assets_values = request.POST['Values for assets'].split(', ')
    equity = request.POST['Equity']
    profit_for_the_year = request.POST['Profit for the year']
    drawings = request.POST['Drawings']
    trade_payable = request.POST['Trade payable']
    current_liabilities = request.POST['Other current liabilities'].split(', ')
    current_liabilities_values = request.POST['Values for liabilities'].split(', ')
    loans = request.POST['Non-current loan names'].split(', ')
    loan_values = request.POST['Values for loan names'].split(', ')
    string = 'The number of {} and values did not match.'
    if len(NAssets) != len(NValues):
        return HttpResponse(string.format('non-current assets'))
    elif len(current_assets) != len(current_assets_values):
        return HttpResponse(string.format('current assets'))
    elif len(current_liabilities) != len(current_liabilities_values):
        return HttpResponse(string.format('current liabilities'))
    elif len(loans) != len(loan_values):
        return HttpResponse(string.format('loans'))
    else:
        list_fin = calculate_balance(NAssets, NValues, closing_inventory, accumulated_depreciation,
                                     trade_receivable, cash_at_bank, cash_in_hand, current_assets,
                                     current_assets_values, equity, profit_for_the_year,
                                     drawings, trade_payable, current_liabilities,
                                     current_liabilities_values, loans, loan_values)
        if list_fin[0] != 'Invalid value':
            details = list_fin[0]
            value_set1 = list_fin[1]
            value_set2 = list_fin[2]
            value_set3 = list_fin[3]
            zipped_list = zip(details, value_set1, value_set2, value_set3)
            return render(request, 'balance_sheet_result.html', {
                'zipped_list': zipped_list,
                'currency': currency,
                'id': id
            })
        else:
            return HttpResponse('You entered an invalid value somewhere.')


total1 = 0
total2 = 0


def trial_balance_form(request, id):
    global total1
    global total2
    fin_list = add_row(total1, total2, request.POST['acc_name'], request.POST['value'],
                       request.POST['type_transaction'])
    total_debit = fin_list[0]
    total_credit = fin_list[1]
    total1 = total_debit
    total2 = total_credit
    Account.objects.create(detail=fin_list[2], debit=fin_list[3], credit=fin_list[4])
    list_output = Account.objects.all()
    return render(request, 'trial_balance.html', {
        'id': id,
        'list_output': list_output,
        'total_debit': total_debit,
        'total_credit': total_credit
    })


def clear_all(request):
    global total2
    global total1
    total1 = 0
    total2 = 0
    Account.objects.all().delete()
    return HttpResponseRedirect('/trial_balance/third/')
