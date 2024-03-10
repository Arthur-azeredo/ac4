def lernotas():
    ap1 = float(input("Insira a nota da AP1: "))
    if ap1 < 0 or ap1 > 10:
        print("Nota inválida. Encerrando o programa.")
        return None

    ap2 = float(input("Insira a nota da AP2: "))
    if ap2 < 0 or ap2 > 10:
        print("Nota inválida. Encerrando o programa.")
        return None

    avaliacaosub = float(input("Insira a nota da AS: "))
    if  avaliacaosub < 0 or  avaliacaosub > 10:
        print("Nota inválida. Encerrando o programa.") 
        return None

    ac = float(input("Insira a nota da AC: "))
    if ac < 0 or ac > 10:
        print("Nota inválida. Encerrando o programa.")
        return None

    return ap1, ap2,  avaliacaosub, ac 

def calcular_media(ap1, ap2,  avaliacaosub, ac):
    menorap = min(ap1, ap2)
    return (menorap +  avaliacaosub) * 0.4 + ac * 0.2

def main_():
    nome = input("Insira seu nome: ")
    if not nome:
        print("Nome inválido. Encerrando o programa.")
        return

    notas = lernotas()
    if notas is None:
        return

    media = calcular_media(*notas) 
    if media >= 7.0:
        print(f"Parabéns, {nome}! Sua média final é {media:.2f}. Você foi aprovado!")
    else:
        print(f"{nome}, sua média final é {media:.2f}. Infelizmente, você foi reprovado.")

if __name__ == "__main__": 
    main_() 