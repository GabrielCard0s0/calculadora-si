import time, os, volume, massa, comprimento

def main():
    """
    Função principal do programa.
    """
    while True:  # Laço infinito
        print("#######################################################")
        print("## CALCULADORA DO SISTEMAS INTERNACIONAL DE UNIDADES ##")
        print("#######################################################")
        print("\nEscolha uma conversão:")
        options = [
            "1. Comprimento (m para km)",
            "2. Comprimento (km para m)",
            "3. Massa (g para kg)",
            "4. Massa (kg para g)",
            "5. Volume (l para ml)",
            "6. Volume (ml para l)",
            "0. Sair"

        ]
        for option in options:
            print(option)
        
        escolha = input("Digite sua escolha: ")
        os.system('cls')

        if escolha == "0":  # Sai do programa quando a escolha é 0
            print('-'*50)
            print("Saindo do programa.")
            print('-'*50)
            time.sleep(1)
            break

        if escolha == "1":
            metros = float(input("Digite o valor em metros: "))
            quilometros = comprimento.converte_m2km(metros)
            print('-'*50)
            print(f"{metros} metros são {quilometros} quilômetros.")
            print('-'*50)
                
        elif escolha == "2":
            quilometros = float(input("Digite o valor em quilômetros: "))
            metros = comprimento.converte_km2m(quilometros)
            print('-'*50)
            print(f"{quilometros} quilômetros são {metros} metros.")
            print('-'*50)

        elif escolha == "3":
            gramas = float(input("Digite o valor em gramas: "))
            quilogramas = massa.converte_g_para_Kg(gramas)
            print('-'*50)
            print(f"{gramas} gramas são {quilogramas} quilogramas.")
            print('-'*50)
            
        elif escolha == "4":
            quilogramas = float(input("Digite o valor em quilogramas: "))
            gramas = massa.converte_Kg_para_g(quilogramas)
            print('-'*50)
            print(f"{quilogramas} quilogramas são {gramas} gramas.")
            print('-'*50)

        elif escolha == "5":
            litros = float(input("Digite o valor em litros: "))
            mililitros = volume.volume_litros_para_mili(litros)
            print('-'*50)
            print(f"{litros} litros são {mililitros} mililitros.")
            print('-'*50)

        elif escolha == "6":
            mililitros = float(input("Digite o valor em mililitros: "))
            litros = volume.volume_mili_para_litros(mililitros)
            print('-'*50)
            print(f"{mililitros} mililitros são {litros} litros.")
            print('-'*50)

        else:
            print('-'*50)
            print("Escolha inválida. Por favor, tente novamente.")
            print('-'*50)
            time.sleep(1)
#-------------------------------------------------------------
if __name__ == "__main__":  # Garante que se o módulo for importado não será executado
    main()  # Chamada da função principal
