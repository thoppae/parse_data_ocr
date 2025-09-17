from google.colab import auth
import gspread
from google.auth import default
from google.cloud import documentai_v1 as documentai
import os
from gspread.exceptions import WorksheetNotFound, APIError

def authenticate_google():
    """Authenticates Colab environment for Google Cloud and Google Sheets."""
    print("Authenticating with Google Cloud and Google Sheets...")
    auth.authenticate_user()
    creds, _ = default()
    gc = gspread.authorize(creds)
    print("Authentication successful.")
    return gc

def configure_documentai(project_id, location, processor_id):
    """Configures the Document AI client."""
    print("Configuring Document AI client...")
    client = documentai.DocumentProcessorServiceClient()
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"
    print(f"Document AI client configured for processor: {name}")
    return client, name

def process_pdf_with_documentai(client, processor_name, pdf_path):
    """Processes the input PDF file with Document AI."""
    print(f"Processing PDF file: {pdf_path}")
    with open(pdf_path, 'rb') as image:
        image_content = image.read()

    raw_document = documentai.RawDocument(content=image_content, mime_type='application/pdf')
    request = documentai.ProcessRequest(name=processor_name, raw_document=raw_document)

    response = client.process_document(request=request)
    document = documentai.Document.to_dict(response.document)
    print("PDF processed successfully!")
    return document

def extract_data_from_documentai_response(document):
    """Extracts the required data from the Document AI processing response."""
    print("Extracting data from Document AI response...")
    extracted_data = {}
    for entity in document.get('entities', []):
        if entity.get('type_'):
            key = entity['type_']
            value = entity.get('mention_text', '').strip()
            extracted_data[key] = value
    print("Data extraction complete.")
    return extracted_data

def prepare_data_for_google_sheets(data):
    """Formats the extracted data into a horizontal structure for Google Sheets."""
    print("Preparing data for Google Sheets...")
    headers = list(data.keys())
    values = list(data.values())
    sheet_data = [headers, values]
    print("Data prepared.")
    return sheet_data

def load_data_into_google_sheets(gc, spreadsheet_title, worksheet_title, data):
    """Loads the prepared data into the target Google Sheet."""
    print(f"Loading data into Google Sheet '{spreadsheet_title}'...")
    try:
        sh = gc.open(spreadsheet_title)
        print(f"Opened spreadsheet: {spreadsheet_title}")
    except gspread.SpreadsheetNotFound:
        print(f"Spreadsheet '{spreadsheet_title}' not found. Please create it.")
        return

    try:
        worksheet = sh.add_worksheet(title=worksheet_title, rows="100", cols="20")
        print(f"Created new worksheet: {worksheet_title}")
    except APIError as e:
        # Check if the error is due to the worksheet already existing
        if "A sheet with the name" in str(e) and "already exists" in str(e):
            print(f"Worksheet '{worksheet_title}' already exists. Accessing existing worksheet.")
            worksheet = sh.worksheet(worksheet_title)
        else:
            print(f"An API error occurred: {e}")
            return
    except WorksheetNotFound:
         # This might happen if trying to access a non-existent worksheet after a different API error
         print(f"Worksheet '{worksheet_title}' not found after an API error.")
         return


    # Update the sheet with the data using named arguments to avoid DeprecationWarning
    worksheet.update(range_name='A1', values=data)

    print(f"Data successfully loaded into '{spreadsheet_title}' in worksheet '{worksheet_title}'")

# Main execution flow
# Set your Google Cloud project ID, location, and processor ID
project_id = '#########' # Replace with your project ID
location = 'us' # Replace with your processor's location (e.g., 'us' or 'eu')
processor_id = '#########' # Replace with your processor ID
pdf_path = 'Receipt - invoice_name.pdf' # Replace with the actual path to your PDF
spreadsheet_title = 'title_1' # Replace with your spreadsheet title
worksheet_title = 'invoice_report' # Replace with the desired name for the new tab


gc = authenticate_google()
client, processor_name = configure_documentai(project_id, location, processor_id)
document = process_pdf_with_documentai(client, processor_name, pdf_path)
extracted_data = extract_data_from_documentai_response(document)
sheet_data = prepare_data_for_google_sheets(extracted_data)
load_data_into_google_sheets(gc, spreadsheet_title, worksheet_title, sheet_data)
