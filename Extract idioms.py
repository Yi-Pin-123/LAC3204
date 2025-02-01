import fitz  # PyMuPDF
import re

# Specify the path to your PDF file
file_path = '第2课 - 成语1 -复习资料.pdf'

def extract_text_from_pdf(file_path):
    # Open the PDF file
    document = fitz.open(file_path)
    text = ""

    # Extract text from all pages
    for page in document:
        text += page.get_text()

    # Close the document
    document.close()

        # Locate the second number in the text and drop everything before it
    def drop_text_before_second_number(text):
        # Find all occurrences of numbers (e.g., '18', '19', etc.)
        matches = list(re.finditer(r"\b\d+\b", text))
        
        if len(matches) >= 2:  # Ensure there are at least two numbers
            second_number_pos = matches[1].start()  # Get the start position of the second number
            text = text[second_number_pos:]  # Slice the text from the second number onwards
        return text
    
    # Drop text before the second number
    text = drop_text_before_second_number(text)
    return text


# Extract idioms and definitions from the PDF
text = extract_text_from_pdf(file_path)

def extract_idioms_and_definitions(text):
    idioms_and_definitions = []
    pattern = r"(\d+)\s(.+?。)\s(.+?)(?=\d+\s|$)"  # Regex to match idiom number, sentence, and definition

    # Find all matches based on the pattern
    matches = re.findall(pattern, text, re.DOTALL)

    for match in matches:
        _, sentence, definition = match
        # Remove any newlines in the sentence and definition
        clean_sentence = sentence.replace("\n", "").strip()
        clean_definition = definition.replace("\n", "").strip()
        idioms_and_definitions.append((clean_sentence, clean_definition))
    
    return idioms_and_definitions

# Extract idioms and definitions
idioms_and_definitions = extract_idioms_and_definitions(text)

len(idioms_and_definitions) 
#use this to check the number of idioms and definitions extracted is correct

def save_idioms_to_txt(idioms_and_definitions, output_file):
    # Clear the file contents before writing
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("")  # Clear the file by writing an empty string

    # Write the idioms and definitions
    with open(output_file, "a", encoding="utf-8") as file:  # Open in append mode to write content
        for idiom, definition in idioms_and_definitions:
            file.write(f"{idiom}\n")
            file.write(f"{definition}\n")
            file.write("\n")  # Add a blank line between entries

# Specify the output file name
output_file = "idioms_and_definitions.txt"

# Save the results to the text file
save_idioms_to_txt(idioms_and_definitions, output_file)

print(f"Idioms and definitions have been saved to {output_file}.")
