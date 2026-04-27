# 📝 Relatório do Candidato

## 👤 Identificação do Candidato

**Nome completo:** Guilherme Silva 
**GitHub:** https://github.com/silva-guilherme

---

## 1️⃣ Visão Geral da Solução

O projeto tem como objetivo desenvolver um sistema embarcado de automação residencial utilizando um **ESP32** para controle automático de dispositivos com base na temperatura ambiente.

O sistema simulado realiza a leitura de temperatura através de um sensor **DHT22** e, ao identificar valores acima de um limite definido (30°C), aciona automaticamente dispositivos representados por LEDs (luz, ar-condicionado e televisão). Quando a temperatura retorna ao normal, os dispositivos são desligados após um intervalo de tempo configurado.

A interação do usuário é indireta, ocorrendo por meio da variação da temperatura no ambiente simulado, sem necessidade de comandos manuais,visando economia de energia.

---

## 2️⃣ Arquitetura do Sistema Embarcado

O sistema segue uma arquitetura simples, porém eficiente, baseada em loop principal com controle de estado.

### 🔹 Fluxo principal (main.py)

1. Inicialização dos pinos GPIO (entrada e saída)
2. Inicialização do sensor de temperatura
3. Loop infinito:

   * Leitura da temperatura
   * Verificação de limite térmico
   * Controle dos dispositivos
   * Controle temporal para desligamento

### 🔹 Estrutura lógica

O sistema utiliza uma abordagem baseada em estado:

* `estado_ligado = False` → dispositivos desligados
* `estado_ligado = True` → dispositivos ligados

Além disso, utiliza uma variável de tempo (`ultimo_evento_quente`) para evitar desligamentos imediatos, implementando uma lógica de histerese temporal.

### 🔹 Interação entre componentes

```
Sensor DHT22 → ESP32 → Decisão lógica → GPIO → LEDs (atuadores)
```

O ESP32 atua como unidade central, processando os dados do sensor e acionando os dispositivos conforme as regras definidas.

---

## 3️⃣ Componentes Utilizados na Simulação

* **ESP32**

  * Microcontrolador responsável pelo processamento e controle do sistema

* **Sensor DHT22**

  * Responsável pela leitura da temperatura ambiente

* **LEDs (3 unidades)**

  * Representam dispositivos reais:

    * Luz
    * Ar-condicionado
    * Televisão

* **Resistores**

  * Utilizados para proteção dos LEDs

### 🔹 Função no sistema

| Componente | Função                              |
| ---------- | ----------------------------------- |
| ESP32      | Processamento e controle            |
| DHT22      | Leitura de temperatura              |
| LEDs       | Simulação de dispositivos           |
| GPIOs      | Interface entre controle e hardware |

---

## 4️⃣ Decisões Técnicas Relevantes

Durante o desenvolvimento, foram adotadas as seguintes decisões:

* **Separação em funções**

  * `ligar_dispositivos()` e `desligar_dispositivos()` para melhorar organização e reutilização

* **Uso de constantes**

  * `LIMITE_TEMPERATURA` e `TEMPO_DESLIGAR` facilitam manutenção e ajuste do sistema

* **Controle de estado**

  * Evita comandos repetidos e melhora eficiência

* **Controle temporal com `time.time()`**

  * Permite lógica baseada em tempo sem depender exclusivamente de delays

* **Tratamento de erros**

  * Uso de `try/except` para lidar com falhas na leitura do sensor

* **Estrutura simples e eficiente**

  * Pensada para sistemas embarcados com recursos limitados

---

## 5️⃣ Resultados Obtidos

O sistema apresentou funcionamento correto na simulação, com os seguintes comportamentos:

* Leitura contínua da temperatura
* Acionamento automático dos dispositivos ao ultrapassar 30°C
* Desligamento após retorno à temperatura normal
* Estabilidade durante execução

### ✔ Requisitos atendidos

* Leitura de sensor funcional
* Controle de atuadores correto
* Integração consistente entre hardware e firmware
* Execução sem erros na simulação

O projeto se mostrou coerente entre código (`main.py`) e circuito (`diagram.json`), atendendo aos critérios de funcionamento no ambiente Wokwi.

---

## 6️⃣ Comentários Adicionais (Opcional)

### 🔹 Dificuldades encontradas

* Ajustar a lógica para evitar acionamentos repetitivos
* Garantir consistência entre código e diagrama

### 🔹 Limitações

* Uso de `sleep()` (abordagem bloqueante)
* Ausência de comunicação com rede (IoT)

### 🔹 Melhorias futuras

* Implementação de temporização não-bloqueante
* Uso de máquina de estados mais formal
* Integração com MQTT para controle remoto
* Expansão para múltiplos sensores

### 🔹 Aprendizados

* Integração entre hardware e software embarcado
* Controle eficiente de GPIOs
* Importância de lógica de estados em sistemas embarcados
* Uso de simulação para validação de projetos

