import pygame, sys, random

class Runner():
    __customes=("turtle", "fish", "smallball", "moray", "prawn", "octopus")
    
    def __init__(self, x=0, y=0):
        ixCustome=random.randint(0,5)
        self.custome=pygame.image.load("./images/{}.png".format(self.__customes[ixCustome]))
        self.position=[x,y]
        self.name=""
        
    def avanzar(self):
        self.position[0]+=random.randint(1,6)
        
class Game():
    runners=[]
    __posY=(155,200,242,287)
    __names=("Speedy","Rayo","Alonso","Gary")
    __startLine=-20
    __finishLine=620
    
    def __init__(self):
        self.__screen=pygame.display.set_mode((640,480))
        self.__background=pygame.image.load("./images/background.png")
        pygame.display.set_caption("Carrera de BICHOS")

        for i in range(4):
            theRunner=Runner(self.__startLine,self.__posY[i])
            theRunner.name=self.__names[i]
            self.runners.append(theRunner)
        
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):         
        gameOver=False
        while not gameOver:
#comprobar eventos
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=True
#actualizar pantalla y corredores        
            for activeRunner in self.runners:
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver=True
            
#refresca la pantalla            
            self.__screen.blit(self.__background,(0,0)) 
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)

            pygame.display.flip()
            
#comprobacion de eventos para que buffer no se llene
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.close()

if __name__=="__main__":
    game=Game()
    pygame.font.init()
    game.competir()
    