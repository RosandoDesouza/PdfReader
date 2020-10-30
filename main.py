import PyPDF2
import pyttsx3

print("Starting Text2Speech Script!!!")

book = open('progit.pdf', 'rb')
pdfFilReader = PyPDF2.PdfFileReader(book)

totalPages = pdfFilReader.numPages

print(f"Total Pages: {totalPages}")

speechEngine = pyttsx3.init()

voices = speechEngine.getProperty('voices')

# voiceCount = 0
# for voice in voices:
#      voiceCount = voiceCount + 1
#      print(f"{voiceCount} - {voice.id}")
#     speechEngine.setProperty('voice', voice.id)
#     speechEngine.say("Hello World!")
#     speechEngine.say('I am currently speaking in ' + voice.id)
#     speechEngine.runAndWait()

# rate set to 160
rate = speechEngine.getProperty('rate')
speechEngine.setProperty('rate', 150)

# Voice set to Linux-Mint
# speechEngine.setProperty('voice', 'english')

# Voice set to Windows 10
speechEngine.setProperty('voice', voices[1].id)

# progit start at 14
page = pdfFilReader.getPage(15)
text = page.extractText()

print(text)

speechEngine.say(text)
speechEngine.runAndWait()

print("Stopping Text2Speech Script!!!")