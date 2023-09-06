import streamlit as st
# Create a function to display a traffic light


def display_traffic_light_people(red='off', yellow='off', green='off', category=""):
    colors = {'on': {'red': '#FF0000', 'yellow': '#FFFF00', 'green': '#00FF00'},
              'off': {'red': '#330000', 'yellow': '#333300', 'green': '#003300'}}

    traffic_light_html = f'''
    <h2>{category}</h2>
    <div style="background-color: black; width: 80px; height: 180px; padding: 10px; border-radius: 15%">
        <div style="background-color: {colors[red]['red']}; width: 50px; height: 50px; border-radius: 50%; margin: 5px auto;"></div>
        <div style="background-color: {colors[yellow]['yellow']}; width: 50px; height: 50px; border-radius: 50%; margin: 5px auto;"></div>
        <div style="background-color: {colors[green]['green']}; width: 50px; height: 50px; border-radius: 50%; margin: 5px auto;"></div>
    </div>
    '''
    return traffic_light_html


def display_traffic_light_vehicles(red='off', yellow='off', green='off', category=""):
    colors = {'on': {'red': '#FF0000', 'yellow': '#FFFF00', 'green': '#00FF00'},
              'off': {'red': '#330000', 'yellow': '#333300', 'green': '#003300'}}

    traffic_light_html = f'''
    <h2>{category}</h2>
    <div style="background-color: black; width: 80px; height: 180px; padding: 10px; border-radius: 15%">
        <div style="background-color: {colors[red]['red']}; width: 50px; height: 50px; border-radius: 50%; margin: 5px auto;"></div>
        <div style="background-color: {colors[yellow]['yellow']}; width: 50px; height: 50px; border-radius: 50%; margin: 5px auto;"></div>
        <div style="background-color: {colors[green]['green']}; width: 50px; height: 50px; border-radius: 50%; margin: 5px auto;"></div>
    </div>
    '''
    return traffic_light_html
