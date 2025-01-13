O que é a Padronização (Standardization)?
A padronização é uma técnica de pré-processamento que transforma os dados para que cada feature (atributo) tenha uma média igual a 0 e um desvio padrão igual a 1.

A fórmula para padronizar uma feature 
𝑥
x é:

𝑧
=
𝑥
−
𝜇
𝜎
z= 
σ
x−μ
​
 
Onde:

𝜇
μ: Média dos valores da feature.
𝜎
σ: Desvio padrão dos valores da feature.
𝑧
z: Valor padronizado.
Após a padronização, os valores estarão em uma escala comum, centrados em 0 e variando com base no desvio padrão.

Por que a padronização ajuda na função de custo?
A padronização impacta diretamente no processo de otimização do modelo, influenciando como a função de custo é minimizada. Vamos explorar as razões:

1. Escalas uniformes para as features
Em conjuntos de dados, as features podem ter escalas muito diferentes. Por exemplo:
Idade: 
0
−
100
0−100
Renda anual: 
10.000
−
1.000.000
10.000−1.000.000
Quando as escalas são muito diferentes, os pesos (
𝑤
w) associados a cada feature também precisam se ajustar para compensar essas diferenças, tornando o processo de treinamento mais difícil.
A padronização garante que todas as features estejam na mesma escala, evitando que uma feature com valores maiores domine o cálculo da função de custo.
2. Melhor comportamento da descida do gradiente
A descida do gradiente depende dos gradientes das features para atualizar os pesos. Se uma feature tem valores muito maiores que as outras, os gradientes também serão desbalanceados.
Isso pode causar oscilações ou passos muito pequenos na direção da otimização, tornando o processo mais lento ou instável.
Com a padronização, os gradientes têm magnitudes mais uniformes, permitindo que a descida do gradiente converja de forma mais eficiente.
3. Forma da função de custo
A função de custo (como o erro quadrático médio, MSE) é mais fácil de otimizar quando os dados estão padronizados.
Sem padronização, a função de custo pode ter o formato de um vale inclinado (com curvas acentuadas em algumas direções e suaves em outras). Isso é chamado de vale em forma de elipse.
Com padronização, a função de custo assume uma forma mais esférica, facilitando os passos consistentes na descida do gradiente.
4. Evita dependência excessiva na taxa de aprendizado
Com dados não padronizados, a escolha de uma boa taxa de aprendizado (
𝜂
η) pode ser muito difícil, porque os gradientes podem variar muito em magnitude.
Padronizar os dados reduz essa variação, permitindo que o modelo funcione bem com uma taxa de aprendizado mais consistente.
Exemplos práticos:
Antes da padronização:

Idade: 
[
20
,
30
,
40
,
50
]
[20,30,40,50]
Renda anual: 
[
20000
,
30000
,
40000
,
50000
]
[20000,30000,40000,50000]
A feature "Renda" domina a otimização porque tem valores maiores.
Depois da padronização:

Idade (padronizada): 
[
−
1.34
,
−
0.67
,
0.67
,
1.34
]
[−1.34,−0.67,0.67,1.34]
Renda (padronizada): 
[
−
1.34
,
−
0.67
,
0.67
,
1.34
]
[−1.34,−0.67,0.67,1.34]
Agora ambas as features contribuem de forma equilibrada na função de custo.