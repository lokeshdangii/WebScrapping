import subprocess

# # path for the bash file
# bash_script_path = '/home/lokesh/Desktop/web/jeans.sh'
# # running the bash file
# subprocess.run(['bash', bash_script_path])

# Initialize variables to store data
brand_name = ""
name = ""
mrp_inr = ""
price_inr = ""
discount_percent = ""
url = ""
image_url = ""

# Open the file and retrieve data
with open('jeans_curl.txt', 'r') as file:
    product_data = []

    for line in file:
        if "brandName" in line:
            brand_name = line.strip()[14:-2]
        if "name" in line:
            name = line.strip()[9:-2]
        if "mrpINR" in line:
            mrp_inr = line.strip()[10:-1]
        if "priceINR" in line:
            price_inr = line.strip()[12:-1]
        if "discountPercent" in line:
            discount_percent = line.strip()[19:-1]
        if "url" in line:
            # Extract the URL correctly
            url = line.strip()[8:-2]
        if "image" in line:
            # Extract the image URL correctly 
            image_url = line.strip()[10:-2]

            

        if brand_name and name and mrp_inr and price_inr and discount_percent and url and image_url:
            product_info = f"{brand_name},{name},{mrp_inr},{price_inr},{discount_percent},{url},{image_url}"
            product_data.append(product_info)
            brand_name = ""
            name = ""
            mrp_inr = ""
            price_inr = ""
            discount_percent = ""
            url = ""
            image_url = ""

# Writing the product data to the file
with open('jeans_data.csv', 'w') as data_file:
    for product_info in product_data:
        data_file.write(product_info + '\n')