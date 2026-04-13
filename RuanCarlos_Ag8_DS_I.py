n = 1

nota_excelente = 0
nota_ruim = 0

for n in range(50):
    nome = input("Registre seu nome: ")
    idade = float(input("Registre sua idade: "))
    opiniao = input("""Qual nota você daria para o atendimento?
    (Escolhendo entre 1 - EXCELENTE, 2 - BOM e 3 - RUIM)
    """)
    
    nota = {
        "1": ("Excelente"),
        "2": ("Bom"),
        "3": ("Ruim")
    }
    
    if opiniao == "1":
        nota_excelente += 1
    elif opiniao == "3":
        nota_ruim += 1
    else: pass

    if opiniao in nota:
        print(f"""RESULTADO:
        
        NOME: {nome}
        IDADE: {idade:.0f}
        NOTA: {nota[opiniao]}""")
        
        print()
        print("Recomeçando questionário...")
        print()

    
    else:
        print(f"""RESULTADO:
          
        NOME: {nome}
        IDADE: {idade:.0f}
        NOTA: Nula""")
        
        print()
        print("Recomeçando questionário...")
        print()

print("RESULTADO DO QUESTIONÁRIO:")

print(f"""Notas excelentes: {nota_excelente}
Notas ruins: {nota_ruim}""")

print()
input("Pressione Enter para fechar...")