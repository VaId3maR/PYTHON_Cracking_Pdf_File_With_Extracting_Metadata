# Python - Cracking pdf file with extracting metadata

## Why these script is better than John The Ripper?

### Intuitive user interface
- Clear menu with numbered options
- Explicit messages guiding the user through the process
- No need to learn complicated command-line parameters

### PDF metadata extraction

- Unique feature not present in John the Ripper
- Automatic saving of metadata to a text file
- Display of key document information even without full access

### Specialization for PDF files

- Designed specifically for handling PDFs
- Directly saves unlocked PDF files
- Doesn't require additional tools to use the cracked password

### Accessibility for beginners

- No need for knowledge of advanced commands
- Clear error and progress messages
- Ability to work without knowing technical details of password formats

### Ease of modification

- Python code that is easy to understand and customize
- Clear structure with separate functions
- Ability to quickly add new features (as demonstrated by the metadata analysis implementation)

### Simplicity of installation

- Requires only Python and the pikepdf library
- No need for compilation or configuration
- Works the same on Windows, Linux, and macOS

### Educational value

- Clear code demonstrating the basics of password cracking
- Shows practical application of cryptographic libraries
- Allows understanding of PDF security mechanisms

### Immediate feedback

- Clear progress messages in real time
- Information about each password attempt
- Detailed metadata report

## How to run the script?
1. Install python - download Python installer from the official website.
2. Install pikepdf - Windows command: ``` pip install pikepdf ```
3. Files: cracking_pdf.py and 100k_passwords.txt should be the same folder.
4. Open cmd and go to where the script is located and use command ``` py cracking_pdf.py ```
<img width="1113" height="626" alt="cmd" src="https://github.com/user-attachments/assets/2aea9357-23e2-469a-ac4a-2685d4df53d4" />


5. Enter the full path to the password-protected PDF file
<img width="1113" height="626" alt="cmd2" src="https://github.com/user-attachments/assets/6c9429ad-6976-474e-9b0c-5be6a573666e" />


6. Then a menu with options to choose from was displayed
<img width="1113" height="626" alt="cmd3" src="https://github.com/user-attachments/assets/3d8a9fed-bfab-42fe-a3a0-1a8716e6016a" />


7. Option 1 - write password manually / Option 2 - AutoScan with your dictionary or default dictionary / Option 3 - Extract metadata from pdf locked (give little information about file) or unlocker (give more information about file)
<img width="1113" height="759" alt="cmd4" src="https://github.com/user-attachments/assets/6ebac975-5168-4ffe-9133-61f4ee37765e" />
<img width="1113" height="759" alt="cmd5" src="https://github.com/user-attachments/assets/3e330d6a-7524-41c6-b4ca-e8201d7551d4" />


> [!TIP]
> After cracking the PDF, a new PDF is created that no longer requires a password.
>
> After extracting the metadata, an file is created in which the metadata from the PDF is saved.

<img width="913" height="723" alt="2025-07-31_16h43_38" src="https://github.com/user-attachments/assets/035d79e5-9ff9-4fa4-b911-cb1cc172f74d" />
