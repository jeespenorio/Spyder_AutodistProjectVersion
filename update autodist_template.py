#%%
''' 
Creator: JID Espenorio
Requestor: Data Analyst - Autodist
Created: July 9, 2024
Modified/Improved Date: September 2, 2024 '''
#####################################################################################################################
import pandas as pd 

# Define a class for the Autodistribution template
class AutodistTemp:
    def __init__(self, make, model, year, mpn, sku, position, pro_type, vendor, vendorcode, vendornotes):
        self.make = make
        self.model = model
        self.year = year
        self.mpn = mpn
        self.sku = sku
        self.position = position
        self.pro_type = pro_type
        self.vendor = vendor
        self.vendorcode = vendorcode
        self.vendornotes = vendornotes
        
    def to_dict(self):
        return {
            'Make': self.make,
            'Model': self.model,
            'Vendor': self.vendor,
            'Vendor Code': self.vendorcode,
            'Product Type': self.pro_type,
            'Position': self.position,
            'SKU': self.sku,
            'MPN': self.mpn,
            'Year': self.year,
            'Vendor Notes': self.vendornotes
        }
#%%
###################################################################################################################
#2nd Part
# Define a class for generating Autodistribution data
class AutodistGenerator:
    def __init__(self, autodist_template, list_models, years):
        self.autodist_template = autodist_template
        self.list_models = list_models
        self.years = years
    
    def generate_autodist(self):
        data = []
        for model in self.list_models:
            for year in self.years:
                autodist_data = {
                    'Make': self.autodist_template.make,
                    'Model': model,
                    'Year': year,
                    'Vendor': self.autodist_template.vendor,
                    'Vendor Code': self.autodist_template.vendorcode,
                    'Position': self.autodist_template.position,
                    'MPN': self.autodist_template.mpn,
                    'SKU': self.autodist_template.sku,
                    'Product Type': self.autodist_template.pro_type,
                    'Vendor Notes': self.autodist_template.vendornotes,
                }
                data.append(autodist_data)
        return pd.DataFrame(data)
#%%    
#####################################################################################################################
# Initialize the Autodist template
autodist_template = AutodistTemp(
    make='KTM',
    model='All types of models',
    year=None,
    vendor='ANTIG',
    vendorcode='ANTIGRAVITY BATTERIES LLC',
    position='',
    mpn='AG-ATZ7-RS',
    sku='505039',
    pro_type='Antigravity Batteries Fitment',
    vendornotes='ENGINE/CC: All Engine Sizes'
)

# List of models
list_models = [
'450 SMR', 
'125 EXC', 
'200 EXC', 
'250 EXC', 
'250 EXC-F', 
'250 EXC 4-Stroke', 
'300 EXC', 
'350 EXC-F', 
'380 EXC', 
'400 EXC', 
'450 EXC', 
'450 EXC-F Six Days', 
'450 EXC-R', 
'500 EXC', 
'500 EXC-F', 
'500 EXC-F Six Days', 
'500 EXC Six Days', 
'520 EXC', 
'525 EXC', 
'525 EXC-G', 
'530 EXC-R', 
'150 XC-W', 
'150 XC-W TPI', 
'200 XC-W', 
'250 XC-W', 
'250 XC-W TPI', 
'300 XC-W', 
'300 XC-W Six Days', 
'300 XC-W TPI', 
'300 XC-W TPI ERZBERGRODEO', 
'300 XC-W TPI Six Days', 
'400 XC-W', 
'450 XC-W', 
'500 XC-W', 
'525 XC-W', 
'530 XC-W', 


]

# List of years
years = list(range(2000, 2023))

# Generate the autodistribution data
generator = AutodistGenerator(autodist_template, list_models, years)
final_df = generator.generate_autodist()

# Display the final DataFrame
#print(final_df) # or just use final_df to display in Notebook
final_df.head(5)
#%%
file_path =r"C:\Users\User\Desktop\nachmann\TODAY -TASK\Antigravity Batteries Fitment 2024\MERGE\AG-ATZ10-RSv66 - 750.csv"
final_df.to_csv(file_path, index = False)

#%%
## Connecting to Postgresql
#%%
file_path =r"C:\Users\User\Desktop\nachmann\TODAY -TASK\Antigravity Batteries Fitment 2024\MERGE\AG-ATZ7-RSv88- Husaberg Beta All Engine Sizes.csv"
final_df.to_csv(file_path, index = False)
#%%
#activating the environment
%load_ext sql
#%%
''#Reloading the environment if possible''
%reload_ext sql
#%%
#Credentials in mylocal database

%sql postgresql://postgres:Password01@localhost:5432/Autodist_Project
#%%
'''Testing the waters'''
# Establish the connection to PostgreSQL
%sql postgresql://postgres:Password01@localhost:5432/Autodist_Project

# Run the query
%sql SELECT * FROM public."new_table9_19" LIMIT 10;
#%%
#import necessary library
import pandas as pd

# Establish the connection to PostgreSQL
%sql postgresql://postgres:Password01@localhost:5432/Autodist_Project

# Run the query and fetch the result into a DataFrame
result = %sql SELECT * FROM public."new_table9_19" LIMIT 10;

# Convert the result to a pandas DataFrame
df = pd.DataFrame(result, columns=['Make', 'Model', 'Year', 'Vendor', 'Vendor Code', 'Position', 'MPN', 'SKU', 'Product Type', 'Vendor Notes'])

# Set pandas to display all columns
pd.set_option('display.max_columns', None)

df
