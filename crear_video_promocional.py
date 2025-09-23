from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
import numpy as np
from datetime import datetime

def crear_video_promocional():
    # Configuración inicial
    W, H = 1080, 1920  # Formato vertical para redes sociales
    duracion_total = 5  # 5 segundos
    
    # Crear clips vacíos para cada segmento
    clips = []
    
    # SEGMENTO 1: 0-1 segundos - Vista aérea y título
    def segmento1(t):
        # Fondo con gradiente azul
        fondo = np.zeros((H, W, 3))
        for i in range(H):
            fondo[i, :, 0] = 0.1 + 0.4 * i/H  # Azul gradual
            fondo[i, :, 2] = 0.6 * i/H        # Rojo gradual
        
        # Texto principal
        texto = TextClip("22,835 m² FRENTE A BAJA MALIBÚ", 
                        fontsize=48, color='white', font='Arial-Bold',
                        stroke_color='black', stroke_width=2)
        texto = texto.set_position(('center', H*0.3)).set_duration(1).set_start(0)
        
        # Icono de ubicación
        ubicacion = TextClip("📍", fontsize=80, color='white')
        ubicacion = ubicacion.set_position(('center', H*0.2)).set_duration(1).set_start(0)
        
        return CompositeVideoClip([ImageClip(fondo).set_duration(1), texto, ubicacion])
    
    # SEGMENTO 2: 1-2.5 segundos - Precio de oportunidad
    def segmento2(t):
        fondo = ColorClip(size=(W, H), color=(0, 50, 100)).set_duration(1.5)
        
        texto_precio = TextClip("PRECIO DE OPORTUNIDAD", fontsize=42, 
                               color='yellow', font='Arial-Bold')
        texto_precio = texto_precio.set_position(('center', H*0.3))
        
        precio = TextClip("$80 USD/m²", fontsize=72, color='white', 
                         font='Arial-Bold', stroke_color='red', stroke_width=3)
        precio = precio.set_position(('center', H*0.45))
        
        # Gráfico de crecimiento
        crecimiento = TextClip("📈", fontsize=100, color='green')
        crecimiento = crecimiento.set_position(('center', H*0.65))
        
        return CompositeVideoClip([fondo, texto_precio, precio, crecimiento]).set_start(1)
    
    # SEGMENTO 3: 2.5-4 segundos - Comparativo
    def segmento3(t):
        fondo = ColorClip(size=(W, H), color=(30, 30, 60)).set_duration(1.5)
        
        texto = TextClip("VS PRECIO DE ZONA: $2,800 USD/m²", fontsize=36, 
                        color='white', font='Arial-Bold')
        texto = texto.set_position(('center', H*0.3))
        
        # Flecha de crecimiento
        flecha = TextClip("⬆️ 3500% PLUSVALÍA", fontsize=44, color='#00ff00', 
                         font='Arial-Bold')
        flecha = flecha.set_position(('center', H*0.5))
        
        explosion = TextClip("💥 OPORTUNIDAD ÚNICA", fontsize=40, color='orange')
        explosion = explosion.set_position(('center', H*0.65))
        
        return CompositeVideoClip([fondo, texto, flecha, explosion]).set_start(2.5)
    
    # SEGMENTO 4: 4-5 segundos - Contacto
    def segmento4(t):
        fondo = ColorClip(size=(W, H), color=(0, 30, 60)).set_duration(1)
        
        nombre = TextClip("Jesús García Farrera", fontsize=46, color='white', 
                         font='Arial-Bold')
        nombre = nombre.set_position(('center', H*0.3))
        
        telefono = TextClip("📞 664 500 6645", fontsize=38, color='yellow')
        telefono = telefono.set_position(('center', H*0.45))
        
        email = TextClip("✉️ farreratijuanahomes@gmail.com", fontsize=34, color='cyan')
        email = email.set_position(('center', H*0.55))
        
        urgente = TextClip("¡NO DEJES PASAR ESTA OPORTUNIDAD!", fontsize=32, 
                          color='red', font='Arial-Bold')
        urgente = urgente.set_position(('center', H*0.7))
        
        return CompositeVideoClip([fondo, nombre, telefono, email, urgente]).set_start(4)
    
    # Crear y unir todos los segmentos
    clip_final = CompositeVideoClip([
        segmento1(0),
        segmento2(0),
        segmento3(0),
        segmento4(0)
    ], size=(W, H))
    
    # Agregar música de fondo (opcional - necesitarías un archivo de audio)
    # audio = AudioFileClip("musica_fondo.mp3").subclip(0, 5)
    # clip_final = clip_final.set_audio(audio)
    
    # Exportar video
    fecha = datetime.now().strftime("%Y%m%d_%H%M")
    nombre_archivo = f"promocion_terreno_{fecha}.mp4"
    
    clip_final.write_videofile(
        nombre_archivo,
        fps=24,
        codec='libx264',
        audio_codec='aac',
        threads=4,
        preset='fast'
    )
    
    print(f"✅ Video creado exitosamente: {nombre_archivo}")
    return nombre_archivo

# Instalación de dependencias necesarias (ejecutar en terminal)
def instalar_dependencias():
    """
    Ejecutar en terminal:
    pip install moviepy numpy pillow
    """
    print("Instala las dependencias con: pip install moviepy numpy pillow")

if __name__ == "__main__":
    # Instalar dependencias primero si no están instaladas
    try:
        from moviepy.editor import *
        print("Creando video promocional...")
        crear_video_promocional()
    except ImportError:
        print("❌ Dependencias no instaladas.")
        instalar_dependencias()