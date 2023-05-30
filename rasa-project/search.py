import requests
#from flask import Flask, render_template, request, jsonify

#app = Flask(__name__, template_folder='templates')


def LocalSearch(search, place_type):
      access_token = "pk.eyJ1IjoicGt1bmR1MjUiLCJhIjoiY2xoaWwwNDBrMDFyaDNrcGNvMmhrZXlsaCJ9.sOxWZOMT9vWN-YyhQm4cwg"
      # Search text could be "city" or "place" if place_type="place" or it could be "beach", "hotel", "hospital" etc. if place_type="poi" (point of interest)
      # `proximity` is set to the coordinates of the campus
      # `bbox` is set to encompass the place/city such as Berkeley CA
      #Final_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/place.json?proximity=-122.25948,37.87221&bbox=-122.30937,37.84214,-122.23715,37.89838&access_token=" + access_token
      #print(Final_url)
      #Final_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + city + ".json" + "?proximity=ip" + "&access_token=" + access_token
      url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + search + ".json?limit=10&proximity=ip&types="+ place_type + "&access_token=" + access_token      
          
      local_search_data = requests.get(url).json()

      # Defining a list of center coordinates
      center_list = []
      for i in local_search_data['features']:
        d = {}
        d['center'] = i['center']
        center_list.append(d['center'])
              
      return center_list[:5]
      
      #return local_search_data['features'][0]['center'], local_search_data['features'][0]['bbox']
      
'''
@app.route('/')
def child():
  #ls = localSearch()  #Instantiating an object of a class
  center, bbox = LocalSearch("Pune")

  lng = center[0]
  lat = center[1]
  lng1 = bbox[0]
  lat1 = bbox[1]
  lng2 = bbox[2]
  lat2 = bbox[3]
  
  locs = [lng, lat, lng1, lat1, lng2, lat2]
  #(lng1, lat1, lng2, lat2) = (163.675406, 115.40937, 164.282659, 115.80082)
  #(lng, lat) = (163.869768, 115.536246)
   
  #return render_template('mapview.html', lng = center[0], lat = center[1], lng1 = bbox[0], lat1 = bbox[1], lng2 = bbox[2], lat2 = bbox[3])
  #return render_template("mapview.html", lng = lng, lat = lat, lng1 = lng1, lat1 = lat1, lng2 = lng2, lat2 = lat2)
  return render_template("./mapview.html", loc = locs)


if __name__ == "__main__":
  #city = 'Berkeley CA'
  #temperature=Weather(city)['temp']
  #humidity = Weather(city)['humidity']
  #places = LocalSearch(city)
  #wind_mph = Weather(city)['wind_speed']
  #print(temperature)
  #LocalSearch('Pune')
  #child()
  #print(wind_mph)
  app.run(debug=True, port = 8001)
'''  
