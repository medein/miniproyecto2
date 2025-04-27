import cv2
import mediapipe as mp
import serial
import time

# Configurar el puerto serial
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Esperar a que se establezca la conexión

# Configurar MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Inicializar captura de video
cap = cv2.VideoCapture(0)

# Lista de IDs de las puntas de los dedos
tipIds = [4, 8, 12, 16, 20]

last_count = -1

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))
            
            fingers = []

            # Pulgar
            if lmList[tipIds[0]][0] > lmList[tipIds[0] - 1][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Otros dedos
            for id in range(1, 5):
                if lmList[tipIds[id]][1] < lmList[tipIds[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)

            # Mostrar número en pantalla
            cv2.putText(img, f'Dedos: {totalFingers}', (10, 70), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

            # Enviar al Arduino solo si cambia
            if totalFingers != last_count:
                arduino.write(str(totalFingers).encode())
                last_count = totalFingers

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Imagen", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cierre
cap.release()
arduino.close()
cv2.destroyAllWindows()


