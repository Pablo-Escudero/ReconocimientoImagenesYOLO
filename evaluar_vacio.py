import sys, glob
from ultralytics import YOLO

model = YOLO(sys.argv[1])
imgs = glob.glob(sys.argv[2] + r"\*.jpg")
for conf in (0.25, 0.5):
    n = sum(1 for im in imgs if len(model(im, conf=conf, verbose=False)[0].boxes) > 0)
    print(f"conf={conf}: {n}/{len(imgs)} imágenes vacías con alguna detección")