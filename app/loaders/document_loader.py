from pypdf import PdfReader
import os
from config import MAX_FILE_SIZE
#Loader for pdf
def loader_pdf(filepath):
    try:
        reader = PdfReader(filepath)

    except Exception as e:
        raise ValueError(f"Error reading {filepath}: {e}")

    text = ""
    for page in reader.pages:
        pagetext =page.extract_text()
        if pagetext:
            text += pagetext + " "

    return text

# Loader for txt
def loader_txt(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        raise ValueError(f"Error reading {filepath}: {e}")
    return text


#For lading files and returing the result with info (to append later)
def loader_document(filepath):
    if not os.path.exists(filepath):
        raise ValueError(f"{filepath} does not exist.")
    size = os.path.getsize(filepath)
    
    if size > MAX_FILE_SIZE:
        raise ValueError(f"{filepath} exceeds the maximum file size.")
 
    if filepath.endswith(".pdf"):
        text=loader_pdf(filepath)
    elif filepath.endswith(".txt"):
        text=loader_txt(filepath)
    else:
        raise ValueError(f"{filepath} is not a pdf or txt file.")

    if not text.strip():
        raise ValueError(f"{filepath} is empty.")

    
    result ={ "filepath": filepath, 
             "filename": os.path.basename(filepath),
             "filetype": os.path.splitext(filepath)[1],
             "text": text, 
             "length": len(text)}
    return result

#Function to main - to load all filkes and append the result (json format)
def ingest_folder(folder_path):
    res=[]
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            try:
                full_path = os.path.join(root, file)
                res.append(loader_document(full_path))
            except ValueError as e:
                print(f"Error processing {file}: {e}")
                continue
    return res
