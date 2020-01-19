from utils import root, filesdir, datadir
import openpyxl
import pandas as pd

headers = [
    'Zulassungsbezirk',
    'Benzin',
    'Diesel',
    'Gas',
    'Hybrid',
    'Elektro',
    'Sonstige'
 ]

args = {
    'sheet_name': 'Pkw',
    'header': None,
    'names': headers,
    'usecols': 'D,F:I,K:L',
    'engine': 'openpyxl',
    'skiprows': list(range(0, 9)),
    'skipfooter': 5,
    'thousands': '.',
    'na_values': '-'
}

infile = filesdir / 'fz1_2019_xlsx.xlsx'

df = pd.read_excel(infile, **args)

# remove subtotal rows
subtotals = pd.isna(df.Zulassungsbezirk)
df = df[~subtotals]

# split Zulassungsbezirksname & Kreisschlüssel into separate columns
zb = df.Zulassungsbezirk.str.strip().str.split('  ', expand=True)
df = df.assign(KS=zb[0], Zulassungsbezirk=zb[1])
df = df[['KS'] + headers]

# write result to csv
outfile = datadir / 'kfzbestand-nach-kraftstoffarten.csv'
df.to_csv(outfile, index=False)
