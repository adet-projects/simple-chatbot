# simple-chatbot

1. Open your cmd
2. Create and new folder named "chatbot" using this command: "mkdir chatbot" and then use "cd chatbot"
3. Make a new virtual environment with this code: "python -m venv venv"
4. Type this code: "venv\Scripts\activate"
5. Install these following libraries:
   - pip install ChatterBot==1.0.4
   - pip install tensorflow==2.16.1
   - pip install keras==3.3.3
   - pip install nltk==3.8.1
   - pip install numpy==1.26.4
6. Type this codeL :"code ." to proceed vscode
7. Clone the repository for references using GitBash: "git clone -b initial-release https://github.com/adet-projects/simple-chatbot.git" 
8. Make new following folders and files in chatbot folder:
   - For folders:
     - pickle 
       - words.pkl
       - classes.pkl
   - For files:
     - chat_model.py
     - chatapp.py
     - chatbot_gui.py
     - utils.py
     - intents.json
     - chatbot_model.h5
9. Copy the codes in all old files to new created files (except the words.pkl, classes.pkl, and chatbot_model.h5)
10. Remove your old projects 
11. Open a terminal and use cmd.
12. Run this file first: "python chatapp.py"
13. If there are no errors, use this command to run: "python chatbot_gui.py"
14. Just type the following queries based on intent.
  
