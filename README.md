# 🧮 Matriz de Confusão - Avaliação de Modelos de Classificação 📊
Este projeto tem como objetivo calcular e visualizar as principais métricas de avaliação para modelos de classificação multiclasse usando uma matriz de confusão . As métricas incluem Sensibilidade (Recall) , Especificidade , Precisão , F-score e Acurácia Global , além de gráficos para facilitar a interpretação dos resultados.
## 📋 Índice
- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Requisitos](#-requisitos)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Resultados Esperados](#-resultados-esperados)
- [Contribuições](#-contribuições)
- [Licença](#-licença)
- [Reconhecimentos](#-reconhecimentos)
- [Links Úteis](#-links-úteis)

## 🌟 Visão Geral
O objetivo deste projeto é avaliar o desempenho de um modelo de classificação multiclasse usando uma matriz de confusão arbitrária . A matriz de confusão é uma ferramenta essencial para entender onde o modelo acerta ou erra, permitindo identificar classes com desempenho inferior ou superior.

As métricas calculadas são úteis para:

- **Avaliar o desempenho global**: Medir a acurácia geral do modelo.
- **Identificar classes problemáticas**: Detectar classes com baixa sensibilidade ou precisão.
- **Tomar decisões informadas**: Melhorar o modelo ajustando os parâmetros ou tratando classes desbalanceadas.

Além disso, os gráficos gerados permitem uma visualização clara das métricas por classe e da acurácia global.


## 🔧 Funcionalidades

### Cálculo de Métricas Individuais:
- **Sensibilidade (Recall)**: Proporção de amostras positivas corretamente identificadas.
- **Especificidade**: Proporção de amostras negativas corretamente identificadas.
- **Precisão**: Proporção de previsões positivas corretas.
- **F-score**: Combinação harmônica entre precisão e recall.
- **Acurácia Global**: Proporção de previsões corretas em relação ao total de amostras.

### Visualização de Gráficos:
- Gráfico de barras comparando métricas por classe.
- Gráfico de pizza mostrando a proporção da acurácia global.

### Matriz de Confusão Arbitrária:
- Permite testar diferentes cenários de classificação multiclasse.


## 💻 Requisitos
Para executar este projeto, você precisará de:

- **Python 3.7+**: Requisito mínimo para execução do projeto.
- **Matplotlib**: Biblioteca para geração de gráficos.
- **NumPy (opcional)**: Para manipulação eficiente de matrizes.

Instale as dependências com o seguinte comando:
`pip install matplotlib numpy`
## 🔧 Instalação
**1- Clone o Repositório** :
Clone este repositório para o seu ambiente local com o comando:
`git clone https://github.com/seu-usuario/matriz-confusao.git
`
`cd matriz-confusao`
**2- Instale as Dependências** :
Dentro do diretório do projeto, instale as dependências usando o pip:
`pip install -r requirements.txt`
## 🚀 Uso
Após configurar o ambiente e as dependências, você pode executar o script principal para calcular as métricas e gerar os gráficos. Basta rodar o seguinte comando:
`python main.py`
Após a execução, os resultados serão exibidos no terminal e os gráficos serão gerados automaticamente.
## 📂 Estrutura do Projeto
Aqui está a estrutura de diretórios e arquivos do projeto:

```matriz-confusao/
├── main.py                     # Código principal que calcula as métricas e gera os gráficos
├── README.md                   # Este arquivo
├── requirements.txt            # Lista de dependências
└── output/                     # Pasta para armazenar os gráficos gerados (opcional)
    ├── grafico_barras.png      # Gráfico de barras comparando métricas por classe
    └── grafico_pizza.png       # Gráfico de pizza mostrando a acurácia global
```

## 📈 Resultados Esperados
Após a execução do script, você obterá os seguintes resultados:

1. **Métricas por Classe**:
   - Sensibilidade (Recall), Especificidade, Precisão e F-score para cada classe.
   - Exemplo:
     - **Classe C1**:
       - Sensibilidade: 0.93
       - Especificidade: 0.98
       - Precisão: 0.95
       - F-score: 0.94

2. **Acurácia Global**:
   - Exemplo:
     - Acurácia Global: 85.0%

3. **Gráficos**:
   - **Gráfico de Barras**: Compara as métricas (Sensibilidade, Especificidade, Precisão e F-score) para cada classe.
   - **Gráfico de Pizza**: Mostra a proporção da acurácia global em relação ao erro global.

Exemplo de Visualização:

- Gráfico de Barras
- Gráfico de Pizza

## 🤝 Contribuições
Contribuições são bem-vindas! Para contribuir com o projeto, siga estas etapas:

Faça um fork deste repositório.
Crie uma branch para sua contribuição:
`git checkout -b feature/nova-funcionalidade`
Envie um pull request detalhando suas alterações.
## 📜 Licença
Este projeto está licenciado sob a MIT License . Consulte o arquivo LICENSE para mais detalhes.

## 🙏 Reconhecimentos
- **Matplotlib**: Pela excelente biblioteca de visualização de gráficos.
- **NumPy**: Pela eficiência em operações matriciais.
- **Python**: Pela simplicidade e versatilidade na implementação.

## 🌐 Links Úteis
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) - Documentação oficial do Matplotlib, biblioteca para visualização de gráficos.
- [NumPy Documentation](https://numpy.org/doc/) - Documentação oficial do NumPy, biblioteca para operações matemáticas e manipulação de arrays.
- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) - Ferramentas adicionais para cálculo de métricas de avaliação.
