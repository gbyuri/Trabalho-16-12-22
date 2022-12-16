import os
from random import randint
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
    os.system("cls")
    print("""Bem Vindo à HARLEY BH MOTOCLUBE
Produtos licenciados e exclusivos Harley Davidson
Todos os produtos são confeccionados com as cores e estampas da marca Harley Davidson
Segue em lista nossos produtos""")
    print(catalogo)
    for i in range(len(carrinho)):
        print("Carrinho:<",i,">",carrinho[i])
    menu=int(input("O que quer fazer hoje:\n"))
    match menu:
        case 1:
            while True:
                print(catalogo[0])
                print(coresbandana)
                escolhabandana=input("Diga qual cor você quer:\n")
                for i in range(len(coresbandana)):
                    estoquebandana=coresbandana[i]
                    if estoquebandana==escolhabandana.upper():
                        aux=True
                if aux==True:
                    break
            print("O preço da bandana é:R$",precobandana)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não\n"))
            match comprar:
                case 1:
                    carrinho.append('Bandana '+escolhabandana.upper()+' R$'+str(precobandana))
                    total=total+precobandana
        case 2:
            while True:
                print(catalogo[1])
                print(tamanhojaqueta)
                escolhajaqueta=input("Diga qual o seu tamanho:\n")
                for i in range(len(tamanhojaqueta)):
                    estoquejaqueta=tamanhojaqueta[i]
                    if estoquejaqueta == escolhajaqueta.upper():
                        aux=True
                if aux==True:
                    break
            print("O preço da jaqueta é:R$",precojaqueta)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não\n"))
            match comprar:
                case 1:
                    carrinho.append('Jaqueta '+escolhajaqueta.upper()+' R$'+str(precojaqueta))
                    total=total+precojaqueta
        case 3:
            while True:
                print(catalogo[2])
                print(tamanhocamisa)
                escolhacamisa=input("Diga qual o seu tamanho:\n")
                for i in range(len(tamanhocamisa)):
                    estoquecamisa=tamanhocamisa[i]
                    if estoquecamisa==escolhacamisa.upper():
                        aux=True
                if aux==True:
                    break
            print("O preço da camisa é:R$",precocamisa)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não\n"))
            match comprar:
                case 1:
                    carrinho.append('Camisa '+escolhacamisa.upper()+' R$'+str(precocamisa))
                    total=total+precocamisa
        case 4:
            while True:
                print(catalogo[3])
                print(tamanhocalca)
                escolhacalca=input("Diga qual o seu tamanho:\n")
                for i in range(len(tamanhocalca)):
                    estoquecalca=tamanhocalca[i]
                    if estoquecalca==escolhacalca:
                        aux=True
                if aux==True:
                    break
            print("O preço a calça é:R$",precocalca)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não\n"))
            match comprar:
                case 1:
                    carrinho.append('Calça '+escolhacalca+' R$'+str(precocalca))
                    total=total+precocalca
        case 5:
            while True:
                print(catalogo[4])
                print(tamanhobota)
                escolhabota=input("Diga qual o seu tamanho:\n")
                for i in range(len(tamanhobota)):
                    estoquebota=tamanhobota[i]
                    if estoquebota==escolhabota:
                        aux=True
                if aux==True:
                    break
            print(escolhabota)
            print("O preço da bota é:R$",precobota)
            comprar=int(input("Gostaria de comprar? <1>Sim <2> Não\n"))
            match comprar:
                case 1:
                    carrinho.append('bota '+escolhabota+' R$'+str(precobota))
                    total=total+precobota
        case 6:
            while True:
                print(catalogo[5])
                for i in range(len(carrinho)):
                    print("Carrinho:<",i,">",carrinho[i])
                print("O total da sua compra é:R$"+str(total))
                print("""Estamos trabalho com cartão de crédito e dinheiro
Pagamentos no dinheiro tem desconto de 10%
Pagamentos no cartão de crédito e avista tem desconto de 5%
Pagamentos no cartão de crédito parcelado tem acrescimo de 1,5% por parcela""")
                pagamento=int(input("Como deseja pagar?\n1..Cartão\n2..Dinheiro\n"))
                if pagamento==1:
                    parcelas=int(input("Diga o número de parcelas:"))
                    if pagamento==1 and parcelas==1:
                        print("O seu total é:R$"+str(total)+"\nCom o desconto de 5%:R$"+str(total-(total*(5/100))))
                        confirmar=input("Confirmar? <SIM> <NÂO>")
                        confirmar=confirmar.upper()
                        if confirmar=="SIM":
                                    aux=True
                    elif pagamento==1 and parcelas > 1:
                        totalparcelado=(total/parcelas)+(totalparcelado*(1.5/100))
                        total=totalparcelado*parcelas
                        print("Cada parcela saira por:R$"+totalparcelado)
                        print("E o total final ficará em:R$"+total)
                        confirmar=input("Confirmar? <SIM> <NÂO>")
                        confirmar=confirmar.upper()
                        if confirmar=="SIM":
                                aux=True
                    else:
                        print("O seu total é:R$"+str(total)+"\nCom o desconto de 10%:R$"+str(total-(total*(10/100))))
                        confirmar=input("Confirmar? <SIM> <NÂO>")
                        confirmar=confirmar.upper()
                        if confirmar=="SIM":
                            aux=True     
                if aux==True:
                    sorteio=randint(1,10)
                    print(sorteio)
                    print("Como promoção pela inauguração da loja, temos uma brincadeira:\nAdvinhe o número de 1 a 10 e ganhe um prêmio!")
                    chute=int(input("Diga um número para tentar a sorte:"))
                    if chute==sorteio:
                        print("Parabéns, você ganhou uma camisa exclusiva da loja!!!")
                    else:
                        print("Que pena, você não acertou!")
                    break
            print("Obrigado por comprar conosco e volte sempre")
            break              
        case 7:
            print(catalogo[6])
            print("Obrigado por visitar nossa loja!!!")
            break
