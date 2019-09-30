#------------------------------------------
# Import Stuff here
#------------------------------------------

import tkinter as tk
import gtts as gTTS

#------------------------------------------
# Define events
#------------------------------------------

# Called by convert button to get text from tk entry and convert it to an mp3 file
def event_convert(event):
    # Visual configurations
    processing_label = tk.Label(win, text = "Converting...")
    processing_label.place(x = 370, y = 130)
    processing_label.configure(background = 'light blue') 
    # Processes
    #print("%s" % (entry1.get()))
    textInput = input('%s' % (entry1.get()))
    textconv = gTTS(text = textInput, lang = 'en')
    textconv.save("text.mp3")

#------------------------------------------
# GUI Configuration
#------------------------------------------

# Create instance of GUI
win = tk.Tk()

# Add title to GUI
win.title("Text to Speech")

#Set size and color of the GUI
win.geometry('600x400')
win.configure(background = 'light gray')

# Create GUI frame
cFrame = tk.Frame(win)
cFrame.pack()

# Create textbox
entry1 = tk.Entry(win)
entry1.place(x = 240, y = 130)

# Create label
label2 = tk.Label(win, text = "Type text to be converted\nto speech below:")
label2.place(x = 233.5, y = 93)

# Create button to convert text to speech
buttonconvert = tk.Button(win, text = "Convert")
buttonconvert.place(x = 240, y = 151)
buttonconvert.bind("<Button-1>", event_convert)

# Create button to quit program
buttonquit = tk.Button(win, text = ' Quit  ', command = win.quit)
buttonquit.place(x = 321, y = 151)

#Start the GUI/Create the main loop
win.mainloop()

#------------------------------------------






