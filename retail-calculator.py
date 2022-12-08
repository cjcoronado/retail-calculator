number_of_tapes = int(input(f'Enter the number of cassette tapes being manufactured: '))
cost_of_tapes = float(input(f'Enter the manufacturing costs for the cassette tapes: '))
unit_cost = cost_of_tapes / number_of_tapes
print(f'Unit cost of tapes is ${unit_cost}.')
print()

profit_margin = float(input(f'How much of a profit margin do you want per item? Enter as a decimal (ex: .5 for 50%, 1.0 for 100%): '))
tape_retail = unit_cost * (1 + profit_margin)
print(f'The retail price for the tapes are ${tape_retail}')
