from machine import Pin, ADC, I2C #el módulo machine controla al
ESP32
from time import sleep #Importamos la libreria time con su modulo time, que detiene la ejecucion del programa por un tiempoespecificado.
import ssd1306 #importamos un módulo de control a las pantallas oled.


# Configuración de pines
sensor_humedad = ADC(Pin(34)) # Simulación con potenciómetro
sensor_humedad.atten(ADC.ATTN_11DB) # Configuración para rango completo (0-3.3V)
led_bomba = Pin(5, Pin.OUT) # Simula la bomba con un LED


# Inicializar pantalla OLED (I2C)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


# Umbral de humedad
UMBRAL_HUMEDAD_BAJA = 30 # Valor simulado de humedad mínima
UMBRAL_HUMEDAD_ALTA = 60 # Valor simulado de humedad alta

while True:
# Leer valor del potenciómetro como simulación de la humedad  del suelo
    humedad = sensor_humedad.read() * 100 / 4095 # Convertir a porcentaje (0-100%)

# Muestra los valores en la pantalla OLED
    oled.fill(0) # Limpia la pantalla
    oled.text('Humedad: {:.1f}%'.format(humedad), 0, 0)

# Activar o desactivar la bomba (LED) según el nivel de humedad
if humedad < UMBRAL_HUMEDAD_BAJA:
    oled.text('Estado: Riego', 0, 20)
    led_bomba.on() # Encender bomba

elif humedad > UMBRAL_HUMEDAD_ALTA:
    oled.text('Estado: No Riego', 0, 20)
    led_bomba.off() # Apagar bomba

oled.show() # Actualizar pantalla

print('Humedad: {:.1f}%'.format(humedad))

sleep(1)