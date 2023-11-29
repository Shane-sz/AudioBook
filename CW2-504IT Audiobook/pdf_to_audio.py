import PyPDF3
import pyttsx3
import pdfplumber
import time
import multiprocessing as mp
# importing necessary libraries
def Sequential(file, output):  # creating the main function
    book = open(file, 'rb')
    pdfReader = PyPDF3.PdfFileReader(book)  # opens the PDF File in binary mode
    pages = pdfReader.numPages   # checks the total number of pages in pdf
    finalText = ""
    print(f'{file} is processed by Process {mp.current_process().pid}.')  # Display the current process ID
    with pdfplumber.open(file) as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            finalText += text     # Iterate through PDF pages, extract text, and append to finalText
    engine = pyttsx3.init()
    engine.save_to_file(finalText, f'{file[0:(len(file)-4)]}_serial_{output}.mp3')
    engine.runAndWait()
    print(f'{file} is done processing. ') # Saving as mp3 file
def Pdfloop():
    filelist = ['25 pages.pdf','25 pages.pdf','25 pages.pdf','25 pages.pdf']
    count = 1
    for file in filelist:
       Sequential(file,count)
       count += 1
# Creating a fuction to provide inputs to my pdf
if __name__ == '__main__':
    start = time.time()
    Pdfloop()
    print("PDF is successfully converted into audio.")
    print("Time taken by Sequential programming:", time.time() - start)

