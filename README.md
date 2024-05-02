# simple-chatbot

1. Open your cmd
2. Create a new folder named "chatbot" using this command: "mkdir chatbot" and then use "cd chatbot"
3. Make a new virtual environment with this code: "python -m venv venv" in chatbot folder
4. Type this code: "venv\Scripts\activate"
5. Install these following libraries while you in (venv):
   - pip install ChatterBot==1.0.4
   - pip install tensorflow==2.16.1
   - pip install keras==3.3.3
   - pip install nltk==3.8.1
   - pip install numpy==1.26.4
6. Type this code:"code ." to proceed vscode
7. Get the chatbot in GitHub or Google Drive for references
   - In GitHub, clone the repository using this command: "git clone -b initial-release https://github.com/adet-projects/simple-chatbot.git" in GitBash
   - In Google Drive, download this file: https://drive.google.com/file/d/1wTUzxHog_bVgwx3ZqAxuuN6sNxNQfkIm/view?usp=sharing
10. Make new following folders and files in chatbot folder:
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
11. Copy the codes in all old files to new created files (except the words.pkl, classes.pkl, and chatbot_model.h5)
12. Remove your old projects 
13. Open a terminal and use cmd.
14. Make sure your cmd terminal is in virtual environment(venv), if not, type this code again: "venv\Scripts\activate" in the vscode's cmd terminal
15. Run this file first: "python chatapp.py"
16. If there are no errors, use this command to run: "python chatbot_gui.py"
17. Just type the following queries based on intents.json.
  
