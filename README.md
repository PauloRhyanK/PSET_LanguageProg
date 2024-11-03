# PSET
Esse é um PSET passado pelo professor Abrantes Araujo Silva Filho na matéria de linguagem de programação do curso de ciência da computação, ela é inspirada em uma atividade da disciplina MIT6.009:Fundamentals of Programming.


## Resposta para as questões do PSET

#### Questão 1: Se você passar essa imagem pelo filtro de inversão, qual seria o output esperado? Justifique sua resposta.
- largura: 4
- altura: 1
- pixels: [29,89,136,200]

ESPERADO:
- largura: 4
- altura: 1
- pixels: [229,166,119,55]

Para a imagem ser invertida em um filtro de inversão, é necessário subtrair o valor de cada pixel de 255.
Portanto, o pixel [29,89,136,200] se tornaria [229,166,119,55].

#### Questão 2: faça a depuração e, quando terminar, seu código deve conseguir passar em todos os testes do grupo de teste TestInvertida (incluindo especificamente o que você acabou de criar). Execute seu filtro de inversão na imagem test_images/bluegill.png, salve o resultado como uma imagem PNG e salve a imagem.


