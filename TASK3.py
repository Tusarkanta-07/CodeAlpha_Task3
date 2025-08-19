import re
import os

input_file = 'input.txt'
output_file = 'extracted_emails.txt'

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
else:
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, content)

    with open(output_file, 'w', encoding='utf-8') as file:
        for email in emails:
            file.write(email + '\n')

    print(f"Extracted {len(emails)} email(s) and saved to {output_file}")