"""
CONSTANTE - "variáveis" que vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de espaços comlexidade (ruim)
"""

velocidade_atual = 61 #velocidade atual do carro
local_carro = 100 # local em que o carro esta na estrada

RADAR_1 = 60 #velocidade máxima radar #constante
LOCAL_1 = 100 #local do radar 1 #constante
RADAR_RANGE = 1 # distância onde o radar pega #constante

velocidade_carro_passou_radar1 = velocidade_atual > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar1 and velocidade_carro_passou_radar1

if velocidade_carro_passou_radar1:
   print("Velocidade passou do radar 1")

if carro_passou_radar1:
    print("Carro passou radar 1")

if carro_multado_radar1:
    print("Carro multado em radar 1")
