# Dependecies:
from elevenlabs import generate, play, set_api_key
from tkinter import *
from tkinter.font import Font
import tkinter as tk
import threading
from tkinter.messagebox import showinfo
from tkinter import ttk

# Create the main application window
root = Tk()
# Setup the GUI
root.geometry("900x600")  # The width and height of the window
root.title("VoiceCom")  # The title of the GUI
root.resizable(False, False)  # The user cannot resize the window
root.configure(bg="#5596AE")  # ADD background color the the window

# Create a splash screen
# Create a Label widget for the splash screen image
splash_image = PhotoImage(file="bg.png")  # Replace with your splash screen image file
splash_label = Label(root, image=splash_image)
# Center the splash screen label within the window
splash_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Define the duration of the splash screen in milliseconds
splash_duration = 1000

# Function to transition from the splash screen to the main content
def transition_to_main():
    splash_label.destroy()  # Remove the splash screen label
    main()

def loder():
    # global speaker_btn
    # speaker_btn.destroy()

    def stop_loading():
        progress_bar.stop()
        progress_bar.destroy()
        frame.destroy()

    # Create a frame to hold the progress bar
    frame = tk.Frame(root, bg="#5596AE")
    frame.place(x=120, y=420, width=800, height=60)

    # Style of progress bar
    style = ttk.Style()
    style.theme_use('clam')  # Use a different theme ('clam', 'alt', 'default', etc.)
    style.configure("TProgressbar", foreground='#5596AE', background='#5596AE')

    # Create the progress bar
    progress_bar = ttk.Progressbar(frame, mode="determinate", maximum=70, value=10, style="TProgressbar")
    progress_bar.place(width=660)

    # Start the loader
    progress_bar.start()

    # Set the duration for the loader (in milliseconds)
    duration = 5000

    # Stop the loader after the specified duration
    root.after(duration, stop_loading)


def main():
    # The window that contains the operations
    # - list of names voices
    # - text box for writing text by users
    # - button for running the voice
    global name, speaker_btn
    font = Font(family="Arial", size=25)

    # Create a frame to hold the text box and scrollbar
    textbox_frame = Frame(root)
    textbox_frame.place(x=120, y=20)

    # Create the text box with y-scrollbar
    textbox = Text(textbox_frame, wrap="word", insertbackground="#5596AE", highlightcolor='#1A3E4B',
                   highlightbackground="#346070", highlightthickness=6, width=35, height=10)
    textbox.pack(side=LEFT, fill=BOTH)

    # Create the y-scrollbar
    ysbar = Scrollbar(textbox_frame, command=textbox.yview)
    ysbar.pack(side=RIGHT, fill=Y)

    # Configure the y-scrollbar
    textbox.config(font=font, yscrollcommand=ysbar.set)

    # A variable for storing the value selected by User
    value_selected = StringVar()
    value_selected.set("Antoni")  # The default value is "Antoni"

    # Selection list to allow to user select the name of the speaker
    # It will be in form of Menu in the above of the GUI
    def convert_text_to_speach(selected_option="Antoni"):
        try:
            set_api_key("Your API Key")
            audio = generate(
                text=textbox.get("0.0", "end-1c"),
                voice=selected_option,
                model="eleven_monolingual_v1"
            )
        except:
            set_api_key("Your API Key")
            audio = generate(
                text=textbox.get("0.0", "end-1c"),
                voice="Adam",
                model="eleven_monolingual_v1"
            )
        return audio

    def play_audio():
        # showinfo("Do Not Hurry", "Please the voice will take some time to run [رجاءا انتظر قليلا حتى يعمل الصوت] ")
        loder()
        threading.Thread(target=play(convert_text_to_speach(selected_voice.get()))).start()

    selected_voice = StringVar()
    menubar = tk.Menu(root)
    root.configure(menu=menubar)
    options_menu = tk.Menu(menubar)
    menubar.add_cascade(label="Voices", menu=options_menu)

    try:
        for i in ['Rachel', 'Domi', 'Bella', 'Antoni', 'Elli', 'Josh', 'Arnold', 'Adam', 'Sam']:
            options_menu.add_command(label=i, command=lambda v=i: selected_voice.set(v))

    except Exception as e:
        pass

    # Configure the button when clicked the audio will be run
    # speaker_btn.configure(command=play_audio(name))
    # Button when user press on it the text coverted to speech
    speaker_btn = Button(root, text="Speak", relief=SOLID, font=font, highlightcolor='#346070',
                         highlightbackground="#1A3E4B", highlightthickness=5, bd=0, default="active", bg='white',
                         command=lambda: threading.Thread(target=play_audio).start())
    speaker_btn.place(x=120, y=420, width=200, height=60)



# Schedule the function to be called after the specified duration
root.after(splash_duration, transition_to_main)
# Start the Tkinter event main loop
root.mainloop()
