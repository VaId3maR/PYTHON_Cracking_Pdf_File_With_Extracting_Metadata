from pikepdf import Pdf, PasswordError
import os
import datetime

# Function to try manual password entry
def try_manual_password(file_path):
    while True:
        passwordPdf = input("Enter password for PDF file: ")
        try:
            pdf = Pdf.open(file_path, password=passwordPdf)
            name_exit = file_path.replace(".pdf", "_unlocked.pdf")
            pdf.save(name_exit)
            print(f"File was unlocked with password: '{passwordPdf}' and saved as: {name_exit}")
            return True
        except PasswordError:
            print(f"Incorrect password: '{passwordPdf}'.")
            if input("Do you want to try another password? (y/n): ").lower() != 'y':
                return False

# Function to try passwords from dictionary
def auto_scan_passwords(file_path, password_dictionary):
    # Load passwords from file
    passwords_from_file = []
    
    if os.path.exists(password_dictionary):
        try:
            with open(password_dictionary, 'r', encoding='utf-8') as f:
                passwords_from_file = [line.strip() for line in f if line.strip()]
            print(f"Loaded {len(passwords_from_file)} passwords from file {password_dictionary}")
        except Exception as e:
            print(f"Error while loading password dictionary file: {e}")
            return False
    else:
        print(f"Password dictionary file: '{password_dictionary}' does not exist")
        return False
        
    if not passwords_from_file:
        print("No passwords found in the dictionary file.")
        return False
        
    print("\nStarted trying passwords from file...")
    for i, passwordPdf in enumerate(passwords_from_file):
        print(f"Attempt {i+1}/{len(passwords_from_file)}: {passwordPdf}")
        try:
            pdf = Pdf.open(file_path, password=passwordPdf)
            name_exit = file_path.replace(".pdf", "_unlocked.pdf")
            pdf.save(name_exit)
            print(f"File was unlocked with password: '{passwordPdf}' and saved as: {name_exit}")
            return True
        except PasswordError:
            continue  # Continue with next password
    
    print("None of the passwords in the file worked.")
    return False

# Function to extract metadata from PDF
def extract_pdf_metadata(file_path):
    try:
        # Try to open without password first
        try:
            pdf = Pdf.open(file_path)
            password_required = False
        except PasswordError:
            print("PDF is password protected. Enter password to extract metadata:")
            password = input("Password (or press Enter to skip): ")
            if password.strip():
                try:
                    pdf = Pdf.open(file_path, password=password)
                    password_required = False
                except PasswordError:
                    print("Incorrect password. Will try to extract basic metadata only.")
                    password_required = True
            else:
                print("No password provided. Will try to extract basic metadata only.")
                password_required = True
        
        metadata = {}
        
        # Extract file info
        metadata["Filename"] = os.path.basename(file_path)
        metadata["File Size"] = f"{os.path.getsize(file_path) / 1024:.2f} KB"
        metadata["Last Modified"] = str(datetime.datetime.fromtimestamp(os.path.getmtime(file_path)))
        
        # Extract PDF metadata if accessible
        if not password_required:
            if pdf.docinfo:
                for key, value in pdf.docinfo.items():
                    metadata[str(key)] = str(value)
            
            # Get document structure info
            metadata["Page Count"] = len(pdf.pages)
            metadata["PDF Version"] = pdf.pdf_version
            
            # Check if PDF has forms
            metadata["Has Forms"] = "/AcroForm" in pdf.Root
            
            # Check for encryption info
            metadata["Is Encrypted"] = pdf.is_encrypted
        else:
            # Try to get some basic info even if encrypted
            try:
                with open(file_path, 'rb') as f:
                    # Read first few bytes to check PDF version
                    header = f.read(8).decode('utf-8', errors='ignore')
                    if header.startswith('%PDF-'):
                        metadata["PDF Version"] = header[5:].strip()
            except Exception as e:
                metadata["Error"] = f"Could not read file header: {e}"
        
        # Save metadata to file
        output_file = "metadata_pdf.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"PDF METADATA EXTRACTION REPORT\n")
            f.write(f"Generated on: {datetime.datetime.now()}\n")
            f.write(f"File: {file_path}\n")
            f.write("-" * 50 + "\n\n")
            
            for key, value in metadata.items():
                f.write(f"{key}: {value}\n")
        
        print(f"Metadata successfully extracted and saved to {output_file}")
        
        # Display some metadata on screen
        print("\nKey metadata:")
        for key in ["Filename", "File Size", "PDF Version", "Author", "Creator", "Producer", "CreationDate", "ModDate"]:
            if key in metadata:
                print(f"{key}: {metadata[key]}")
        
        return True
        
    except Exception as e:
        print(f"Error extracting metadata: {e}")
        return False

# Run the program
if __name__ == "__main__":
    print("=== PDF Password Cracker ===")
    
    # Ask user for path to PDF file
    pdf_path = input("Enter full path to the protected PDF file: ")
    
    # Check if PDF file exists
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist!")
        exit(1)
    
    # Present the options immediately
    print("\nChoose operation:")
    print("1. Enter password manually")
    print("2. AutoScan (use passwords from dictionary)")
    print("3. Extract PDF metadata")
    
    # Get user choice
    while True:
        user_choice = input("Your choice (1, 2 or 3): ")
        
        if user_choice == "1":
            try_manual_password(pdf_path)
            break
            
        elif user_choice == "2":
            dict_path = input("Enter path to password dictionary file (click 'ENTER' for scan with default dictionary: 100k_passwords.txt): ") or "100k_passwords.txt"
            auto_scan_passwords(pdf_path, dict_path)
            break
            
        elif user_choice == "3":
            extract_pdf_metadata(pdf_path)
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    print("Program finished.")