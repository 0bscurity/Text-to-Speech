from gtts import gTTS

menu = int(input('Choose menu option\n1. text input\n2. .txt import\n3. Quit\n~ '))

while menu != 3:
    if menu == 1:
        usrtxt = str(input('Enter the text you would like to convert to speech: \n'))
        tts = gTTS(text = usrtxt, lang = 'en')
        tts.save("speech_file.mp3")
        print("****************************************************\n" + usrtxt + "\
     was exported to " + "speech_file.mp3\n*****************\
    ***********************************")
    elif menu == 2:
        f = open(input('Enter filename: '))
        usrtxt = f.read()
        tts = gTTS(text = usrtxt, lang = 'en')
        tts.save("speech_file_1.mp3")
        print("****************************************************\n" + f + "\
         was exported to " + "speech_file.mp3\n*****************\
        ***********************************")
        f.close()
    elif menu == 3:
        quit
    menu = int(input('Choose menu option\n1. text input\n2. .txt import\n3. Quit\n~ '))
