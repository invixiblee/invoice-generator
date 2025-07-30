
import pandas as pd
import glob

filepaths = glob.glob('invoices/*.xlsx')

for fpath in filepaths:
    df = pd.read_excel(fpath, sheet_name='Sheet 1')
    print(df)
