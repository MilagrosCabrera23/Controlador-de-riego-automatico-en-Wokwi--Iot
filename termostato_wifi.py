import network
import time
from machine import Pin
from umqtt.simple import MQTTClient
import dht


# Configurar los pines del sensor DHT22 y el relé
sensor_dht = dht.DHT22(Pin(15))
relay = Pin(2, Pin.OUT)

# Credenciales de WiFi y Blynk
WIFI_SSID = 'YOUR_WIFI_SSID'
WIFI_PASS = 'YOU_WIFI_PASSWORD'
BLYNK_AUTH_TOKEN = 'YOUR_BLYNK_AUTH_TOKEN' #Este TOKEN se genera en la app Blynk

# Umbrales de temperatura
TEMP_UMBRAL = 18 # Cambia este valor según el umbral que quieras usar

# Función para conectar a la red WiFi
SSID = 'Wokwi-GUEST'
PASSWORD = ''

def conectar_wifi():
    print("Conectando WiFi", end="")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    while not wlan.isconnected():
        print(".", end="")
        time.sleep(0.1)

    print(" Conectado!")
    print("Dirección IP:", wlan.ifconfig()[0])
    return True

# Función para enviar temperatura a Blynk
def update_blynk_temperature(temp):
    client = MQTTClient('esp32', 'blynk-cloud.com',port=1883)
    client.connect()
    client.publish(f'/v1/{BLYNK_AUTH_TOKEN}/update/V1',
str(temp))
    client.disconnect()


# Función para obtener el control del relé desde Blynk
def get_blynk_control():
    client = MQTTClient('esp32', 'blynk-cloud.com',port=1883)
    client.connect()
    client.subscribe(f'/v1/{BLYNK_AUTH_TOKEN}/get/V2')
    control = client.check_msg() # Espera recibir '1' o '0' desde el botón en Blynk
    client.disconnect()
    return control


# Función principal del termostato
def termostato():
    conectar_wifi()

while True:
    try:
        # Leer temperatura y humedad
        sensor_dht.measure()
        temp = sensor_dht.temperature()
        humedad = sensor_dht.humidity()
        # Imprimir datos en la consola
        print(f'Temperatura: {temp}°C, Humedad:{humedad}%')

    # Enviar temperatura a la aplicación Blynk
        update_blynk_temperature(temp)

        # Obtener estado de control desde la app Blynk
        control = get_blynk_control()

# Controlar el relé según la temperatura y el control remoto
        if control == '1' and temp > TEMP_UMBRAL:
            relay.on() # Encender el calentador/ventilador
            print("Relé activado (calentador/ventilador encendido)")
        else:
            relay.off() # Apagar el calentador/ventilador
            print("Relé desactivado (calentador/ventilador apagado)")

# Esperar 10 segundos antes de la siguiente lectura
        time.sleep(10)

    except OSError as e:
        print("Error leyendo el sensor:", e)
        time.sleep(2)
        
# Ejecutar el termostato
termostato()