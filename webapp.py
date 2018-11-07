from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(_name_)

{{my_variable}}
#render_template('index.html', my_variable="state")

@app.route("/")
def render_main():
    render_template('index.html', my_variable = get_state_options())

def get_state_options():
        listOfStates = []
        #First step is to create a list of all states
        for county in counties:
            if county["State"] in listOfStates:

                add the county's state to listOfStates
        #Second step is to create a string containing html
        #code for the options in the select element
        String options is initialized to the empty String
        for each state in listOfStates
            options = options + Markup("<option value=\""+s+"\">"+s+"</option>")
        return options
