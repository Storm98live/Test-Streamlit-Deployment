import pandas as pd
from cryptography.fernet import Fernet


# Function to encrypt data
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(data.encode())

# Function to encrypt Excel to CSV
def encrypt_excel_to_csv(input_excel_path, output_csv_path, key):
    # Load Excel file
    df = pd.read_excel(input_excel_path)

    # Convert DataFrame to CSV format
    csv_data = df.to_csv(index=False)

    # Encrypt CSV data
    encrypted_data = encrypt_data(csv_data, key)

    # Save encrypted data to CSV file
    with open(output_csv_path, 'wb') as csv_file:
        csv_file.write(encrypted_data)

if __name__ == "__main__":
    
    # Replace 'your_key_here' with your actual encryption key
    encryption_key = b'\xdbG\xcd$\xdcWq\xa9f\xa9\xae\x0e\xedI\xf4z)\x8e,s\xb5q\xc5\xab<k7\ty\xbe"\xd4'

    # Specify paths for the input Excel and output encrypted CSV files
    input_excel_path = r"C:\Users\SetupGame\Downloads\Santé Mentale.xlsx"
    output_csv_path = 'encrypted_output_example.csv'

    # Encrypt Excel to CSV
    encrypt_excel_to_csv(input_excel_path, output_csv_path, encryption_key)

    print(f"Excel file encrypted and saved as CSV: {output_csv_path}")
