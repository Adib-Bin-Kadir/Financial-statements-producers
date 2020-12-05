def add_row(total1, total2, acc_name, value, status):
    if status == 'debit':
        detail = acc_name
        debit = value
        credit = ''
        total1 += int(value)
    elif status == 'credit':
        detail = acc_name
        debit = ''
        credit = value
        total2 += int(value)
    return [total1, total2, detail, debit, credit]
