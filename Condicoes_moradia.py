print("Condições de Moradia")
print("Autor: Bruno Fritsch")

# Variáveis de controle
total_familias = 0
total_pessoas = 0

pessoas_municipios = 0
pessoas_berger = 0
pessoas_reunidas = 0

soma_renda_reunidas = 0
quantidade_reunidas = 0

quantidade_pai_3_grau = 0
quantidade_sem_esgoto = 0
quantidade_apartamentos_berger = 0

# Entrada inicial
renda_familiar = float(input("Digite a renda familiar (-1 para encerrar): "))

while renda_familiar != -1:

    bairro = input("Digite o bairro (Municipios/Berger/Reunidas): ")
    tipo_residencia = input("Digite o tipo de residência (Casa/Apartamento): ")
    numero_pessoas = int(input("Digite o número de pessoas da família: "))
    escolaridade_pai = int(input("Digite a escolaridade do pai (1/2/3): "))
    possui_esgoto = input("Possui esgoto? (S/N): ").upper()

    # Total de famílias e pessoas
    total_familias = total_familias + 1
    total_pessoas = total_pessoas + numero_pessoas

    # Bairro Municípios
    if bairro == "Municipios":
        pessoas_municipios = pessoas_municipios + numero_pessoas

    # Bairro Berger
    if bairro == "Berger":
        pessoas_berger = pessoas_berger + numero_pessoas

        if tipo_residencia == "Apartamento":
            quantidade_apartamentos_berger = quantidade_apartamentos_berger + 1

    # Bairro Reunidas
    if bairro == "Reunidas":
        pessoas_reunidas = pessoas_reunidas + numero_pessoas
        soma_renda_reunidas = soma_renda_reunidas + renda_familiar
        quantidade_reunidas = quantidade_reunidas + 1

    # Escolaridade do pai
    if escolaridade_pai == 3:
        quantidade_pai_3_grau = quantidade_pai_3_grau + 1

    # Possui esgoto
    if possui_esgoto == "N":
        quantidade_sem_esgoto = quantidade_sem_esgoto + 1

    # Nova entrada
    renda_familiar = float(input("\nDigite a renda familiar (-1 para encerrar): "))

# Cálculos

if quantidade_reunidas > 0:
    media_renda_reunidas = soma_renda_reunidas / quantidade_reunidas
else:
    media_renda_reunidas = 0

if total_familias > 0:
    media_pessoas_familia = total_pessoas / total_familias
    percentual_pai_3_grau = (quantidade_pai_3_grau / total_familias) * 100
    percentual_sem_esgoto = (quantidade_sem_esgoto / total_familias) * 100
else:
    media_pessoas_familia = 0
    percentual_pai_3_grau = 0
    percentual_sem_esgoto = 0

# Bairro mais populoso

if pessoas_municipios > pessoas_berger:
    if pessoas_municipios > pessoas_reunidas:
        bairro_mais_populoso = "Municipios"
    else:
        bairro_mais_populoso = "Reunidas"
else:
    if pessoas_berger > pessoas_reunidas:
        bairro_mais_populoso = "Berger"
    else:
        bairro_mais_populoso = "Reunidas"

# Resultados

print("\n========== RESULTADOS ==========")
print(f"Bairro mais populoso: {bairro_mais_populoso}")
print(f"Média de renda no bairro Reunidas: R$ {media_renda_reunidas:.2f}")
print(f"Percentual de pais com 3º grau: {percentual_pai_3_grau:.2f}%")
print(f"Média de pessoas por família: {media_pessoas_familia:.2f}")
print(f"Percentual de famílias sem esgoto: {percentual_sem_esgoto:.2f}%")
print(f"Quantidade de apartamentos no bairro Berger: {quantidade_apartamentos_berger}")