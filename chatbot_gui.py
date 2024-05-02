import tkinter
from tkinter import *
from chatapp import ChatApp as cA

def send(event=None):
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        
        # Configure tag for "You" text
        ChatLog.tag_config("you_tag", foreground="blue", font=("Verdana", 12, "bold"))
        
        # Configure tag for "ChatBot" text
        ChatLog.tag_config("chatbot_tag", foreground="green", font=("Verdana", 12, "bold"))
        
        # Insert "You" text with the configured tag
        ChatLog.insert(END, "You: ", "you_tag")
        ChatLog.insert(END, msg + '\n\n')
        
        # Get response from the chatbot
        res = cA().chatbot_response(msg)
        
        # Insert "ChatBot" text with the configured tag
        ChatLog.insert(END, "ChatBot: ", "chatbot_tag")
        ChatLog.insert(END, res + '\n\n')
        
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        
base = Tk()
base.title("Simple ChatBot")
base.geometry("1000x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#489556", activebackground="grey", fg='#ffffff',
                    command=send, anchor='center')

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")

#Bind Enter key to send message
EntryBox.bind("<Return>", send)

#Place all components on the screen
scrollbar.place(x=980, y=6, height=386)
ChatLog.place(x=6, y=6, height=386, width=1000)  
EntryBox.place(x=128, y=401, height=90, width=900) 
SendButton.place(x=6, y=401, height=90)

base.mainloop()
