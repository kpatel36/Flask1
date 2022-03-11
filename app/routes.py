from app import app
from flask import render_template


@app.route('/')
def home():
    print('og route if this works')
    return render_template('index.html') 


@app.route('/carinventory')
def car_inventory():
    # defining a variable here and creating a print statement will print it in the terminal everytime that url endpoint is accessed
    small_car_inventory = ['Honda Accord', 'Honda Civic', 'Honda Insight', 'Honda Accord Hybrid']
    big_car_inventory = ['Honda Odessey', 'Honda CR-V', 'Honda HR-V', 'Honda Pilot', 'Honda Passport', 'Honda Ridgeline']
    print('carinventory is working')
    return render_template('carinventory.html', car_inventory=small_car_inventory, big_cars = big_car_inventory)


@app.route ('/traveldestinations')
def travel():
    a = "Welcome to Flightfinder. Where are you looking to fly today?"
    b = 'Here are the current trending travel locations'
    top_destinations = ['Galapagos Islands, Ecuador', 'The Maldives', 'Fiji', 'Tahiti', 'The Bahamas', 'Toronto, Canada', 'Chicago, USA', 'Nice, France', 'Seville, Spain', 'New York City, USA', 'Nambia', 'Napa Valley, USA', 'Colchagua Valley, Chile']
    tropicals = ['Galapagos Islands, Ecuador', 'The Maldives', 'Fiji', 'Tahiti', 'The Bahamas']
    return render_template('traveldestinations.html', text_a=a, text_b=b, top_dests=top_destinations, tropicals=tropicals)