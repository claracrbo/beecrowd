h_inicial, m_inicial, h_final, m_final = map(int, input().split())
inicio = h_inicial * 60 + m_inicial
fim = h_final * 60 + m_final
duracao = fim - inicio
if duracao <= 0:
    duracao += 24 * 60
horas = duracao // 60
minutos = duracao % 60
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")