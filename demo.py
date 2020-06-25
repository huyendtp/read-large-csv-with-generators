file_name = 'demo.csv'
# start by reading each line from the file with a generator expression
lines = (line for line in open(file_name))

# split each line into a list
list_line = (s.rstrip().split(',') for s in lines)

# pull the column names out of demo.csv
cols = next(list_line)

# creates dictionaries and unites them with a zip() call
company_dicts = (dict(zip(cols, data)) for data in list_line)
a = next(company_dicts)

# gets each company’s series A funding amounts
funding = (int(company_dict['raisedAmt']) for company_dict in company_dicts if company_dict['round'] == 'a')

# sum() to get the total amount of series A funding found in the CSV
total_series_a = sum(funding)
print(f'Total series A fundraising: ${total_series_a}')
