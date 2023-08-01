#!/usr/bin/env pybricks-micropython
def seguir_linha(drive_base, sensor_cor_esquerdo, sensor_cor_direito, ev3=null):
    cor_alvo = Color.BLACK
    velocidade_maxima = 300
    velocidade_base = 150
    kp = 1.2
    desvio_referencia = 50

    while True:
        valor_cor_esquerdo = sensor_cor_esquerdo.reflection()
        valor_cor_direito = sensor_cor_direito.reflection()

        if(ev3 != null):
            ev3.screen.clear()
            ev3.screen.print(f"Esquerdo: {valor_cor_esquerdo}, direito: {valor_cor_direito}")

        erro = (valor_cor_esquerdo + valor_cor_direito) / 2 - desvio_referencia
        correcao = erro * kp
        velocidade_esquerda = velocidade_base + correcao
        velocidade_direita = velocidade_base - correcao
        velocidade_esquerda = min(velocidade_esquerda, velocidade_maxima)
        velocidade_direita = min(velocidade_direita, velocidade_maxima)
        drive_base.drive(velocidade_esquerda, velocidade_direita)
