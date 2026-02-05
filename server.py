#!/usr/bin/env python3
from flask import Flask, render_template_string, request, redirect, url_for
try:
    from ws2801 import ws2801
except ImportError:
    ws2801 = None
import time
import threading
import math

app = Flask(__name__)

# Initialize LEDs
NUMBER_OF_PIXELS = 9
ledpixels = [0] * NUMBER_OF_PIXELS
LEDs = None

try:
    if ws2801:
        LEDs = ws2801()
        LEDs.cls(ledpixels)
except Exception as e:
    print(f"Error initializing LEDs (Simulating mode): {e}")

# Ingress Prime Colors
COLORS = {
    'Neutral': [100, 100, 100],
    'Enlightened': [2, 191, 2],
    'Resistance': [4, 146, 208]
}

RESONATOR_COLORS = [
    [0, 0, 0],       # L0 (OFF)
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
    'resonators': [1, 1, 1, 1, 1, 1, 1, 1]  # Levels for R1-R8
}

def led_animation_loop():
    global ledpixels
    while True:
        if LEDs is None:
            time.sleep(1)
            continue

        # Firefly / Breathing effect using Sine wave
        # Cycle every 4 seconds, brightness between 20% and 100%
        brightness = (math.sin(time.time() * (2 * math.pi / 4)) + 1) / 2 * 0.8 + 0.2

        # 1. Set Center (Index 0)
        f_color = COLORS.get(current_state['faction'], [0, 0, 0])
        c = LEDs.Color(
            int(f_color[0] * brightness),
            int(f_color[1] * brightness),
            int(f_color[2] * brightness)
        )
        LEDs.setpixelcolor_int(ledpixels, 0, c)

        # 2. Set Resonators (Index 1-8)
        for i in range(8):
            level = current_state['resonators'][i]
            r_color = RESONATOR_COLORS[level]
            rc = LEDs.Color(
                int(r_color[0] * brightness),
                int(r_color[1] * brightness),
                int(r_color[2] * brightness)
            )
            LEDs.setpixelcolor_int(ledpixels, i + 1, rc)

        LEDs.writestrip(ledpixels)
        time.sleep(0.05) # ~20 FPS

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Tecthulhu Controller</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; background-color: #121212; color: #e0e0e0; text-align: center; padding: 20px; }
        h1 { color: #00d4ff; }
        .section { margin-bottom: 30px; padding: 15px; border: 1px solid #333; border-radius: 10px; }
        .btn { display: inline-block; padding: 10px 15px; margin: 3px; font-size: 14px; border: none; border-radius: 5px; cursor: pointer; color: white; text-decoration: none; }
        .enl { background-color: #02BF02; }
        .res { background-color: #0492D0; }
        .neu { background-color: #666; }
        .res-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; max-width: 800px; margin: 0 auto; }
        .res-box { background: #222; padding: 10px; border-radius: 8px; }
        .lvl-btn { display: inline-block; width: 25px; height: 25px; line-height: 25px; margin: 2px; font-size: 10px; text-decoration: none; color: #fff; border-radius: 3px; background: #444; }
        .active { outline: 2px solid #fff; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Tecthulhu Prime</h1>
    
    <div class="section">
        <h3>Faction</h3>
        <a href="/set_faction/Enlightened" class="btn enl {% if state.faction == 'Enlightened' %}active{% endif %}">Enlightened</a>
        <a href="/set_faction/Resistance" class="btn res {% if state.faction == 'Resistance' %}active{% endif %}">Resistance</a>
        <a href="/set_faction/Neutral" class="btn neu {% if state.faction == 'Neutral' %}active{% endif %}">Neutral</a>
    </div>

    <h3>Resonators (R1 - R8)</h3>
    <div class="res-grid">
        {% for i in range(8) %}
        <div class="res-box">
            <strong>R{{ i + 1 }}</strong><br>
            {% for lvl in range(9) %}
                <a href="/set_res/{{ i }}/{{ lvl }}" 
                   class="lvl-btn {% if state.resonators[i] == lvl %}active{% endif %}" 
                   style="border-bottom: 3px solid rgb({{ res_colors[lvl][0] }},{{ res_colors[lvl][1] }},{{ res_colors[lvl][2] }})">
                   {{ lvl if lvl > 0 else 'X' }}
                </a>
            {% endfor %}
        </div>
        {% endfor %}
    </div>

    <br><br>
    <div class="section">
        <a href="/all_max" class="btn" style="background: #555;">All L8</a>
        <a href="/all_off" class="btn" style="background: #000; border: 1px solid #555;">All OFF</a>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, state=current_state, res_colors=RESONATOR_COLORS)

@app.route('/set_faction/<faction>')
def set_faction(faction):
    if faction in COLORS:
        current_state['faction'] = faction
    return redirect(url_for('index'))

@app.route('/set_res/<int:index>/<int:level>')
def set_res(index, level):
    if 0 <= index < 8 and 0 <= level <= 8:
        current_state['resonators'][index] = level
    return redirect(url_for('index'))

@app.route('/all_max')
def all_max():
    current_state['resonators'] = [8] * 8
    return redirect(url_for('index'))

@app.route('/all_off')
def all_off():
    current_state['resonators'] = [0] * 8
    current_state['faction'] = 'Neutral'
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Start animation thread
    threading.Thread(target=led_animation_loop, daemon=True).start()
    
    # Run Flask
    app.run(host='0.0.0.0', port=5000)