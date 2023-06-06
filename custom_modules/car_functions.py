import requests
import pandas as pd

def import_car_brand(brand):
    print(f"Importing {brand}")


    # uppercase the brand
    brand_upper = brand.upper()

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()

    # return nothing if it is empty
    if len(data) == 0:
        print(f"No cars found for {brand}")
        return None

    # convert data to a data frame
    data_df = pd.DataFrame(data)

    # export the data to csv
    data_df.to_csv(f"{brand}_export.csv", sep=";", index=False)

    pass