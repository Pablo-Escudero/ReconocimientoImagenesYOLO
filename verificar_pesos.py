import sys
from ultralytics import YOLO

for ruta in sys.argv[1:]:
    m = YOLO(ruta)
    a = m.ckpt["train_args"]
    print(ruta)
    print("  clases:", m.names)
    print("  épocas:", a.get("epochs"), "| fraction:", a.get("fraction"))
    print("  carpeta de origen:", a.get("save_dir"))