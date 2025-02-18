import matplotlib.pyplot as plt

# Definindo a matriz de confusão
matriz_confusao = [
    [40, 2, 1, 0, 0, 0, 0, 0, 0, 0],  # Classe C1
    [1, 35, 3, 0, 0, 0, 0, 0, 0, 0],  # Classe C2
    [0, 2, 30, 1, 0, 0, 0, 0, 0, 0],  # Classe C3
    [0, 0, 1, 25, 2, 0, 0, 0, 0, 0],  # Classe C4
    [0, 0, 0, 1, 20, 1, 0, 0, 0, 0],  # Classe C5
    [0, 0, 0, 0, 1, 18, 2, 0, 0, 0],  # Classe C6
    [0, 0, 0, 0, 0, 1, 15, 1, 0, 0],  # Classe C7
    [0, 0, 0, 0, 0, 0, 1, 12, 1, 0],  # Classe C8
    [0, 0, 0, 0, 0, 0, 0, 1, 10, 1],  # Classe C9
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 8]    # Classe C10
]

# Função para calcular a acurácia global
def calcular_acuracia_global(matriz_confusao):
    total_amostras = sum(sum(linha) for linha in matriz_confusao)
    vp_total = sum(matriz_confusao[i][i] for i in range(len(matriz_confusao)))
    return vp_total / total_amostras

# Função para calcular sensibilidade (recall) para uma classe
def calcular_sensibilidade(VP, FN):
    return VP / (VP + FN) if (VP + FN) > 0 else 0

# Função para calcular especificidade para uma classe
def calcular_especificidade(VN, FP):
    return VN / (VN + FP) if (VN + FP) > 0 else 0

# Função para calcular precisão para uma classe
def calcular_precisao(VP, FP):
    return VP / (VP + FP) if (VP + FP) > 0 else 0

# Função para calcular o F-score para uma classe
def calcular_f_score(precisao, recall):
    return 2 * (precisao * recall) / (precisao + recall) if (precisao + recall) > 0 else 0

# Calculando métricas para cada classe
num_classes = len(matriz_confusao)
metricas_por_classe = []

for i in range(num_classes):
    VP = matriz_confusao[i][i]  # Verdadeiros Positivos
    FN = sum(matriz_confusao[i]) - VP  # Falsos Negativos
    FP = sum(matriz_confusao[j][i] for j in range(num_classes)) - VP  # Falsos Positivos
    total_amostras = sum(sum(linha) for linha in matriz_confusao)  # Total de amostras na matriz
    VN = total_amostras - (VP + FN + FP)  # Verdadeiros Negativos
    
    sensibilidade = calcular_sensibilidade(VP, FN)
    especificidade = calcular_especificidade(VN, FP)
    precisao = calcular_precisao(VP, FP)
    f_score = calcular_f_score(precisao, sensibilidade)
    
    metricas_por_classe.append({
        "Classe": f"C{i+1}",
        "Sensibilidade": sensibilidade,
        "Especificidade": especificidade,
        "Precisão": precisao,
        "F-score": f_score
    })

# Calculando a acurácia global
acuracia_global = calcular_acuracia_global(matriz_confusao)

# Exibindo os resultados
print("Métricas por Classe:")
for metrica in metricas_por_classe:
    print(f"Classe {metrica['Classe']}:")
    print(f"  Sensibilidade (Recall): {metrica['Sensibilidade']:.2f}")
    print(f"  Especificidade: {metrica['Especificidade']:.2f}")
    print(f"  Precisão: {metrica['Precisão']:.2f}")
    print(f"  F-score: {metrica['F-score']:.2f}\n")

print(f"Acurácia Global: {acuracia_global:.2f}")

# Criando gráficos para visualizar as métricas
classes = [metrica["Classe"] for metrica in metricas_por_classe]
sensibilidades = [metrica["Sensibilidade"] for metrica in metricas_por_classe]
especificidades = [metrica["Especificidade"] for metrica in metricas_por_classe]
precisoes = [metrica["Precisão"] for metrica in metricas_por_classe]
f_scores = [metrica["F-score"] for metrica in metricas_por_classe]

# Gráfico de barras comparando as métricas por classe (reduzido em 50%)
x = range(len(classes))
width = 0.15

plt.figure(figsize=(7, 3.5))  # Reduzido de (14, 7) para (7, 3.5)

# Barras para Sensibilidade
plt.bar(x, sensibilidades, width, label="Sensibilidade", color="blue", alpha=0.7)

# Barras para Especificidade
plt.bar([p + width for p in x], especificidades, width, label="Especificidade", color="green", alpha=0.7)

# Barras para Precisão
plt.bar([p + 2 * width for p in x], precisoes, width, label="Precisão", color="orange", alpha=0.7)

# Barras para F-score
plt.bar([p + 3 * width for p in x], f_scores, width, label="F-score", color="purple", alpha=0.7)

# Configurações do gráfico
plt.xlabel("Classes")
plt.ylabel("Valor da Métrica")
plt.title("Comparação de Métricas por Classe")
plt.xticks([p + 1.5 * width for p in x], classes)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Mostrar o gráfico
plt.tight_layout()
plt.show()

# Gráfico de pizza para a acurácia global (reduzido em 50%)
plt.figure(figsize=(3, 3))  # Reduzido de (6, 6) para (3, 3)
labels = ["Acurácia Global", "Erro Global"]
sizes = [acuracia_global, 1 - acuracia_global]
colors = ["lightgreen", "lightcoral"]
explode = (0.1, 0)  # Destacar a fatia da acurácia

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
plt.title("Acurácia Global")
plt.axis("equal")  # Para garantir que o gráfico seja um círculo

# Mostrar o gráfico
plt.tight_layout()
plt.show()
