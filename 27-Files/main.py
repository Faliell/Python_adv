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


""" File handles """


""" Python assume que todo arquivo está oculto atrás de um
 objeto de uma classe adequada."""


""" Um objeto de classe adequada é criado quando você abre
 o arquivo e o aniquila no momento de fechar."""


""" Nota: você nunca usa construtores para dar vida a esses objetos.
 A única maneira de obtê-los é invocando a função chamada open().
 Se você quiser se livrar do objeto, você invoca o método chamado close()
 """

""" io.IOBase é uma classe base abstrata que representa a interface
 comum para objetos de fluxo de entrada/saída.
As classes derivadas de io.IOBase incluem io.TextIOBase (para manipulação
 de fluxos de texto), io.BufferedIOBase (para operações de E/S em buffer)
  e várias outras """


""" todos os fluxos são divididos em fluxos de texto e binários."""


""" Então surge um problema sutil. Em sistemas Unix/Linux, os finais de linha
 são marcados por um único caractere denominado LF (código ASCII 10) designado 
 em programas Python como \n.

Outros sistemas operacionais, especialmente aqueles derivados do sistema
pré-histórico CP/M (que também se aplica aos sistemas da família Windows)
usam uma convenção diferente: o final da linha é marcado por um par de caracteres,
CR e LF (códigos ASCII 13 e 10 ) que pode ser codificado como \r\n."""


""" Tais características indesejáveis do programa, que impedem ou dificultam
 a utilização do programa em diferentes ambientes, são chamadas de não
  portabilidade.

Da mesma forma, a característica do programa que permite a execução em
 diferentes ambientes é chamada de portabilidade."""


""" durante a leitura/gravação de linhas de/para o arquivo associado,
nada de especial ocorre no ambiente Unix, mas quando as mesmas operações
são executadas no ambiente Windows, ocorre um processo chamado tradução
de caracteres de nova linha: quando você lê uma linha do arquivo, cada par
de caracteres \r\n é substituído por um único caractere \n e vice-versa;
durante operações de gravação, cada caractere \n é substituído por um par
de caracteres \r\n;"""


""" Opening the streams """


# stream = open(file, mode = 'r', encoding = None)


""" Nota: os argumentos mode e encoding podem ser omitidos – seus
valores padrão são então assumidos. O modo de abertura padrão é lido em modo
texto, enquanto a codificação padrão depende da plataforma utilizada."""


""" 
r open mode: read
    o arquivo associado ao fluxo deve existir e ser legível
    
w open mode: write
    o arquivo associado ao stream não precisa existir; se não existir será criado; 
    se existir, será truncado para o comprimento zero (apagado)
    
a open mode: append
    o arquivo associado ao stream não precisa existir; se não existir,
    será criado; se existir, o cabeçote de gravação virtual será colocado no
    final do arquivo (o conteúdo anterior do arquivo permanece intacto).
    
r+ open mode: read and update
    o arquivo associado ao fluxo deve existir e ser gravável
    
w+ open mode: write and update
    o arquivo associado ao stream não precisa existir; se não existir,
    será criado; o conteúdo anterior do arquivo permanece intacto
"""









