import pandas as pd

# Reads the data
sales_data = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']

# Concatenate all columns
df = pd.concat((pd.read_csv(filename) for filename in sales_data), ignore_index=True)
# Final length = 41160

# Create seperate df for Pink Morsels
pink_morsels = df[df['product']=='pink morsel']
# Final Length = 5880

# To remove the $ sign from Price column of Pink Morsels df
def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('$', ''))
    return(x)

pink_morsels['price'] = df['price'].apply(clean_currency).astype('float')


# Mutliplying Price & Quantity data to get Sales data
pink_morsels['Sales'] = pink_morsels['price'] * pink_morsels['quantity']

# Saving the cleaned df to final csv file!
pink_morsels.to_csv('Final_sales_output.csv', index=False)

# Further removed the product, price & quantity cols in EXCEL!