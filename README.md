
#  Desarrollo de Prototipos IoT con ESP32

Este repositorio contiene la implementación de dos proyectos IoT desarrollados como parte del curso de la Tecnicatura Superior en Desarrollo de Software del ISPC. Ambos proyectos utilizan la plataforma ESP32 y el simulador Wokwi.


## Proyectos

## 1. Controlador de Riego Automático
- **Descripción:** Sistema que riega automáticamente plantas según la humedad del suelo.
- **Componentes:**
  - Sensor de humedad del suelo.
  - Pantalla OLED.
  - LED que simula una bomba de agua.
- **Características:**
  - Riego automático cuando la humedad está por debajo del 30%.
  - Detención del riego cuando la humedad alcanza el 60%.
  - Datos de humedad mostrados en tiempo real en la pantalla OLED.

[🔗 Proyecto en Wokwi](https://wokwi.com/projects/408567695015950337)

## 2. Termostato Wi-Fi
- **Descripción:** Dispositivo para controlar la temperatura del hogar de manera remota.
- **Componentes:**
  - Sensor DHT22 para medir temperatura y humedad.
  - Relé para controlar dispositivos de calefacción o ventilación.
  - Aplicación Blynk para el monitoreo remoto.
- **Características:**
  - Control remoto desde cualquier dispositivo con Blynk.
  - Activación de ventilador/calefacción según temperatura predefinida.

[🔗 Proyecto en Wokwi](https://wokwi.com/projects/408676052052227073)


##  Tecnologia utilizada

- **ESP32** para el control y la conectividad.
- **MicroPython** para la programación de los prototipos.
- **Simulador Wokwi** para pruebas virtuales.
- **Blynk App** para el monitoreo remoto del Termostato Wi-Fi.


## Posibles Mejoras
- Implementar alertas para fallos en los sensores o dispositivos.
- Registrar históricos de datos para análisis.
- Configurar umbrales dinámicos desde la app Blynk.
- Optimizar la conexión MQTT para mayor eficiencia.

## Pasos para la instalación

1. **Clona el repositorio:**

   git clone https://github.com/tuusuario/proyectos-iot-esp32.git

#Requerimientos:

- Una placa ESP32.
- Simulador Wokwi o hardware real.
- Credenciales de red WiFi para el Termostato.
- Token de autenticación de la app Blynk.


#Carga de código:
- Configura el entorno de MicroPython en tu ESP32.
- Carga el archivo correspondiente desde este repositorio.

#Configuración:

- Actualiza el código con tus credenciales de red WiFi.
- Inserta el token de autenticación de Blynk en el proyecto del Termostato.
    
