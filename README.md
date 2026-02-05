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

## Unimplemented Features

*   **Sound Effects**: Sound file playback functionality is not implemented.

## Installation

### Prerequisites

*   **Hardware**: Raspberry Pi (3B+ or 4 recommended), WS2801 LED Strip.
*   **OS**: Raspberry Pi OS (Bullseye or newer).
*   **Python**: Python 3.

### Setup

1.  **Clone this repository**:
    ```bash
    git clone https://github.com/keiichiyasu/tecthulhu-prime.git
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

---

# Tecthulhu Prime Controller (日本語)

Ingress Primeのポータル状態を可視化するための、Raspberry Pi用LED制御プロジェクトです。
Webインターフェースを通じて手動でLEDの状態を制御し、ポータルの状態（陣営、レベル、ヘルス）をインテリアやコスプレ用にシミュレートすることができます。

## コンプライアンスと安全性について

**重要: 本ツールは、あくまで「手動シミュレーション」専用です。**

**Ingress 利用規約 (ToS)** を完全に遵守するため、本ソフトウェアは以下の仕様となっています：
*   NianticのサーバーやAPIとは**一切通信しません**。
*   Intel Mapからのデータスクレイピングを**行いません**。
*   ゲームからのデータ自動収集を**行いません**。

ポータルの状態は、ユーザー自身が観測に基づき、Webコントロールパネルのボタンを手動で押した時にのみ更新されます。これにより、デスクのインテリアやコスプレ用の物理的なLED演出を、規約を守りながら安全に楽しむことができます。

## 謝辞

このプロジェクトは、2017年の #MagnusReawakens アノマリー用に設計されたMartin Brenner氏によるオリジナルの [Tecthulhu](https://github.com/mtbrenner/tecthulhu) プロジェクトの派生版（フォーク）です。
本バージョンでは、Python 3への対応と、Ingress Primeのビジュアル仕様への適応を行っています。

## 特徴

*   **Ingress Prime カラー**: Enlightened（緑）、Resistance（青）、およびレゾネーターレベル（L1-L8）のカラーパレットを更新しました。
*   **Webコントロールパネル**: ポータルの陣営やステータスを手動で設定するためのシンプルなWebインターフェース（自動スクレイピングを回避し、Ingress利用規約を遵守するため）。
*   **WS2801 対応**: WS2801 アドレス指定可能LEDテープに対応しています。

## 未実装の機能

*   **サウンドエフェクト**: 音声ファイルを再生する機能は実装されていません。

## インストール

### 前提条件

*   **ハードウェア**: Raspberry Pi (3B+ または 4 推奨), WS2801 LEDテープ。
*   **OS**: Raspberry Pi OS (Bullseye 以降)。
*   **Python**: Python 3。

### セットアップ

1.  **リポジトリのクローン**:
    ```bash
    git clone https://github.com/keiichiyasu/tecthulhu-prime.git
    cd tecthulhu-prime
    ```

2.  **依存ライブラリのインストール**:
    ```bash
    sudo apt-get update
    sudo apt-get install python3-pip python3-dev build-essential
    sudo pip3 install RPi.GPIO requests pygame flask
    ```

3.  **SPIの有効化**:
    `sudo raspi-config` を実行し、 **Interface Options** -> **SPI** へ移動して有効化してください。

4.  **配線**:
    WS2801テープをPiに接続します:
    *   VCC -> 5V
    *   GND -> GND
    *   CLK -> Pin 23 (SCLK)
    *   DAT -> Pin 19 (MOSI)

## 使い方

1.  **Webコントローラーの起動**:
    ```bash
    sudo python3 server.py
    ```

2.  **操作**:
    Webブラウザを開き、 `http://<ラズパイのIP>:5000` にアクセスします。
    ボタンを使って陣営の色やレゾネーターのレベルを変更してください。

## ライセンス

本プロジェクトはオープンソースです。ライセンスの詳細については、必要に応じて元のリポジトリを参照してください。
