# miniproyecto2
mini proyecto 2 inteligencia artificial, contador de dedos con arduino y display de 7 segmentos

# Miniproyecto 2: Contador de Dedos usando Python, Arduino y Display de 7 segmentos

## 🧩 Descripción

Este proyecto implementa un sistema de visión por computadora que detecta entre 0 y 5 dedos levantados mediante una cámara, usando Python, OpenCV y MediaPipe.  
El número detectado se envía vía puerto serial a un Arduino UNO, que a su vez muestra el conteo en un display de 7 segmentos utilizando un decodificador 7447.

## Tecnologías utilizadas

- Python 3.x
- OpenCV
- MediaPipe
- PySerial
- Arduino IDE

## Hardware necesario

- Arduino UNO
- Decodificador BCD a 7 segmentos 7447
- Display de 7 segmentos (Ánodo Común)
- Resistencias (220Ω)
- Cables jumper
- Protoboard

## Funcionamiento

1. **Detección de dedos**:
   - Python captura video en tiempo real con OpenCV.
   - MediaPipe analiza la posición de los dedos.
   - Se cuenta el número de dedos levantados (0 a 5).

2. **Comunicación Serial**:
   - Cada vez que cambia el número de dedos, se envía el número al Arduino a través del puerto COM3.

3. **Visualización**:
   - Arduino recibe el número.
   - Codifica el número en BCD (4 bits) y lo manda al 7447.
   - El 7447 decodifica los 4 bits para activar los segmentos correctos en el display.

## Codigo principal

- `main.py`: Detección de dedos y envío de número por Serial.
- `arduino.ino`: Lectura del número Serial y actualización del display.

## Esquema de conexión

- Arduino D2 → 7447 A (pin 7)
- Arduino D3 → 7447 B (pin 1)
- Arduino D4 → 7447 C (pin 2)
- Arduino D5 → 7447 D (pin 6)
- Arduino 5V → 7447 VCC (pin 16)
- Arduino GND → 7447 GND (pin 8)
- 7447 salidas (a, b, c, d, e, f, g) → Display 7 segmentos
- Entradas LT, BI/RBO, RBI del 7447 conectadas a 5V.

> se usaron resistencias de 330 homios entre las salidas del 7447 y el display.

## consideraciones

- El display de 7 segmentos utilizado fue Ánodo Común.
- Configurar correctamente la comunicación Serial a la misma velocidad en Python y Arduino (9600 baudios).

## 📷 Video del programa funcionando 
likn del video explicando 
https://drive.google.com/drive/folders/1-zml_85W6Kbqbi92z91sSKhmY9fPm34i?usp=drive_link

---
