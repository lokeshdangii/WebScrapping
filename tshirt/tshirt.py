import subprocess

# # path for the bash file
bash_script_path = '/home/lokesh/Desktop/Decode/WebScrapping/tshirt.sh'  
# running the bash file
subprocess.run(['bash', bash_script_path])

# retving the  name and price form the file 
with open('curl.txt', 'r') as file:

    price_data = []
    name_data = []

    for line in file:

        if "name" in line:
            name_data.append(line.strip())
        if "priceINR" in line:
            price_data.append(line.strip())
             

# writting the name and price to the file
with open('data.txt', 'w') as data_file:
    for name, price in zip(name_data, price_data):
        data_file.write(name  +'\n' + price )



# 
    # MRP_price = []
    # discount_percent = []
    # brand_data = []


# if "brandName" in line:
        #     brand_data.append(line.strip())
        # if "mrpINR" in line:
        #     MRP_price.append(line.strip())
        # if "discountPercent" in line:
        #     discount_percent.append(line.strip())