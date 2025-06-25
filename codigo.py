# -*- coding: utf-8 -*-
import os
from moviepy.editor import *

# --- 1. CONFIGURACIÓN DEL PROYECTO ---
# Asegúrate de que los nombres de archivo coincidan con los que descargaste.
CLIP_MITO_PATH = "clip_mito.mp4"
CLIP_REALIDAD_PATH = "clip_realidad.mp4"
CLIP_SISTEMA_PATH = "clip_sistema.mp4"
CLIP_CTA_PATH = "clip_cta.mp4"
AUDIO_PATH = "musica_fondo.mp3"
FONT_PATH = "fuente_personalizada.ttf" # Si no tienes una, puedes comentar esta línea
OUTPUT_FILENAME = "video_final_MitoVsRealidad.mp4"

# Parámetros de video y texto
VIDEO_SIZE = (1080, 1920) # Formato vertical para TikTok/Reels
TEXT_COLOR = 'white'
TEXT_STROKE_COLOR = 'black'
TEXT_STROKE_WIDTH = 2
HEADER_FONT_SIZE = 120
BODY_FONT_SIZE = 90

# --- VERIFICACIÓN DE ARCHIVOS (para evitar errores) ---
for path in [CLIP_MITO_PATH, CLIP_REALIDAD_PATH, CLIP_SISTEMA_PATH, CLIP_CTA_PATH, AUDIO_PATH]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Error: El archivo '{path}' no se encuentra. Asegúrate de que esté en la misma carpeta que el script.")
if not os.path.exists(FONT_PATH):
    print(f"Advertencia: Fuente '{FONT_PATH}' no encontrada. Se usará una fuente predeterminada.")
    FONT_PATH = 'Arial-Bold' # Fuente de respaldo

# --- 2. CREACIÓN DE LAS ESCENAS ---

# --- Escena 1: MITO (Duración: 3 segundos) ---
print("Procesando Escena 1: MITO...")
clip_mito_base = (VideoFileClip(CLIP_MITO_PATH)
                  .subclip(0, 3)
                  .resize(height=VIDEO_SIZE[1])
                  .crop(x_center=VIDEO_SIZE[0]/2, y_center=VIDEO_SIZE[1]/2, width=VIDEO_SIZE[0], height=VIDEO_SIZE[1])
                  .fx(vfx.blackwhite)) # Efecto blanco y negro para el mito

txt_mito_header = TextClip("MITO", fontsize=HEADER_FONT_SIZE, color=TEXT_COLOR, font=FONT_PATH, stroke_color=TEXT_STROKE_COLOR, stroke_width=TEXT_STROKE_WIDTH).set_pos('center').set_duration(3)
txt_mito_body = TextClip("“Con tener redes ya vendo” ❌", fontsize=BODY_FONT_SIZE, color=TEXT_COLOR, font=FONT_PATH, stroke_color=TEXT_STROKE_COLOR, stroke_width=TEXT_STROKE_WIDTH).set_pos(('center', 150)).set_duration(3)

scene1 = CompositeVideoClip([clip_mito_base, txt_mito_header, txt_mito_body]).set_duration(3)

# --- Escena 2: REALIDAD (Duración: 4 segundos) ---
print("Procesando Escena 2: REALIDAD...")
clip_realidad_base = (VideoFileClip(CLIP_REALIDAD_PATH)
                      .subclip(0, 4)
                      .resize(height=VIDEO_SIZE[1])
                      .crop(x_center=VIDEO_SIZE[0]/2, y_center=VIDEO_SIZE[1]/2, width=VIDEO_SIZE[0], height=VIDEO_SIZE[1]))

txt_realidad_header = TextClip("REALIDAD", fontsize=HEADER_FONT_SIZE, color=TEXT_COLOR, font=FONT_PATH, stroke_color=TEXT_STROKE_COLOR, stroke_width=TEXT_STROKE_WIDTH).set_pos('center').set_duration(4)
txt_realidad_body = TextClip("Las redes son solo el anzuelo 🎣", fontsize=BODY_FONT_SIZE, color=TEXT_COLOR, font=FONT_PATH, stroke_color=TEXT_STROKE_COLOR, stroke_width=TEXT_STROKE_WIDTH).set_pos(('center', 150)).set_duration(4)

scene2 = CompositeVideoClip([clip_realidad_base, txt_realidad_header, txt_realidad_body]).set_duration(4)

# --- Escena 3: EXPLICACIÓN (Duración: 5 segundos) ---
print("Procesando Escena 3: EXPLICACIÓN...")
clip_sistema_base = (VideoFileClip(CLIP_SISTEMA_PATH)
                     .subclip(0, 5)
                     .resize(height=VIDEO_SIZE[1])
                     .crop(x_center=VIDEO_SIZE[0]/2, y_center=VIDEO_SIZE[1]/2, width=VIDEO_SIZE[0], height=VIDEO_SIZE[1]))

# Textos que aparecen secuencialmente
txt_sistema1 = TextClip("Atraes en redes...", fontsize=BODY_FONT_SIZE, color=TEXT_COLOR, font=FONT_PATH, stroke_color=TEXT_STROKE_COLOR, stroke_width=TEXT_STROKE_WIDTH).set_pos(('center', 200)).set_start(0).set_duration(1.5)
txt_sistema2 = TextClip("...llevas a un lugar...", fontsize=BODY_FONT_SIZE, color=TEXT_COLOR, font=FONT_PATH, stroke_color=TEXT_STROKE_COLOR, stroke_width=TEXT_STROKE_WIDTH).set_pos(('center', 400)).set_start(1.5).set_duration(2)
txt_sistema3 = TextClip("...y AHÍ es donde vendes. ⚙️", fontsize=BODY_FONT_SIZE, color=TEXT_COLOR, font=FONT_PATH, stroke_color=TEXT_STROKE_COLOR, stroke_width=TEXT_STROKE_WIDTH).set_pos(('center', 600)).set_start(3.5).set_duration(1.5)

scene3 = CompositeVideoClip([clip_sistema_base, txt_sistema1, txt_sistema2, txt_sistema3]).set_duration(5)

# --- Escena 4: CTA (Duración: 4 segundos) ---
print("Procesando Escena 4: CTA...")
clip_cta_base = (VideoFileClip(CLIP_CTA_PATH)
                 .subclip(0, 4)
                 .resize(height=VIDEO_SIZE[1])
                 .crop(x_center=VIDEO_SIZE[0]/2, y_center=VIDEO_SIZE[1]/2, width=VIDEO_SIZE[0], height=VIDEO_SIZE[1]))

txt_cta_pregunta = TextClip("Y tú, ¿ya tienes un sistema\no solo publicas?", fontsize=BODY_FONT_SIZE, color=TEXT_COLOR, font=FONT_PATH, stroke_color=TEXT_STROKE_COLOR, stroke_width=TEXT_STROKE_WIDTH, align='center').set_pos('center').set_duration(4)
txt_cta_comenta = TextClip("👇 Cuéntame abajo 👇", fontsize=BODY_FONT_SIZE-10, color=TEXT_COLOR, font=FONT_PATH, stroke_color=TEXT_STROKE_COLOR, stroke_width=TEXT_STROKE_WIDTH).set_pos(('center', VIDEO_SIZE[1] * 0.75)).set_duration(4)

scene4 = CompositeVideoClip([clip_cta_base, txt_cta_pregunta, txt_cta_comenta]).set_duration(4)

# --- 3. ENSAMBLAJE FINAL ---
print("Ensamblando el video final...")

# Concatenar todas las escenas en un solo video
final_video = concatenate_videoclips([scene1, scene2, scene3, scene4], method="compose")

# Añadir la música de fondo
audio_background = AudioFileClip(AUDIO_PATH).set_duration(final_video.duration)
final_clip_with_audio = final_video.set_audio(audio_background)

# --- 4. EXPORTACIÓN DEL VIDEO ---
print(f"Exportando el video a '{OUTPUT_FILENAME}'... Esto puede tardar unos minutos.")
final_clip_with_audio.write_videofile(
    OUTPUT_FILENAME,
    codec='libx264',
    audio_codec='aac',
    temp_audiofile='temp-audio.m4a',
    remove_temp=True,
    fps=24 # FPS estándar para redes sociales
)

print("¡Video generado con éxito! ✨")
