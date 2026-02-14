import cv2
from ultralytics import YOLO

MODEL_PATH = "./best.pt"
model = YOLO(MODEL_PATH)

def open_camera(indexes=(0, 1, 2), backends=(cv2.CAP_AVFOUNDATION, cv2.CAP_ANY)):
    for backend in backends:
        for idx in indexes:
            cap = cv2.VideoCapture(idx, backend)
            if cap.isOpened():
                print(f"Cámara abierta con index={idx}, backend={backend}")
                return cap
            cap.release()
    return None

cap = open_camera()
if cap is None:
    raise SystemExit(
        "No se pudo abrir la cámara.\n"
        "• En macOS: Ajustes del sistema → Privacidad y seguridad → Cámara → "
        "activa el acceso para la app que usas (Terminal, iTerm, VS Code, PyCharm).\n"
        "• Cierra otras apps que puedan estar usando la cámara (Zoom, Meet, QuickTime).\n"
        "• Si tienes cámara externa, prueba otros índices (0/1/2)."
    )

cv2.namedWindow("YOLO", cv2.WINDOW_NORMAL)

while True:
    ok, frame = cap.read()
    if not ok:
        print("No se pudo leer frame.")
        break

    results = model.predict(frame, conf=0.5, iou=0.45, verbose=False)
    annotated = results[0].plot()  # dibuja cajas + etiquetas con Ultralytics

    # Opción: espejar estilo “selfie”
    # annotated = cv2.flip(annotated, 1)

    cv2.imshow("YOLO (ESC para salir)", annotated)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()