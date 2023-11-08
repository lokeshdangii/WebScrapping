import csv
import mysql.connector

# Database connection information
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'tata_neu'
}

# CSV file containing the data
csv_file = 'jacket_data.csv'

try:
    # Connect to the MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Open the CSV file and read the data
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)  # Skip the header row if it exists

        for row in csv_reader:
            if len(row) == 7:  # Ensure the row has the expected number of values
                brand_name, product_name, mrp_price, inr_price, discount_percent, url, image_url = row
                # Insert the data into the database
                query = "INSERT INTO jackets (brand_name, product_name, MRP_Price, INR_Price, discount_percent, url, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (brand_name, product_name, mrp_price, inr_price, discount_percent, url, image_url)
                cursor.execute(query, values)
            else:
                # print(f"Skipped a row : {row}")
                print(f"------------------------ Skipped a row ------------------------- ")

    # Commit the changes to the database
    conn.commit()

    print("Data added to the database successfully.")

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    cursor.close()
    conn.close()
