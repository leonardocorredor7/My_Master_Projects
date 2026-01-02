## Data Download Script (`data_download.py`)

#The datasets used in this project are **not stored in the GitHub repository**. Instead, they are downloaded locally using the script "data_download.py".

#This script downloads the monthly FuelWatch retail price data directly from the official website of the Western Australia Government. It automatically:

#- Creates a local `data/` folder if it does not exist
#- Builds the correct download links for each month
#- Downloads the available CSV files into the `data/` folder

#The CSV files are ignored by Git and are therefore not uploaded to GitHub. This keeps the repository clean and avoids storing large data files.

#To download the data, run the script from the project directory:

#bash
#python data_download.py



import requests  # to work with HTTP requests
from pathlib import Path  # handle file paths
import pandas as pd  
from datetime import date  # get the current date

base_url = "https://warsydprdstafuelwatch.blob.core.windows.net/historical-reports"  # URL base de los datos

current_year = date.today().year  

dates = pd.date_range(  
    start=f"{current_year - 1}-10-01",  # Octubre del año anterior
    periods=12,  # last 12 months
    freq="MS"  # begining each month
)

data_path = Path("data")  # destiny folder
data_path.mkdir(exist_ok=True)  # it creates the folder if it doesn't exist

for d in dates: 
    filename = f"FuelWatchRetail-{d:%m-%Y}.csv"  
    url = f"{base_url}/{filename}" 

    print(f"Downlading {filename}...")  

    try:
        response = requests.get(url, timeout=30)  # Download with a timeout of 30 seconds
        response.raise_for_status()  # is the server response OK?
        (data_path / filename).write_bytes(response.content)  # it saves the file
        print(f"✔ {filename} DONE")  # Confirmation

    except requests.exceptions.RequestException as e:  # in that case of error
        print(f"✘ Error: {filename}: {e}")  
