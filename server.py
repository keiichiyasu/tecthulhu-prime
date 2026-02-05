#!/usr/bin/env python3
from flask import Flask, render_template_string, request, redirect, url_for
from ws2801 import ws2801
import time
import threading

app = Flask(__name__)

# Initialize LEDs
# Note: RPi.GPIO needs root privileges usually.
try:
    LEDs = ws2801()
    NUMBER_OF_PIXELS = 16
    ledpixels = [0] * NUMBER_OF_PIXELS
    LEDs.cls(ledpixels)
except Exception as e:
    print(f"Error initializing LEDs (Simulating mode): {e}")
    LEDs = None
    ledpixels = [0] * 16

# Ingress Prime Colors
COLORS = {
    'Neutral': [100, 100, 100],
    'Enlightened': [2, 191, 2],
    'Resistance': [4, 146, 208]
}

RESONATOR_COLORS = [
    [0, 0, 0],       # L0
    [254, 206, 90],  # L1
    [255, 166, 48],  # L2
    [255, 115, 21],  # L3
    [228, 0, 0],     # L4
    [253, 41, 146],  # L5
    [235, 38, 205],  # L6
    [193, 36, 224],  # L7
    [150, 39, 244]   # L8
]

current_state = {
    'faction': 'Neutral',
    'level': 1
}

def update_leds():
    if LEDs is None:
        return

    # Set Faction LEDs (Assuming pixels 8-15 based on prototype.py)
    faction_color = COLORS.get(current_state['faction'], [0,0,0])
    c = LEDs.Color(faction_color[0], faction_color[1], faction_color[2])
    
    for i in range(8, 16):
        LEDs.setpixelcolor_int(ledpixels, i, c)

    # Set Resonator LEDs (Assuming pixels 0-7)
    # For simplicity, setting all resonators to the current portal level color
    res_level = current_state['level']
    if 0 <= res_level < len(RESONATOR_COLORS):
        rc = RESONATOR_COLORS[res_level]
        res_c = LEDs.Color(rc[0], rc[1], rc[2])
        for i in range(0, 8):
            LEDs.setpixelcolor_int(ledpixels, i, res_c)

    LEDs.writestrip(ledpixels)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Tecthulhu Controller</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; background-color: #121212; color: #e0e0e0; text-align: center; padding: 20px; }
        h1 { color: #00d4ff; }
        .btn { display: inline-block; padding: 15px 25px; margin: 5px; font-size: 16px; border: none; border-radius: 5px; cursor: pointer; color: white; text-decoration: none; }
        .enl { background-color: #02BF02; }
        .res { background-color: #0492D0; }
        .neu { background-color: #666; }
        .level-btn { background-color: #333; width: 50px; }
        .status { margin: 20px; padding: 10px; border: 1px solid #444; }
    </style>
</head>
<body>
    <h1>Tecthulhu Prime</h1>
    
    <div class="status">
        Current: <span style="color: {{ faction_color }}">{{ state.faction }}</span> | L{{ state.level }}
    </div>

    <h3>Faction</h3>
    <a href="/set_faction/Enlightened" class="btn enl">Enlightened</a>
    <a href="/set_faction/Resistance" class="btn res">Resistance</a>
    <a href="/set_faction/Neutral" class="btn neu">Neutral</a>

    <h3>Portal Level</h3>
    {% for i in range(1, 9) %}
        <a href="/set_level/{{ i }}" class="btn level-btn" style="border: 2px solid rgb({{ res_colors[i][0] }},{{ res_colors[i][1] }},{{ res_colors[i][2] }})">L{{ i }}</a>
    {% endfor %}

    <br><br>
    <a href="/off" class="btn" style="background-color: #000; border: 1px solid #555;">Turn Off</a>
</body>
</html>
"""

@app.route('/')
def index():
    f_color = "#666"
    if current_state['faction'] == 'Enlightened': f_color = "#02BF02"
    elif current_state['faction'] == 'Resistance': f_color = "#0492D0"
    
    return render_template_string(HTML_TEMPLATE, state=current_state, faction_color=f_color, res_colors=RESONATOR_COLORS)

@app.route('/set_faction/<faction>')
def set_faction(faction):
    if faction in COLORS:
        current_state['faction'] = faction
        update_leds()
    return redirect(url_for('index'))

@app.route('/set_level/<int:level>')
def set_level(level):
    if 1 <= level <= 8:
        current_state['level'] = level
        update_leds()
    return redirect(url_for('index'))

@app.route('/off')
def turn_off():
    if LEDs:
        LEDs.cls(ledpixels)
    return redirect(url_for('index'))

if __name__ == '__main__':
    update_leds() # Set initial state
    app.run(host='0.0.0.0', port=5000)
