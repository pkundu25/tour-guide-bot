import sys


from flask import Flask, render_template, request
import numpy as np
import requests
from random import randint
import time
#from db.mongo import Person

sender = randint(1000, 10000)
app = Flask(__name__, template_folder='templates')
#app = Flask(__name__)

def restart_session():
    global sender
    sender = randint(10000, 100000)
    print("\n\n\n")
    print(f"Sender id reset to {sender}")
    print("\n\n\n")
    return "Success"

@app.route("/")
def home():
    return render_template("diginurse_index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    
    print(userText)
    #try:
    print("\n\n\n")
    print(f"Current sender id {sender}")
    print("\n\n\n")
    r = requests.post("http://localhost:5005/webhooks/rest/webhook",json={"message":userText,"sender":sender})
    text = r.json()
    print(f"\n\n\n *************** Response from RASA !!!! \n{text} \n")
    final_text = ""
    loc = None
    for t in  text:
        print(t)
        if 'custom' in t.keys():
            loc = t['custom']['blocks']   
        else:                         
            final_text += t['text'] + " "

    if loc is not None:
        print(loc)
        centers = loc['center']
        L = []
        for i in centers.keys():
            if centers[i] != "None" :
                f = float(centers[i])
                L.append(f)


        city = loc['city']

        return render_template("index1.html", latlong = L)

        '''
        centers = loc['center']
        if len(centers) < 5:
            lng0 = centers['lng0']
            lat0 = centers['lat0']
            lng1 = None
            lat1 = None
            lng2 = None
            lat2 = None
            lng3 = None
            lat3 = None
            lng4 = None
            lat4 = None




        else:  

            lng0 = centers['lng0']
            lat0 = centers['lat0']
            lng1 = centers['lng1']
            lat1 = centers['lat1']
            lng2 = centers['lng2']
            lat2 = centers['lat2']
            lng3 = centers['lng3']
            lat3 = centers['lat3']
            lng4 = centers['lng4']
            lat4 = centers['lat4']

            #print(lng1, lat1, lng2, lat2)

            # Forming a dict containing coordinate values thus extracted
        coord = {
        "lng0" : lng0, "lat0" : lat0, "lng1": lng1, "lat1": lat1, "lng2": lng2, "lat2": lat2, "lng3": lng3, "lat3": lat3,
        "lng4": lng4, "lat4": lat4
        }

        
        #return render_template("index1.html")
        return render_template('index1.html', lng0 = coord['lng0'], lat0 = coord['lat0'], lng1 = coord['lng1'], lat1 = coord['lat1'],
                            lng2 = coord['lng2'], lat2 = coord['lat2'], lng3 = coord['lng3'], lat3 = coord['lat3'], 
                            lng4 = coord['lng4'], lat4 = coord['lat4'])

        '''                            
    


    else:    
        if final_text == "":
            final_text = "Sorry, Seems like my connection lost!! Please come back later 🙏"
        return_this = '<p class="botText"><span>' + final_text + '</span></p>'

        return_this = return_this.replace("\n","<br>")
        print(return_this)

        return return_this
    

if __name__ == "__main__":
    app.run(debug=True, port = 8001)
