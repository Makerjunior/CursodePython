Aqui está a documentação para o código fornecido. A documentação explica as classes, seus métodos e atributos, e como utilizá-los:

---

# Documentação do Código

## Classes e Métodos

### Classe `Carros`

A classe `Carros` é uma classe base que representa um carro genérico. Ela armazena informações básicas sobre um carro e oferece métodos para manipular e acessar essas informações.

#### Atributos

- `__marca` (str): Marca do carro.
- `__modelo` (str): Modelo do carro.
- `__ano` (int): Ano de fabricação do carro.

#### Métodos

- `__init__(self, marca, modelo, ano)`: Construtor que inicializa um novo objeto `Carros` com marca, modelo e ano.

- `definir_informacoes(self, marca, modelo, ano)`: Atualiza a marca, modelo e ano do carro.

- `mostrar_informacoes(self)`: Imprime as informações básicas do carro, incluindo marca, modelo e ano.

- `get_marca(self)`: Retorna a marca do carro.

- `set_marca(self, marca)`: Define a marca do carro.

- `get_modelo(self)`: Retorna o modelo do carro.

- `set_modelo(self, modelo)`: Define o modelo do carro.

- `get_ano(self)`: Retorna o ano do carro.

- `set_ano(self, ano)`: Define o ano do carro.

### Classe `CarroEsportivo`

A classe `CarroEsportivo` é uma subclasse de `Carros` que representa um carro esportivo, adicionando informações específicas e funcionalidades adicionais.

#### Atributos

- `__velocidade_maxima` (int): Velocidade máxima do carro esportivo em km/h.
- `__potencia` (int): Potência do carro esportivo em CV (cavalos-vapor).
- `__ligado` (bool): Estado do carro esportivo (ligado ou desligado). Inicialmente definido como `False`.

#### Métodos

- `__init__(self, marca, modelo, ano, velocidade_maxima, potencia)`: Construtor que inicializa um novo objeto `CarroEsportivo` com marca, modelo, ano, velocidade máxima e potência.

- `definir_informacoes(self, marca, modelo, ano, velocidade_maxima, potencia)`: Atualiza as informações do carro esportivo, incluindo marca, modelo, ano, velocidade máxima e potência.

- `mostrar_informacoes(self)`: Imprime as informações completas do carro esportivo, incluindo marca, modelo, ano, velocidade máxima, potência e estado (ligado ou desligado).

- `ligar(self)`: Liga o carro esportivo, alterando o estado para `ligado`. Exibe uma mensagem indicando que o carro está ligado.

- `desligar(self)`: Desliga o carro esportivo, alterando o estado para `desligado`. Exibe uma mensagem indicando que o carro está desligado.

- `get_velocidade_maxima(self)`: Retorna a velocidade máxima do carro esportivo.

- `set_velocidade_maxima(self, velocidade_maxima)`: Define a velocidade máxima do carro esportivo.

- `get_potencia(self)`: Retorna a potência do carro esportivo.

- `set_potencia(self, potencia)`: Define a potência do carro esportivo.

## Exemplo de Uso

```python
# Criando um carro esportivo
carro_esportivo = CarroEsportivo("Ferrari", "488 Spider", 2021, 330, 670)

# Usando os métodos específicos do carro esportivo
carro_esportivo.ligar()
carro_esportivo.mostrar_informacoes()

print('----------------------------------')

# Atualizando informações
carro_esportivo.definir_informacoes("Porsche", "911 Turbo", 2022, 320, 650)
carro_esportivo.desligar()
carro_esportivo.mostrar_informacoes()
```

### Explicação do Exemplo

1. **Criação do Objeto**:
   - Um objeto `CarroEsportivo` é criado com a marca "Ferrari", modelo "488 Spider", ano 2021, velocidade máxima de 330 km/h e potência de 670 CV.

2. **Métodos Utilizados**:
   - `ligar()`: Liga o carro e imprime uma mensagem confirmando o estado ligado.
   - `mostrar_informacoes()`: Exibe todas as informações do carro esportivo, incluindo velocidade máxima, potência e estado atual.
   - `definir_informacoes()`: Atualiza as informações do carro para um novo modelo e características.
   - `desligar()`: Desliga o carro e imprime uma mensagem confirmando o estado desligado.

---

Esta documentação cobre a estrutura e o uso das classes e métodos, além de fornecer um exemplo prático de como utilizar as funcionalidades implementadas no código.