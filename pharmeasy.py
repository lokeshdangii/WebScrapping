# from web import extract_slug
import time
import requests
from bs4 import BeautifulSoup
import json

# --------------------------------------------- Slug Extract Function  -------------------------------------

def extract_slug():

    with open("output.txt", "r") as file:
        web_txt = file.read()

    # Split the file data by lines
    lines = web_txt.split("\n")
    # print(lines)

    # list to store the extracted slugs
    slugs = []

    # Iterate through the lines and extract slugs using conditional statements
    for line in lines:
        # Check if the line contains the "slug" field
        if '"slug":' in line:
            # Split the line by the first delimiter '"slug": "'
            parts = line.split('"slug": "')
            # print("parts of the slug : ", parts)

            # Get the second part (index 1) which contains the slug value
            slug_part = parts[1]
            # print("slug part : ", slug_part)

            # Split the slug_part by the double quote delimiter '"'
            slug_part2 = slug_part.split('"')
            # print("slug part2 : ", slug_part2)
            slug = slug_part2[0]
            # print("slug :", slug)
            slugs.append(slug)
    print(slugs)

    # Open a new file for writing and append slugs to it
    with open("slugs.txt", "a") as output_file:
        for slug in slugs:
            output_file.write(slug + "\n")

    return slugs

# loop for multiple pages
for i in range(2,50):
    # url = f"https://www.meesho.com/search?q=shirt&searchType=manual&searchIdentifier=text_search&page={i}"
    url = f'https://pharmeasy.in/api/search/search/?intent_id&page={i}&q=parac'
    response = requests.get(url).json()

    # Save the response as a formatted JSON string
    formatted_response = json.dumps(response, indent=4)

    with open("output.txt", "w") as json_file:
        json_file.write(formatted_response)



# -------------------------------------------- Beautiful Soup --> Name and Price  ------------------------------------------------

    slugs = extract_slug()
    print(slugs)

    name_and_price = {}

    for slug in slugs:

        if '-' in slug:
            url = "https://pharmeasy.in/online-medicine-order/" + slug 
            data = requests.get(str(url))
            # print(url)

            # # print(data.text)
        
            soup = BeautifulSoup(data.text, 'html.parser')

            # print()
            # print("-------------------Medicine Name and Price ----------------------------------")
            # print()

            # name
            name = soup.find_all("h1", {"class":"MedicineOverviewSection_medicineName__dHDQi" })
            # print("page : ", i)
            # check name is there or not
            if name:
                print("\n----------------------------------------------------------\n")
                str_name = str(name[0])
                start_idx = str_name.find('>')
                end_idx = str_name.rfind('<')
                str_name = str_name[start_idx+1:end_idx]
                print(str_name)
                #1. MedicineOverviewSection_medicineName__dHDQi  #OverviewSection_productNameOTC__HqnU_
            

            # price
            price = soup.find_all("span", {"class":"PriceInfo_striked__Hk2U_" })
            # check price is there or not
            if price:
                str_price = str(price[0])
                start_idx = str_price.find('->')
                end_idx = str_price.rfind('<')
                str_price = str_price[start_idx+2:end_idx]   #PriceInfo_striked__Hk2U_
                print(str_price)
            
            
            # name_and_price.update({str_name:str_price})

            # # print("\nnames and prices are :",name_and_price)

            # for x,y in name_and_price.items():
            #     print(x + ' : ' + y)



# slug = slug.strip()[9:-2]}\n