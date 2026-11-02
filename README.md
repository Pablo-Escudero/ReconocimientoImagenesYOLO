# Detección de frutas con YOLO26

Detecta frutas con la cámara web usando un modelo YOLO26 entrenado con un dataset de Roboflow. El entrenamiento se hizo en Google Colab.

## Requisitos
- Windows, Python 3.11 y una cámara web
- GPU NVIDIA con driver compatible con CUDA 12.6 o superior (se comprueba con `nvidia-smi`)

## Instalación
    python -m venv .venv
    .venv\Scripts\activate
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126
    pip install -r requirements.txt
    python -c "import torch; print(torch.cuda.is_available())"

La última línea debe imprimir True. Si imprime False se instaló la versión CPU: ejecutar `pip uninstall -y torch torchvision` y repetir el tercer comando.

Si `activate` da error de scripts deshabilitados: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`.

No instalar `roboflow` en este entorno: trae `opencv-python-headless` y rompe la ventana de la cámara.

## Uso
    python ProbarCamara.py
    python ProbarCamara.py modelos\yolo26s_best.pt

Cierra la ventana con la tecla q. Por defecto usa el modelo large (`modelos\yolo26l_best.pt`).

## Clases
Apple, Banana, Grapes, Mango, Orange, Pineapple, Watermelon.

## Resultados (conjunto de test, 76 imágenes, mAP50)
n 0,772 | s 0,826 | l 0,806 | x 0,807 (el x no se incluye en el repositorio por su tamaño).

## Limitaciones
- Dataset pequeño y mayormente de fotos de catálogo; el test tiene pocas imágenes, así que las cifras son orientativas.
- Banana fue la clase más débil en la evaluación del modelo nano.
- No reconoce plátano. Probado en cámara con pocas frutas reales (banana, mango y naranja).

## Datos
Dataset "Fruits by YOLO" (Fruitsdetection, Roboflow Universe), licencia CC BY 4.0.