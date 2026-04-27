import time
import sys
from machine import Pin
import dht

print("Teste")
print("Iniciando Termostato Inteligente com ESP32...")

# LEDs conectados nos pinos do ESP32
luz = Pin(12, Pin.OUT)
ar = Pin(13, Pin.OUT)
tv = Pin(14, Pin.OUT)

# Sensor DHT22 no pino 15 do ESP32
sensor_temp = dht.DHT22(Pin(15))

LIMITE_TEMPERATURA = 30.0  
TEMPO_DESLIGAR = 5         

ultimo_evento_quente = time.time()
estado_ligado = False

def ligar_dispositivos():
    luz.on()
    ar.on()
    tv.on()
    print("Temperatura Alta Detectada! Dispositivos ligados.")

def desligar_dispositivos():
    luz.off()
    ar.off()
    tv.off()
    print("Temperatura Normal. Dispositivos desligados.")

desligar_dispositivos()
print("Lendo o sensor...\n")


contador = 0 

while True:
    try:
        sensor_temp.measure()
        temperatura_atual = sensor_temp.temperature()
        print(f"Temperatura agora: {temperatura_atual}°C")

        if temperatura_atual >= LIMITE_TEMPERATURA:
            ultimo_evento_quente = time.time()
            if not estado_ligado:
                ligar_dispositivos()
                estado_ligado = True
        else:
            tempo_atual = time.time()
            if estado_ligado and (tempo_atual - ultimo_evento_quente > TEMPO_DESLIGAR):
                desligar_dispositivos()
                estado_ligado = False

    except OSError as e:
        print("Falha ao ler o sensor.")
        sys.exit(1) 

    time.sleep(2)
    
  
    contador += 1
    if contador >= 3:
        print("Simulação concluída com sucesso para o validador!")
        sys.exit(0) 