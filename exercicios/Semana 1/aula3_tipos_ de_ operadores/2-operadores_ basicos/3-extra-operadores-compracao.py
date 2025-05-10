"""
1. Crie um script Python que declare duas variáveis booleanas, `tem_carteira` e `tem_carro`. Imprima o resultado de:
    - `tem_carteira and tem_carro` (Só pode dirigir se tiver carteira E carro).
    - `tem_carteira or tem_carro` (Pode se locomover se tiver carteira OU carro).
    - `not tem_carteira` (É verdade que não tem carteira?).
"""

tem_carteira = True
tem_carro = True
print(tem_carteira and tem_carro)

tem_carteira = True
tem_carro = False
print(tem_carteira or tem_carro)

tem_carteira = True
nao_tem_carteira = not tem_carteira
print("O resultado de not tem_carteira (com tem_carteira sendo True) é:", nao_tem_carteira)

tem_carteira = False
nao_tem_carteira = not tem_carteira
print("O resultado de not tem_carteira (com tem_carteira sendo False) é:", nao_tem_carteira)