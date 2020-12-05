# currency = input('Currency:')
# NAssets = input('Non-current Asset names:').split(', ')
# NValues = input('Values for Non-current assets:').split(', ')
# accumulated_depreciation  = input('Accumulated depreciation')
# closing_inventory = input('Closing Inventory:')
# trade_receivable = input('Trade Receivable:')
# cash_at_bank = input('Cash at Bank:')
# cash_in_hand = input('Cash in Hand:')
# current_assets = input('Other current assets:').split(', ')
# current_assets_values = input('Values:').split(', ')
# equity = input('Equity:')
# profit_for_the_year = input('Profit for the year:')
# drawings = input('Drawings:')
# trade_payable = input('Trade payable:')
# current_liabilities = input('Other current liabilities:').split(', ')
# current_liabilities_values = input('Values:').split(', ')
# loans = input('Non-current loan names:').split(', ')
# loan_values = input('Values:').split(', ')


def calculate_balance(NAssets, NValues, closing_inventory, accumulated_depreciation, trade_receivable,
                      cash_at_bank, cash_in_hand, current_assets, current_assets_values, equity,
                      profit_for_the_year, drawings, trade_payable, current_liabilities,
                      current_liabilities_values, loans, loan_values):
    try:
        details = []
        value_set1 = []
        value_set2 = []
        value_set3 = []
        details.append('ASSETS')
        value_set1.append('')
        value_set2.append('')
        value_set3.append('')
        total1 = 0
        length_gap = 0
        if NAssets[0].lower() != 'none':
            details.append('Non-current Assets')
            value_set1.append('')
            value_set2.append('')
            value_set3.append('')
            for asset, value in zip(NAssets, NValues):
                details.append(asset)
                value_set1.append(value)
                length_gap += 1
                total1 += int(value)
            if accumulated_depreciation.lower() != 'none':
                details.append('Accumulated depreciation')
                value_set1.append('({})'.format(accumulated_depreciation))
                length_gap += 1
                total1 -= int(accumulated_depreciation)
            for gap in range(length_gap):
                value_set2.append('')
                value_set3.append('')
            details.append('Total Non-current assets')
            value_set1.append('')
            value_set2.append(str(total1))
            value_set3.append('')
        length_gap = 0
        total2 = 0
        if (closing_inventory.lower() != 'none') or (trade_receivable.lower() != 'none') or \
                (cash_at_bank.lower() != 'none') or (cash_in_hand.lower() != 'none') or (current_assets[0] != 'none'):
            details.append('Current Assets')
            value_set2.append('')
            value_set3.append('')
            value_set1.append('')
            if closing_inventory.lower() != 'none':
                details.append('Closing inventory')
                value_set1.append(closing_inventory)
                length_gap += 1
                total2 += int(closing_inventory)
            if trade_receivable.lower() != 'none':
                details.append('Trade receivable')
                value_set1.append(trade_receivable)
                length_gap += 1
                total2 += int(trade_receivable)
            if cash_at_bank.lower() != 'none':
                details.append('Cash at bank')
                value_set1.append(cash_at_bank)
                length_gap += 1
                total2 += int(cash_at_bank)
            if cash_in_hand.lower() != 'none':
                details.append('Cash in hand')
                value_set1.append(cash_in_hand)
                length_gap += 1
                total2 += int(cash_in_hand)
            if current_assets[0].lower() != 'none':
                for current_asset, asset_value in zip(current_assets, current_assets_values):
                    details.append(current_asset)
                    value_set1.append(asset_value)
                    length_gap += 1
                    total2 += int(asset_value)
            for gap in range(length_gap):
                value_set2.append('')
                value_set3.append('')
            details.append('Total Current Assets')
            value_set1.append('')
            value_set2.append(str(total2))
            value_set3.append('')
            details.append('TOTAL ASSETS')
            value_set1.append('')
            value_set2.append('')
            value_set3.append(str(total1 + total2))
        total3 = 0
        length_gap = 0
        details.append('EQUITY AND LIABILITIES')
        value_set1.append('')
        value_set2.append('')
        value_set3.append('')
        details.append('Equity')
        value_set1.append(equity)
        length_gap += 1
        total3 += int(equity)
        if profit_for_the_year.lower() != 'none':
            details.append('Profit for the year')
            value_set1.append(profit_for_the_year)
            length_gap += 1
            total3 += int(profit_for_the_year)
        if drawings.lower() != 'none':
            details.append('Drawings')
            value_set1.append('({})'.format(drawings))
            length_gap += 1
            total3 -= int(drawings)
        for gap in range(length_gap):
            value_set2.append('')
            value_set3.append('')
        details.append('Closing equity')
        value_set1.append('')
        value_set2.append(total3)
        value_set3.append('')
        length_gap = 0
        total4 = 0
        if (trade_payable.lower() != 'none') or (current_liabilities[0].lower() != 'none'):
            if trade_payable.lower() != 'none':
                details.append('Trade payable')
                value_set1.append(trade_payable)
                length_gap += 1
                total4 += int(trade_payable)
            if current_liabilities[0].lower() != 'none':
                for liability, liability_value in zip(current_liabilities, current_liabilities_values):
                    details.append(liability)
                    value_set1.append(liability_value)
                    length_gap += 1
                    total4 += int(liability_value)
            for gap in range(length_gap):
                value_set2.append('')
                value_set3.append('')
            details.append('Total current liabilities')
            value_set1.append('')
            value_set2.append(str(total4))
            value_set3.append('')
        total5 = 0
        if loans[0].lower() != 'none':
            details.append('Non-current liabilities')
            value_set1.append('')
            value_set2.append('')
            value_set3.append('')
            for loan, loan_value in zip(loans, loan_values):
                details.append(loan)
                value_set1.append(loan_value)
                total5 += int(loan_value)
                value_set2.append('')
                value_set3.append('')
            details.append('Total Non-current liabilities')
            value_set1.append('')
            value_set2.append(total5)
            value_set3.append('')
        details.append('TOTAL EQUITY AND LIABILITIES')
        value_set1.append('')
        value_set2.append('')
        value_set3.append(str(total3 + total4 + total5))
        return [details, value_set1, value_set2, value_set3]
    except ValueError:
        return ['Invalid value']
