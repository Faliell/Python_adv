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


""" Selecting text and binary modes """


""" 
Se houver uma letra b no final da string de modo, significa que o fluxo deve ser aberto em modo binário.

Se a string de modo terminar com a letra t, o fluxo será aberto em modo de texto. 
"""


""" 
O modo de texto é o comportamento padrão assumido quando nenhum especificador de modo binário/texto é usado.

A abertura bem-sucedida de um arquivo definirá a posição atual do arquivo (a cabeça virtual de
 leitura/gravação) antes do primeiro byte do arquivo se o modo não for "a" e após o último byte do arquivo
se o modo estiver definido como "a".
"""

""" 
Text    mode	Binary mode	Description
rt	    rb	    read
wt	    wb	    write
at	    ab	    append
r+t 	r+b	    read and update
w+t	    w+b	    write and update
"""

""" 
EXTRA
Você também pode abrir um arquivo para sua criação exclusiva. Você pode fazer isso usando o "x" open mode.
 Se o arquivo já existir, a função open() gerará uma exceção.
"""


""" Opening the stream for the first time """

# r ignora as \

try:
    stream = open(r"C:\Users\User\DesktopFile.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)


""" Pre-opened streams """


""" 
Em programação, "fluxos" referem-se a uma maneira de lidar com a entrada e saída de dados.
São canais de comunicação através dos quais você pode enviar e receber informações.
 """


""" Dissemos anteriormente que qualquer operação de stream deve ser precedida pela invocação da função open().
 Existem três exceções bem definidas à regra.

Quando nosso programa começa, os três streams já estão abertos e não requerem nenhum preparo extra.
Além do mais, seu programa pode usar esses fluxos explicitamente se você importar o módulo sys 

porque é onde é colocada a declaração dos três fluxos.

Os nomes desses fluxos são: sys.stdin, sys.stdout e sys.stderr.
"""


"""
Vamos analisá-los:

sys.stdin
stdin (como entrada padrão)
    o fluxo stdin é normalmente associado ao teclado, pré-aberto para leitura e considerado a principal
    fonte de dados para os programas em execução;
    a conhecida função input() lê dados de stdin por padrão.

sys.stdout
stdout (como saída padrão)
    o fluxo stdout é normalmente associado à tela, pré-aberta para escrita, considerada o alvo 
    principal para saída de dados pelo programa em execução;
    a conhecida função print() envia os dados para o fluxo stdout.

sys.stderr
stderr (como saída de erro padrão)
    o fluxo stderr normalmente está associado à tela, pré-aberta para escrita, considerada o local principal
    para onde o programa em execução deve enviar informações sobre os erros encontrados durante seu trabalho;
    a separação do stdout (resultados úteis produzidos pelo programa) do stderr (mensagens de erro, inegavelmente
    úteis, mas que não fornecem resultados) dá a possibilidade de redirecionar estes dois tipos de informação para
    os diferentes alvos.
"""


""" Closing streams """


""" A última operação executada em um stream (isso não inclui os streams stdin, stdout e stderr,
 que não exigem isso) deve ser "close".

Essa ação é executada por um método invocado de dentro do objeto de fluxo aberto: stream.close()."""


""" 
a maioria dos desenvolvedores acredita que a função close() sempre é bem-sucedida e, portanto, 
não há necessidade de verificar se ela executou sua tarefa corretamente.

Esta crença é apenas parcialmente justificada. Se o fluxo foi aberto para escrita e depois uma série
de operações de escrita foram executadas, pode acontecer que os dados enviados ao fluxo ainda não tenham
sido transferidos para o dispositivo físico (devido a um mecanismo chamado cache ou buffer).

Como o fechamento do fluxo força os buffers a liberá-los, pode ser que as liberações falhem e,
portanto, o close() falhe também.
"""


""" Diagnosing stream problems """


"""O objeto IOError é equipado com uma propriedade chamada errno (o nome vem da frase 
número do erro) e você pode acessá-lo da seguinte forma:"""


try:
    # Some stream operations.
    stream = open(r"C:\Users\User\DesktopFile.txt", "rt")
except IOError as exc:
    print(exc.errno)


""" 
Algumas constantes selecionadas úteis para detectar erros de stream:

errno.EACCES → Permissão negada

O erro ocorre quando você tenta, por exemplo, abrir um arquivo com o atributo somente leitura para escrita.

errno.EBADF → Número de arquivo inválido

O erro ocorre quando você tenta, por exemplo, operar com um fluxo não aberto.

errno.EEXIST → Arquivo existe

O erro ocorre quando você tenta, por exemplo, renomear um arquivo com seu nome anterior.

errno.EFBIG → Arquivo muito grande

O erro ocorre ao tentar criar um arquivo maior que o máximo permitido pelo sistema operacional.

errno.EISDIR → É um diretório

O erro ocorre quando você tenta tratar um nome de diretório como o nome de um arquivo comum.

errno.EMFILE → Muitos arquivos abertos

O erro ocorre quando você tenta abrir simultaneamente mais fluxos do que o aceitável para o seu sistema operacional.

errno.ENOENT → Arquivo ou diretório inexistente

O erro ocorre quando você tenta acessar um arquivo/diretório inexistente.

errno.ENOSPC → Não há espaço restante no dispositivo

O erro ocorre quando não há espaço livre na mídia.

"""

# Exemplo de tratamento de erros
import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)


# Simplificada com os
from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))
