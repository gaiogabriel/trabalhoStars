from tkinter import Tk, simpledialog
import pygame
import pickle

pygame.init()
branco = (255,255,255)
vermelho = (255,0, 0)
preto = (0,0,0)
clock = pygame.time.Clock()
tela =  pygame.display.set_mode( (800,600) )
fundo= pygame.image.load("fundo.jpg")
pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption('Star and Space')
fonte= pygame.font.Font(None, 20)
texto1= fonte.render("Pressione F10 para salvar os pontos", True, branco)
texto2= fonte.render("Pressione F11 para carregar os pontos", True, branco)
texto3= fonte.render("Pressione F12 para deletar os pontos", True, branco)
cordenada = (10,10)
cordenada1 = (10,30)
cordenada2 = (10,50)

cordenadas = []
root= Tk()

def line():
    for i in range( len( cordenadas) - 1):
        pygame.draw.line(tela, branco, cordenadas[i], cordenadas[i + 1])
        
        d1 = cordenadas[i][0]
        d2 = cordenadas[i + 1][0]
        d3 = cordenadas[i][1]
        d4 = cordenadas[i + 1][1]
        x = d1,d2
        x = sorted(x)
        y = d3,d4
        y = sorted(y)
        
        diferencax = abs(x[0] - x[1])
        diferencay = abs(y[0] - y[1])
        diferenca = diferencax, diferencay
        x = x[0] + (diferencax / 2)
        y = y[0] + (diferencay / 2)
        cordenadaTexto = (x,y) 

        fonte = pygame.font.Font(None, 20)
        texto  = fonte.render(str(diferenca), True,branco)
        tela.blit(texto, cordenadaTexto)

    pygame.display.flip()
running = True
while running:
    tela.blit(fundo,(0,0))
    tela.blit(texto1, cordenada)
    tela.blit(texto2, cordenada1)
    tela.blit(texto3, cordenada2)  

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE:
            running = False
        elif evento.type  == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                x,y = evento.pos
                pygame.draw.circle(tela, branco,(x,y), 5)
                xy = x,y
                cordenadas.append(xy)
                line()
                pygame.display.update() 
        elif evento.type == pygame.MOUSEBUTTONUP:
            root.withdraw()
            pos= pygame.mouse.get_pos()
            item= simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            if item == None:
                item = "desconhecido"+str(pos)
                cordenadas[item]= pos
                root.destroy()      
        

    pygame.display.update()
    clock.tick(60)
pygame.quit()