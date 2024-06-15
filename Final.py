import pygame
import simpleGE
import random

pygame.init()
fps = 30

pygame.mixer.init()
pygame.mixer.music.load('menumusic.mp3')
pygame.mixer.music.play(loops=-1, start=20, fade_ms=2000)
pygame.mixer.music.set_volume(0.1)

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 40)
        self.fgColor = "white"
        self.clearBack = True

class LblTimer(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time: 30"
        self.center = (550, 40)
        self.fgColor = "white"
        self.clearBack = True

class Chocolate(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("chocolate.png")
        self.setSize(60, 60)
        self.image_width, self.image_height = self.image.get_size()
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.scene.background.get_width() - self.image_width)
        self.y = 20
        self.dy = random.randint(2, 8)

    def process(self):
        self.y += self.dy
        if self.bottom > self.scene.background.get_height():
            self.reset()
            
class Chocolate1(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("chocolate1.png")
        self.position = (320, 300)
        self.setSize(280, 240)


class Gumball(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("gumballs.png")
        self.setSize(60, 60)
        self.image_width, self.image_height = self.image.get_size()
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.scene.background.get_width() - self.image_width)
        self.y = 20
        self.dy = random.randint(1, 4)

    def process(self):
        self.y += self.dy
        if self.bottom > self.scene.background.get_height():
            self.reset()

class Broccoli(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("broccoli.png")
        self.setSize(60, 60)
        self.image_width, self.image_height = self.image.get_size()
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.scene.background.get_width() - self.image_width)
        self.y = 10
        self.dy = random.randint(1, 4)

    def process(self):
        self.y += self.dy
        if self.bottom > self.scene.background.get_height():
            self.reset()

class Ghost(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.neutral = pygame.image.load("ghostUser.png")
        self.happy = pygame.image.load("happyGhost.png")
        self.gross = pygame.image.load("ewGhost.png")
        self.image = self.neutral
        self.rect = self.image.get_rect()
        self.setSize(140, 140)
        self.position = (320, 410)
        self.facing_right = True

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.facing_right = not self.facing_right

    def react_to_chocolate(self):
        self.image = self.happy
        self.setSize(140, 140)
        self.rect = self.image.get_rect()
        self.facing_right = False
    
    def react_to_gumballs(self):
        self.image = self.happy
        self.setSize(140, 140)
        self.rect = self.image.get_rect()
        self.facing_right = False
    
    def react_to_broccoli(self):
        self.image = self.gross
        self.setSize(140, 140)
        self.rect = self.image.get_rect()
        self.facing_right = False

    def reset_image(self):
        self.image = self.neutral

    def process(self):
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += 7
            if not self.facing_right:
                self.flip()
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= 7
            if self.facing_right:
                self.flip()

class BouncingGhost(simpleGE.Sprite):
    def __init__(self, scene, image, start_position):
        super().__init__(scene)
        self.setImage(image)
        self.setSize(175, 200)
        self.position = start_position
        self.dy = 1

    def process(self):
        self.y += self.dy
        if self.y > self.scene.background.get_height() - 120 or self.y < self.scene.background.get_height() -180:
            self.dy = -self.dy

class BouncingGhostInstructions(BouncingGhost):
    def __init__(self, scene, image, start_position):
        super().__init__(scene, image, start_position)
        self.setImage(image)
        self.setSize(175, 200)
        self.position = start_position
        self.dy = 1

    def process(self):
        self.y += self.dy
        if self.y > self.scene.background.get_height() - 90 or self.y < self.scene.background.get_height() - 120:
            self.dy = -self.dy

class TrickOrTreat(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("trickortreat.png")
        self.setSize(600, 600)
        self.position = (320, 300)
        self.dy = 1

    def process(self):
        self.y += self.dy
        if self.y > self.scene.background.get_height() - 170 or self.y < self.scene.background.get_height() - 220:
            self.dy = -self.dy
            
class treat(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("treat.png")
        self.position = (320, 150)
        
class NiceWork(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("NiceWork.png")
        self.position = (220, 60)


class Menu(simpleGE.Scene):
    def __init__(self):
        
        super().__init__()
        self.setImage("night.png")

        self.lblTitle = simpleGE.Label()
        self.lblTitle.text = " "
        self.lblTitle.center = (320, 100)
        self.lblTitle.fgColor = "white"
        self.lblTitle.clearBack = True

        self.btnStart = simpleGE.Button()
        self.btnStart.bgColor = "purple"
        self.btnStart.fgColor = "white"
        self.btnStart.text = "Start"
        self.btnStart.center = (320, 195)

        self.btnQuit = simpleGE.Button()
        self.btnQuit.bgColor = "purple"
        self.btnQuit.fgColor = "white"
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (320, 235)

        self.ghostLeft = BouncingGhost(self, "ghostleft.png", (120, self.background.get_height() - 180))
        self.ghostRight = BouncingGhost(self, "ghostright.png", (520, self.background.get_height() - 180))
        
        self.trickOrTreat = TrickOrTreat(self)

        self.sprites = [self.lblTitle, self.btnStart, self.btnQuit, self.ghostLeft, self.ghostRight, self.trickOrTreat]
  
    def process(self):
        if self.btnStart.clicked:
            self.next = "instructions"
            self.stop()
        if self.btnQuit.clicked:
            self.next = "quit"
            self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("instructions.png")

        self.lblInstructions = simpleGE.Label()
        self.lblInstructions.text = " "
        self.lblInstructions.center = (320, 200)
        self.lblInstructions.fgColor = "white"
        self.lblInstructions.clearBack = True

        self.btnBegin = simpleGE.Button()
        self.btnBegin.text = "Begin"
        self.btnBegin.fgColor = "white"
        self.btnBegin.center = (320, 210)
        self.btnBegin.bgColor = "purple"
        
        self.bouncingGhost = BouncingGhostInstructions(self, "ghostRight.png", (520, self.background.get_height() - 120))

        self.sprites = [self.lblInstructions, self.btnBegin, self.bouncingGhost]

    def process(self):
        if self.btnBegin.clicked:
            self.next = "begin"
            self.stop()

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 30
        self.setImage("night.png")
        self.setCaption("Spooky")
        self.lblScore = LblScore()
        self.lblTimer = LblTimer()
        self.ghost = Ghost(self)
        self.chocolates = [Chocolate(self) for _ in range(5)]
        self.broccolis = [Broccoli(self) for _ in range(5)]
        self.gumballs = [Gumball(self) for _ in range(5)]
        self.sprites = [self.lblScore, self.lblTimer, self.ghost] + self.chocolates + self.broccolis + self.gumballs
        pygame.mixer.init()
        pygame.mixer.music.load('maingamemusic.mp3')
        pygame.mixer.music.play(loops=-1, start=0, fade_ms=5000)
        pygame.mixer.music.set_volume(0.3)
        self.fadeout_duration = 7000

    def process(self):
        for chocolate in self.chocolates:
            if self.ghost.collidesWith(chocolate):
                chocolate.reset()
                self.score += 3
                self.lblScore.text = f"Score: {self.score}"
                self.ghost.react_to_chocolate()

        for broccoli in self.broccolis:
            if self.ghost.collidesWith(broccoli):
                broccoli.reset()
                self.score -= 2
                self.lblScore.text = f"Score: {self.score}"
                self.ghost.react_to_broccoli()

        for gumball in self.gumballs:
            if self.ghost.collidesWith(gumball):
                gumball.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                self.ghost.react_to_gumballs()

        timeLeft = self.timer.getTimeLeft()
        self.lblTimer.text = f"Time: {int(timeLeft)}"
        
        if timeLeft <= self.fadeout_duration / 2000:
            pygame.mixer.music.fadeout(int(timeLeft * 1000))
        
        if timeLeft < 0:
            self.stop()

class GameOver(simpleGE.Scene):
    def __init__(self):
        super().__init__()

        pygame.mixer.music.load('maingamemusic.mp3')
        pygame.mixer.music.play(loops=-1, start=20, fade_ms=2000)
        pygame.mixer.music.set_volume(0.1)

        self.gameover_sound = pygame.mixer.Sound('booandlaugh.mp3')
        self.gameover_sound.set_volume(0.8)

        self.setImage("night.png")
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Score: 0"
        self.lblScore.center = (540, 60)
        self.lblScore.bgColor = "purple"
        self.lblScore.fgColor = "white"

        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "quit"
        self.btnQuit.bgColor = "purple"
        self.btnQuit.fgColor = "white"
        self.btnQuit.center = (100, 240)

        self.btnAgain = simpleGE.Button()
        self.btnAgain.text = "play again"
        self.btnAgain.bgColor = "purple"
        self.btnAgain.fgColor = "white"
        self.btnAgain.center = (540, 240)
        
        self.NiceWork = NiceWork(self)
        self.treat = treat(self)
        self.chocolate1 = Chocolate1(self)

        self.sprites = [self.lblScore, self.btnQuit, self.btnAgain, self.NiceWork, self.treat, self.chocolate1]

    def setScore(self, score):
        self.score = score

    def start(self):
        self.gameover_sound.play()
        super().start()

    def process(self):
        self.lblScore.text = f"{self.score}"

        if self.btnQuit.clicked:
            self.next = "quit"
            self.stop()
        if self.btnAgain.clicked:
            self.next = "again"
            self.stop()
            
def start(self):
    self.gameover_sound.play()
    super().start()
            

def main():
    keepGoing = True
    while keepGoing:
        menu = Menu()
        menu.start()

        if menu.next == "quit":
            keepGoing = False
            continue

        if menu.next == "instructions":
            instructions = Instructions()
            instructions.start()

            if instructions.next == "begin":
                game = Game()
                game.start()

                gameOver = GameOver()
                gameOver.setScore(game.score)
                gameOver.start()

                if gameOver.next == "quit":
                    keepGoing = False

if __name__ == "__main__":
    main()