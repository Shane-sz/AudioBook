import PyPDF3
import pyttsx3
import pdfplumber
import time
import multiprocessing as mp    # importing necessary libraries
def parallel(file,output):
    book = open(file, 'rb')
    pdfReader = PyPDF3.PdfFileReader(book)  # opens the PDF File in binary mode
    pages = pdfReader.numPages  # checks the total number of pages in pdf
    finalText = ""
    print(f'{file} is processed by Process {mp.current_process().pid}.')  # Display the current process ID
    with pdfplumber.open(file) as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            finalText += text
    engine = pyttsx3.init()
    engine.save_to_file(finalText, f'{file[0:(len(file))-4]}_parallel_{output}.mp3')
    engine.runAndWait()
    print(f"{file} is done processing.")  # saving as mp3
if __name__ == '__main__':
    start = time.time()  # to measure the time taken
    processes = []
    files = ['25 pages.pdf', '25 pages.pdf','25 pages.pdf','25 pages.pdf']
    count = 1
    for file in files:
        process = mp.Process(target=parallel, args=(file,count))
        processes.append(process)
        print(process,file)
        count += 1
        process.start()
    for process in processes:  # Shows the process code number
        process.join()
    print("PDF is successfully converted.")
    print("Time taken by parallel processing:", time.time() - start)
