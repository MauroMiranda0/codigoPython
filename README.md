# codigoPython

Este proyecto contiene un script llamado `codigo.py` que genera un video vertical a partir de varios clips, un audio de fondo y una fuente personalizada.

## Requisitos

1. **Python 3**
2. **moviepy** - Librería para edición de video.
3. **ffmpeg** - Backend necesario para procesar video y audio.

Puedes instalar las dependencias de Python ejecutando:

```bash
pip install moviepy
```

Asegúrate también de que `ffmpeg` esté disponible en tu sistema. En la mayoría de las distribuciones de Linux puedes instalarlo con:

```bash
sudo apt-get install ffmpeg
```

## Archivos de entrada

Coloca los siguientes archivos en la misma carpeta que `codigo.py`:

- `clip_mito.mp4`        – Primer video (3 s).
- `clip_realidad.mp4`    – Segundo video (4 s).
- `clip_sistema.mp4`     – Tercer video (5 s).
- `clip_cta.mp4`         – Cuarto video (4 s).
- `musica_fondo.mp3`     – Pista de audio.
- `fuente_personalizada.ttf` – Fuente opcional para los textos. Si no se encuentra, se usará una fuente predeterminada.

## Ejecución

Desde la terminal, ejecuta los siguientes pasos:

```bash
# 1. Instala las dependencias (si no lo has hecho)
pip install moviepy
sudo apt-get install ffmpeg

# 2. Ejecuta el script
python3 codigo.py
```

El video final se guardará con el nombre `video_final_MitoVsRealidad.mp4`.
