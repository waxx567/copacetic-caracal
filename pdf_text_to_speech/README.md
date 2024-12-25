# PDF-to-Speech Reader

This Python program reads the text from a PDF file aloud using a text-to-speech engine (`pyttsx3`). It extracts the content of a PDF starting from a specified page and converts it to speech.

## Features

- Converts text from a PDF file to speech.
- Skips the first two pages by default (useful for PDFs with introductory content or table of contents).
- Supports any PDF with readable, extractable text.

---

## Prerequisites

### Required Libraries

Before running the program, ensure you have the following Python libraries installed:

1. **PyPDF2**: To extract text from PDF files.
2. **pyttsx3**: To perform text-to-speech.

### Installation

Install the required libraries using pip:
```bash
pip install pyttsx3 PyPDF2
```

---

## Usage Instructions

1. **Prepare Your PDF File**  
   - Place your desired PDF file in the same directory as this script.
   - Ensure the PDF is not password-protected and contains selectable text (scanned PDFs with images won't work).

2. **Edit the Script**  
   - Replace the file name `'On-the-Origin-of-Species.pdf'` in the `myFile` variable with the name of your PDF file.
   ```python
   myFile = open('Your-PDF-File.pdf', 'rb')
   ```

3. **Run the Script**  
   - Execute the script in your Python environment or terminal:
     ```bash
     python pdf_to_speech.py
     ```

4. **Output**  
   - The program will start reading the PDF aloud from the third page onward. Adjust the starting page by modifying the range in the `for` loop:
     ```python
     for i in range(2, numPages):
     ```

---

## Customization

1. **Change the Starting Page**
   - To start reading from a different page, change the starting index in the `range` function. For example:
     ```python
     for i in range(0, numPages):  # Start from the first page
     ```

2. **Use a Different Voice**
   - Customize the voice or language settings of the text-to-speech engine:
     ```python
     speaker.setProperty('voice', 'voice_id')  # Replace 'voice_id' with a valid ID
     ```

3. **Adjust Speech Rate**
   - Modify the speech rate for faster or slower playback:
     ```python
     speaker.setProperty('rate', 150)  # Adjust the rate value
     ```

4. **Save Speech as Audio File**  
   - Save the spoken text as an audio file instead of playing it live:
     ```python
     speaker.save_to_file(text, 'output_audio.mp3')
     ```

---

## Limitations

- The program may not handle PDFs with complex layouts (e.g., multiple columns, tables) accurately.
- Extracted text might contain artifacts from the PDF formatting.

---

## Troubleshooting

1. **No Text Being Read**
   - Ensure your PDF contains extractable text. Test by manually copying text from the PDF.

2. **Error: File Not Found**
   - Verify the file name and ensure the PDF is in the same directory as the script.

3. **Error: Missing Library**
   - Make sure all required libraries are installed by running:
     ```bash
     pip install pyttsx3 PyPDF2
     ```

---

## Future Improvements

- Add GUI support for selecting PDFs.
- Allow the user to specify the start and end pages dynamically.
- Implement OCR capabilities to handle image-based PDFs.

---

Enjoy your PDF-to-Speech Reader! 🎧📖
