import sys, time
from pathlib import Path

import cv2
import torch
from ultralytics import YOLO

PESOS = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("modelos") / "yolo26l_best.pt"
CONF = 0.4
DEVICE = 0 if torch.cuda.is_available() else "cpu"

if not PESOS.exists():
    sys.exit(f"No se encontró el modelo: {PESOS}")
print(f"Modelo: {PESOS} | dispositivo: {DEVICE}")
model = YOLO(str(PESOS))

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    sys.exit("No se pudo abrir la cámara. Cierra otras apps que la usen o prueba otro índice.")

while True:
    t0 = time.time()
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame, device=DEVICE, conf=CONF, verbose=False)
    img = results[0].plot()
    fps = 1 / (time.time() - t0)
    cv2.putText(img, f"{fps:.1f} FPS", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("YOLO frutas", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()