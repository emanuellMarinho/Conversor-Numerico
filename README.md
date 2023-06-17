# Conversão entre Bases

Este código implementa uma classe chamada `Base`, que permite realizar conversões entre bases numéricas, incluindo binário, octal e hexadecimal.

A classe `Base` possui os seguintes métodos:

## Método `__init__()`

O método `__init__()` é o construtor da classe `Base` e é chamado automaticamente quando um objeto da classe é criado. Neste caso, ele chama o método `select_conversion()`, que inicia o processo de seleção da conversão.

## Métodos de Conversão

Os seguintes métodos são responsáveis por realizar as conversões entre bases:

### Método `convert_bin()`

Este método converte um número decimal para binário. Solicita ao usuário que digite o número decimal a ser convertido e, em seguida, realiza a conversão passo a passo. Utiliza o algoritmo de divisão sucessiva por 2 para obter os dígitos binários e construir a representação binária do número.

### Método `convert_octal()`

Este método converte um número decimal para octal. Solicita ao usuário que digite o número decimal a ser convertido e, em seguida, realiza a conversão passo a passo. Utiliza o algoritmo de divisão sucessiva por 8 para obter os dígitos octais e construir a representação octal do número.

### Método `convert_hex()`

Este método converte um número decimal para hexadecimal. Solicita ao usuário que digite o número decimal a ser convertido e, em seguida, realiza a conversão passo a passo. Utiliza o algoritmo de divisão sucessiva por 16 para obter os dígitos hexadecimais e construir a representação hexadecimal do número. Utiliza os dígitos hexadecimais de 0 a F para representar os restos da divisão.

## Método `select_conversion()`

Este método inicia o processo de seleção da conversão. Solicita ao usuário que escolha uma das bases disponíveis: binário, octal ou hexadecimal. Em seguida, verifica a opção escolhida e chama o método correspondente para realizar a conversão. Caso a opção seja inválida, exibe uma mensagem de erro.

O processo de seleção é realizado em um loop `while True`, permitindo que o usuário faça várias conversões consecutivas até optar por sair.

---

Esta implementação foi uma atividade de iniciativa própria em virtude da matéria de "Matemática Computacional/Discreta" da faculdade UNINTER. O objetivo foi compreender na prática como o computador realiza a compilação do algoritmo, aplicando os conceitos de conversão entre bases numéricas.

Através desse código, foi possível exercitar a lógica de programação e compreender os algoritmos de conversão entre bases, aprimorando o conhecimento sobre o funcionamento interno do computador.

Espera-se que essa atividade tenha contribuído para a compreensão dos conceitos abordados na disciplina, proporcionando uma aplicação prática dos mesmos.