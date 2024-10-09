import time, os, volume, massa, comprimento, digitar

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
        try:
            escolha = input("Digite sua escolha: ")
            os.system('cls')
        except ValueError:
            
            digitar.texto("Escolha inválida. Por favor, tente novamente.")
            
            time.sleep(1)         
        try:
            if escolha == "0":  # Sai do programa quando a escolha é 0
                os.system('cls')
                
                digitar.texto("Saindo do programa.")
                
                time.sleep(1)
                break

            if escolha == "1":
                digitar.texto("Digite o valor em metros: ")
                metros = float(input('> '))
                quilometros = comprimento.converte_m2km(metros)
                time.sleep(1) 
                os.system('cls')
                time.sleep(1) 
                
                digitar.texto(f"{metros} metros são {quilometros} quilômetros.")
                
                time.sleep(1)
                    
            elif escolha == "2":
                digitar.texto('Digite o valor em quilômetros:')
                quilometros = float(input("> "))
                metros = comprimento.converte_km2m(quilometros)
                time.sleep(1) 
                os.system('cls')
                time.sleep(1) 
                
                digitar.texto(f"{quilometros} quilômetros são {metros} metros.")
                
                time.sleep(1)

            elif escolha == "3":
                digitar.texto("Digite o valor em gramas: ")
                gramas = float(input('> '))
                quilogramas = massa.converte_g_para_Kg(gramas)
                time.sleep(1) 
                os.system('cls')
                time.sleep(1) 
                
                digitar.texto(f"{gramas} gramas são {quilogramas} quilogramas.")
                
                time.sleep(1)
                
            elif escolha == "4":
                digitar.texto("Digite o valor em quilogramas: ")
                quilogramas = float(input('> '))
                gramas = massa.converte_Kg_para_g(quilogramas)
                time.sleep(1) 
                os.system('cls')
                time.sleep(1) 
                
                digitar.texto(f"{quilogramas} quilogramas são {gramas} gramas.")
                
                time.sleep(1)

            elif escolha == "5":
                digitar.texto("Digite o valor em litros: ")
                litros = float(input('>'))
                mililitros = volume.volume_litros_para_mili(litros)
                time.sleep(1) 
                os.system('cls')
                time.sleep(1) 
                
                digitar.texto(f"{litros} litros são {mililitros} mililitros.")
                
                time.sleep(1)

            elif escolha == "6":
                digitar.texto("Digite o valor em mililitros: ")
                mililitros = float(input("> "))
                litros = volume.volume_mili_para_litros(mililitros)
                time.sleep(1) 
                os.system('cls')
                time.sleep(1) 
                
                digitar.texto(f"{mililitros} mililitros são {litros} litros.")
                
                time.sleep(1)

            else:
                time.sleep(1) 
                os.system('cls')
                
                digitar.texto("Escolha inválida. Por favor, tente novamente.")
                
                time.sleep(1)
                
        except ValueError:
            time.sleep(1)
            os.system('cls')
            
            digitar.texto("Escolha inválida. Por favor, tente novamente.")
            
            time.sleep(1)
#-------------------------------------------------------------
if __name__ == "__main__":  # Garante que se o módulo for importado não será executado
    main()  # Chamada da função principal
