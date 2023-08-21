""" Os nomes de arquivo do sistema Unix/Linux diferenciam maiúsculas
 de minúsculas. Os sistemas Windows armazenam as maiúsculas e minúsculas
das letras usadas no nome do arquivo, mas não fazem nenhuma distinção
entre as maiúsculas e minúsculas.

Dois separadores diferentes para os nomes dos diretórios:
\ no Windows e / no Unix/Linux """


# name = "/dir/file"

# name = "\dir\file"
# name = "\\dir\\file" # para não dar erro

""" O Python é inteligente o suficiente para converter barras em barras
 invertidas sempre que descobre que é exigido pelo sistema operacional"""


""" Qualquer programa escrito em Python (e não apenas em Python,
porque essa convenção se aplica a praticamente todas as linguagens
de programação) não se comunica diretamente com os arquivos, mas por meio
de algumas entidades abstratas que recebem nomes diferentes em linguagens
ou ambientes diferentes – os termos mais usados são handles ou streams"""


""" A operação de conectar o stream com um arquivo é chamada de abrir o arquivo,
 enquanto desconectar esse link é chamada de fechar o arquivo."""


""" A abertura do stream pode falhar, e isso pode acontecer por vários motivos:
- a falta de um arquivo com um nome especificado.
- o arquivo físico exista, mas o programa não tenha permissão para abri-lo.
- o programa ter aberto muitos streams e o sistema operacional
 específico não permitir a abertura simultânea de mais de n arquivos """


""" open mode """


""" Há duas operações básicas executadas no stream:

read: as porções dos dados são recuperadas do arquivo e colocadas
em uma área de memória gerenciada pelo programa (por exemplo, uma variável);
write: as partes dos dados da memória (por exemplo, uma variável)
são transferidas para o arquivo.

Existem três modos básicos usados para abrir o stream:

read mode: permite apenas operações de leitura; tentar gravar no fluxo
causará uma exceção (a exceção é chamada UnsupportedOperation, que herda
OSError e ValueError e vem do módulo io);
write mode: permite apenas operações de gravação; tentar ler o fluxo
causará a exceção mencionada acima;
update mode: permite gravações e leituras."""





