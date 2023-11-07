import subprocess

# path for the bash file
# bash_script_path = '/home/lokesh/Desktop/Decode/WebScrapping/jackets/jackets.sh'  
# # running the bash file
# subprocess.run(['bash', bash_script_path])

# retving the  name and price form the file 
with open('jackets_curl.txt', 'r') as file:

    price_data = []
    name_data = []

    for line in file:

        if "name" in line:
            name_data.append(line.strip())
        if "priceINR" in line:
            price_data.append(line.strip())        

# length
print(len(price_data))
print(len(name_data))

# writting the name and price to the file
with open('jackets_data.txt', 'w') as data_file:
    for name, price in zip(name_data, price_data):
        data_file.write(name  +'\n' + price  + '\n\n')
