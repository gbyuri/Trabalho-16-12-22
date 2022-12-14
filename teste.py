catalogo=['1..Bandana','2..Jaqueta','3..Camisa','4..Calça','5..Botas','6..Finalizar compra','7..Sair']
coresbandana=['1..Azul','2..Vermelho','3..Amarelo','4..Preto']
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
    print("""Bem Vindo à HARLEY BH MOTOCLUBE
    Produtos licenciados e exclusivos Harley Davidson
    Todos os produtos são confeccionados com as cores e estampas da marca Harley Davidson
    Segue em lista nossos produtos
    """)
    print(catalogo)
    print("Carrinho:",carrinho)
    menu=int(input("O que quer fazer hoje:"))
    match menu:
        case 1:
            print(catalogo[0])
        case 2:
            print(catalogo[1])

        case 3:
            while True:
                print(catalogo[2])
                print(tamanhocamisa)
                escolhacamisa=input("Diga qual o seu tamanho:")
                print(escolhacamisa)
                if escolhacamisa == "pp" or escolhacamisa == "p" or escolhacamisa == "m" or escolhacamisa == "g" or escolhacamisa == "gg":
                    break

            print(escolhacamisa)

            print("O preço da camisa é:R$",precocamisa)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não"))
            match comprar:
                case 1:
                    carrinho.append('Camisa '+escolhacamisa)
                    total=total+precocamisa
                    print(total)
        case 4:
            print(catalogo[3])

        case 5:
            print(catalogo[4])

        case 6:
            print(catalogo[5])

        case 7:
            print(catalogo[6])
            print("Obrigado por visitar nossa loja!!!")
            break