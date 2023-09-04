"""
https: // pypi.org /

pip significa “pip instala pacotes”
"""

"""
pip3 --version or pip --version
pip help

* pip help operation:
pip help install
pip list

pip show pip

quais pacotes são necessários para utilizar o pacote com sucesso ( Requires:)
quais pacotes precisam que o pacote seja utilizado com sucesso ( Required-by:)

- depreciado:
pip search pip

+ --user instala somente para o usuário local, excluindo vai para todo sistema
pip install --user pygame
pip show pygame
pip list

*  -U significa update. 
pip install -U package_name

* versão exata
pip install package_name==package_version
pip install pygame==1.9.2

pip uninstall package_name
pip uninstall pygame

"""

""" 
dependência é um fenômeno que aparece toda vez que você usa um software
que depende de outro software . 

O pip pode fazer tudo isso.
"""

import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT \
                or event.type == pygame.MOUSEBUTTONUP \
                or event.type == pygame.KEYUP:
            run = False

