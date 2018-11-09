from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('index.html', my_variable = get_state_options())

def get_state_options():
    listOfStates = []
    with open('countydemographics.JSON') as demographics_data:
        counties = json.load(demographics_data)
    #state  = county["State"]
    #First step is to create a list of all states
    for county in counties:
        state = county["State"]
        if not state in listOfStates :
            listOfStates.append(state)
    print(listOfStates)
    return listOfStates
    
    for state in listOfStates:
        options += Markup("<option value=\"" +state+ "\">" +state+ "</option>")
        
    return options

if __name__ == "__main__":
    app.run(debug=True)
