from tkinter import Tk, simpledialog
import pygame
pygame.init()
tamanho = (1000,650)
branco= (255,255,255)
tela= pygame.display.set_mode(tamanho)
fundo= pygame.image.load("fundo.jpg")
fonte= pygame.font.Font(None, 20)
running= True
texto1= fonte.render("Pressione F10 para salvar os pontos", True, branco)
texto2= fonte.render("Pressione F11 para carregar os pontos", True, branco)
texto3= fonte.render("Pressione F12 para deletar os pontos", True, branco)
cordenada = (10,10)
cordenada1 = (10,30)
cordenada2 = (10,50)
estrelas={}
root= Tk()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        elif event.type == pygame.MOUSEBUTTONUP:
            root.withdraw()
            pos= pygame.mouse.get_pos()
            item= simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            if item == None:
                item = "desconhecido"+str(pos)
            estrelas[item]= pos
            root.destroy()
    tela.fill(branco)
    tela.blit(fundo,(0,0))
    tela.blit(texto1, cordenada)
    tela.blit(texto2, cordenada1)
    tela.blit(texto3, cordenada2)   
    pygame.display.update()
pygame.quit()