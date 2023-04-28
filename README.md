# TourBot
This is an virtual assistant chatbot that can help the tourists tell the weather for any city etc. 

We have used RASA framework to build the chatbot using NLP.

To start with, create a project folder named 'tour-guide-bot' as an example. 

Go to the command prompt and then change it to project path. 

Run git clone command to clone the repo from GitHub. Check the project structure.

## Environment setup:

1. First create a virtual environment using command prompt. To do that, run below command in command line.

> conda create --name tour-bot python==3.8

2. Acivate the virtual environment. To do this, run the command

> conda activate tour-bot

3. Install rasa 2.8 along with other python packages using requirements.txt. To do this, Run the command

> pip install -r requirements.txt

We are now ready to run the bot.
This chatbot makes use of weather API obtained from https://openweathermap.org/api which is free and 
easy to use.


## Running the chatbot:

1) To train the chatbot with the stories, run the command.

> rasa train

Now open 2 more terminals using start command and execute steps 2, 3 & 4 in 3 different terminals separately.

2) Run the Action server in debug mode.

> rasa run actions --debug

3) To initiate the converasation with the bot, run Rasa server (which internally calls Action server). 

> rasa run -m models --enable-api --cors "*" --debug

You can omit "-m models".

4) To open the conversation over App, go to the root path of the project and run app.py as below.

> python app.py

Note the localhost port. 

Copy and paste the local server url in your local browser. Once you run the url,
you will be able to see the chatbot icon visible on right bottom corner of the web page.

Click to open and you are ready to start conversing with your TourBot.

Further development is in progress and GitHub will be updated accordingly. 

### References:
1. https://rasa.com/docs/rasa/user-guide/installation/ 
2. https://rasa.com/docs/rasa/2.x/stories/
3. https://rasa.com/docs/rasa/command-line-interface/
3. https://medium.com/featurepreneur/integrating-chatbot-with-website-rasa-flask-4569f18d31be
4. https://openweathermap.org/