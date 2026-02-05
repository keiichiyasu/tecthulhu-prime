# Tecthulhu Prime Controller

A Raspberry Pi project to control LED strips for visualizing Ingress Prime portal status.
This project allows you to manually control the LED status via a web interface, simulating a portal's state (Faction, Level, Health) for decorative or cosplay purposes.

## Compliance & Safety

**IMPORTANT: This tool is strictly for MANUAL simulation.**

To ensure full compliance with the **Ingress Terms of Service (ToS)**, this software:
*   **DOES NOT** interact with Niantic's servers or APIs.
*   **DOES NOT** scrape data from the Intel Map.
*   **DOES NOT** automate any data collection from the game.

The portal status is updated only when the user manually presses buttons on the web control panel based on their own observations. This makes it a safe and "ToS-friendly" way to enjoy physical LED effects for your desk or cosplay.

## Attribution

This project is a fork/derivative of the original [Tecthulhu](https://github.com/mtbrenner/tecthulhu) project by Martin Brenner, originally designed for the #MagnusReawakens anomaly in 2017.
This version has been modernized for Python 3 and adapted for Ingress Prime visual specifications.

## Features

*   **Ingress Prime Colors**: Updated color palettes for Enlightened (Green), Resistance (Blue), and Resonator levels (L1-L8).
*   **Web Control Panel**: A simple web interface to manually set the portal's faction and status (to comply with Ingress Terms of Service by avoiding automated scraping).
*   **WS2801 Support**: Designed for WS2801 addressable LED strips.

## Installation

### Prerequisites

*   **Hardware**: Raspberry Pi (3B+ or 4 recommended), WS2801 LED Strip.
*   **OS**: Raspberry Pi OS (Bullseye or newer).
*   **Python**: Python 3.

### Setup

1.  **Clone this repository**:
    ```bash
    git clone <your-repo-url>
    cd tecthulhu-prime
    ```

2.  **Install Dependencies**:
    ```bash
    sudo apt-get update
    sudo apt-get install python3-pip python3-dev build-essential
    sudo pip3 install RPi.GPIO requests pygame flask
    ```

3.  **Enable SPI**:
    Run `sudo raspi-config`, navigate to **Interface Options** -> **SPI**, and enable it.

4.  **Wiring**:
    Connect your WS2801 strip to the Pi:
    *   VCC -> 5V
    *   GND -> GND
    *   CLK -> Pin 23 (SCLK)
    *   DAT -> Pin 19 (MOSI)

## Usage

1.  **Start the Web Controller**:
    ```bash
    sudo python3 server.py
    ```

2.  **Control**:
    Open a web browser and navigate to `http://<raspberry-pi-ip>:5000`.
    Use the buttons to change the faction color and resonator levels.

## License

This project is open source. Please refer to the original repository for license details where applicable.