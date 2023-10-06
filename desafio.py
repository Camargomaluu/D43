#Faça um programa para calcular o IMC (Índice de Massa Corporal). Para fazer esse cálculo, você vai precisar usar a fórmula abaixo: IMC = Peso / (Altura * Altura) Depois de obter o resultado, você precisa classificar o usuário em uma das cinco categorias do IMC.

variavel = ""

p = float(input("Para calcular o seu Índice de Massa Corporal, digite o seu peso em kilos: "))
a = float(input("Agora, digite a sua altura em metros: "))

imc = p / (a*a)

if (imc < 18.5):
    print("Classificado como magreza, está abaixo do peso!")

elif (imc < 25):
    print ("Classificado Peso Normal!")

elif (imc <30):
    print ("Classificado como Sobrepeso!")

elif (imc <40):
    print ("Classificado como Obesidade!")

else:
    print ("Classificado como Obesidade Grave!")                    