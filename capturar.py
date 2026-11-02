import cv2, os, sys, time

carpeta = sys.argv[1]           # ej: capturas\banana   o   capturas\vacio
os.makedirs(carpeta, exist_ok=True)
nombre = os.path.basename(carpeta)
n = len(os.listdir(carpeta))

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print("ESPACIO = guardar foto | q = salir")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    vista = frame.copy()
    cv2.putText(vista, f"{nombre}: {n}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Captura", vista)
    k = cv2.waitKey(1) & 0xFF
    if k == 32:
        cv2.imwrite(os.path.join(carpeta, f"{nombre}_{int(time.time()*1000)}.jpg"), frame)
        n += 1
    elif k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()