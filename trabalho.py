catalogo=['1..Bandana','2..Jaqueta','3..Camisa','4..Calça','5..Botas','6..Finalizar compra','7..Sair']
coresbandana=['AZUL','VERMELHA','AMARELA','PRETA']
precobandana=24.9
tamanhojaqueta=['PP','P','M','G','GG']
precojaqueta=249.9
tamanhocamisa=['PP','P','M','G','GG']
precocamisa=49.9
tamanhocalca=['36','38','40','42','44','46','48']
precocalca=99.9
tamanhobota=['36~37','38~39','40~41','42~43','44~45','46~47']
precobota=149.9
carrinho=[]
total=0
escolhacamisa="nada"
while True:
    aux=False
    print("""Bem Vindo à HARLEY BH MOTOCLUBE
    Produtos licenciados e exclusivos Harley Davidson
    Todos os produtos são confeccionados com as cores e estampas da marca Harley Davidson
    Segue em lista nossos produtos
    """)
    print(catalogo)
    for i in range(len(carrinho)):
        print("Carrinho:<",i,">",carrinho[i])
    menu=int(input("O que quer fazer hoje:"))
    match menu:
        case 1:
            while True:
                print(catalogo[0])
                print(coresbandana)
                escolhabandana=input("Diga qual cor você quer:")
                for i in range(len(coresbandana)):
                    estoquebandana=coresbandana[i]
                    print(estoquebandana)
                    if estoquebandana==escolhabandana.upper():
                        aux=True
                if aux==True:
                    break
            print(escolhabandana)
            print("O preço da bandana é:R$",precobandana)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não"))
            match comprar:
                case 1:
                    carrinho.append('Bandana '+escolhabandana.upper())
                    total=total+precobandana
                    print(total)  
        case 2:
            while True:
                print(catalogo[1])
                print(tamanhojaqueta)
                escolhajaqueta=input("Diga qual o seu tamanho:")
                for i in range(len(tamanhojaqueta)):
                    estoquejaqueta=tamanhojaqueta[i]
                    if estoquejaqueta == escolhajaqueta.upper():
                        aux=True
                    
                if aux==True:
                    break
            print(escolhajaqueta)
            print("O preço da jaqueta é:R$",precojaqueta)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não"))
            match comprar:
                case 1:
                    carrinho.append('Jaqueta '+escolhajaqueta.upper())
                    total=total+precojaqueta
                    print(total)
        case 3:
            while True:
                print(catalogo[2])
                print(tamanhocamisa)
                escolhacamisa=input("Diga qual o seu tamanho:")
                print(escolhacamisa.upper())
                for i in range(len(tamanhocamisa)):
                    estoquecamisa=tamanhocamisa[i]
                    if estoquecamisa==escolhacamisa.upper():
                        aux=True
                if aux==True:
                    break
            print(escolhacamisa.upper())
            print("O preço da camisa é:R$",precocamisa)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não"))
            match comprar:
                case 1:
                    carrinho.append('Camisa '+escolhacamisa.upper())
                    total=total+precocamisa
                    print(total)
        case 4:
            print(catalogo[3])
            print(tamanhocalca)
            escolhacalca=input("Diga qual o seu tamanho:")
            print(escolhacalca.upper())
            for i in range(len(tamanhocalca)):
                estoquecalca=tamanhocalca[i]
                if estoquecalca==escolhacalca.upper():
                    aux=True
            if aux==True:
                break
            print(escolhacalca.upper())
            print("O preço a calça é:R$",precocalca)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não"))
            match comprar:
                case 1:
                    carrinho.append('Calça '+escolhacalca.upper())
                    total=total+precocalca
                    print(total)
        case 5:
            print(catalogo[4])

        case 6:
            print(catalogo[5])

        case 7:
            print(catalogo[6])
            print("Obrigado por visitar nossa loja!!!")
            break
