# Wiring Diagram / 接続図

This document outlines how to connect the WS2801 LED strip to the Raspberry Pi.
WS2801 LEDテープをRaspberry Piに接続する方法を説明します。

## Pinout / ピン配置

| Function | Raspberry Pi (Physical Pin) | WS2801 Strip |
| :--- | :--- | :--- |
| **Data (MOSI)** | **Pin 19** (GPIO 10) | **DI** (Data In) |
| **Clock (SCLK)** | **Pin 23** (GPIO 11) | **CI** (Clock In) |
| **Ground** | **Pin 6** (GND) | **GND** |
| **Power (5V)** | *External PSU (+)* OR *Pin 2/4* | **5V / VCC** |

---

## Configuration A: External Power Supply (Recommended)
## 構成A: 外部電源を使用する場合（推奨）

For strips with more than 10-15 LEDs, using an external 5V power supply is strongly recommended to prevent damaging the Raspberry Pi.
LEDが10〜15個以上ある場合は、Raspberry Piの破損を防ぐため、外部5V電源の使用を強く推奨します。

**IMPORTANT**: You must connect the Power Supply GND to **BOTH** the LED Strip GND **AND** the Raspberry Pi GND (Common Ground).
**重要**: 電源のGND（マイナス）は、LEDテープのGND **かつ** Raspberry PiのGNDの両方に接続してください（共通グランド）。

```mermaid
graph LR
    subgraph Raspberry Pi
        P19[Pin 19: MOSI]
        P23[Pin 23: SCLK]
        P6[Pin 6: GND]
    end

    subgraph WS2801 LED Strip
        DI[DI / Data]
        CI[CI / Clock]
        LG[GND]
        LV[5V]
    end

    subgraph "External Power Supply (5V)"
        PSU_P[+]
        PSU_N[-]
    end

    P19 ==> DI
    P23 ==> CI
    
    PSU_P ==> LV
    PSU_N ==> LG
    PSU_N ==> P6
    style PSU_N stroke:#f00,stroke-width:2px
    style P6 stroke:#f00,stroke-width:2px
    style LG stroke:#f00,stroke-width:2px
```

### ASCII Diagram

```text
[ Raspberry Pi ]                  [ WS2801 LED Strip ]
|              |                  |                  |
|  Pin 19 ------------------------> DI (Data)        |
|  (MOSI)      |                  |                  |
|              |                  |                  |
|  Pin 23 ------------------------> CI (Clock)       |
|  (SCLK)      |                  |                  |
|              |                  |                  |
|  Pin 6  -----+                  |  5V (VCC) <-----------+
|  (GND)       |                  |                  |    |
|              |                  |  GND  <-----------+   |
+--------------+                  |                  |    |
               |                  +------------------+    |
               |                                          |
               |                                          |
      [ Common Ground connection ]                        |
               |                                          |
               |         [ External 5V Power Supply ]     |
               |         |                          |     |
               +---------| (-) GND          (+) 5V  |-----+
                         +--------------------------+
```

---

## Configuration B: Powered by Pi (Testing Only)
## 構成B: Piから給電する場合（テスト用のみ）

Use this ONLY for short strips (e.g., < 10 LEDs).
LEDが少ない（10個未満など）場合のみ使用してください。

```mermaid
graph LR
    subgraph Raspberry Pi
        P19[Pin 19: MOSI]
        P23[Pin 23: SCLK]
        P6[Pin 6: GND]
        P2[Pin 2 or 4: 5V]
    end

    subgraph WS2801 LED Strip
        DI[DI / Data]
        CI[CI / Clock]
        LG[GND]
        LV[5V]
    end

    P19 --> DI
    P23 --> CI
    P6  --> LG
    P2  --> LV
```
