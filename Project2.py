import pygame,sys
import math
from random import randint
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


bulletImage = pygame.image.load('bullet.png')
bullet_X = 500
bullet_Y = 0
bullet_Xchange = 3
bullet_Ychange = 0
bullet_state = "rest"



def bullet(x,y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"


    



# Collision Concept
def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) +
                         (math.pow(y1 - y2,2)))
    if distance <= 50:
        return True
    else:
        return False
        
    
class enemy_goblin(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image=pygame.image.load("enemy_globlin.png").convert_alpha()
        self.rect=self.image.get_rect(topleft=pos)


                 
class Tree(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image=pygame.image.load("tree.png").convert_alpha()
        self.rect=self.image.get_rect(topleft=pos)

        
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        img_c = pygame.image.load("player.png").convert_alpha()
        self.img_c = pygame.image.load("player.png").convert_alpha()
        #right
        self.image=pygame.transform.scale(img_c,(100,100))
        #left
        self.image2=pygame.transform.scale(img_c,(100,100))
        self.image_bullet=pygame.image.load("bullet.png").convert_alpha()
        self.rect=self.image.get_rect(center=pos)
        self.direction=pygame.math.Vector2()
        self.speed=5
        self.initial_HP=100
        self.initial_ATK=200
        self.initial_DEF=50
        self.initial_stamina=100
        self.initial_crit_rate=0.05
        self.initial_crit_DMG=1.2
        self.initial_energy_recharge=1
        self.initial_elemental_mastery=0
        self.initial_Pyro_DMG_Bonus=0
        self.initial_Cryo_DMG_Bonus=0
        self.initial_Anemo_DMG_Bonus=0
        self.initial_Electro_DMG_Bonus=0


        

    def determine_position(self):
 
        flipped = None
        if self.direction.x > 0:
            self.image = self.image2
                
        elif self.direction.x <0:
            if not flipped:
                self.image = pygame.transform.flip(self.image2,True,False)
                flipped = True
        else:
            #look middle
            pass





        
    def input(self):
        keys=pygame.key.get_pressed()
       
    
#up and down
        if keys[pygame.K_s]:
            self.direction.y=1
        elif keys[pygame.K_w]:
            self.direction.y=-1
        else:
            self.direction.y=0
        if keys[pygame.K_SPACE]:
            ima4 = pygame.image.load("HP.png").convert_alpha()
            imp4 = pygame.transform.scale(ima4,(60,60))
            ima3 = pygame.image.load("DEF.png").convert_alpha()
            imp3 = pygame.transform.scale(ima3,(60,60))
            ima6 = pygame.image.load("stamina.png").convert_alpha()
            imp6 = pygame.transform.scale(ima6,(60,60))
            screen.blit(imp6, (0, 120))
            screen.blit(imp4, (0, 0))
            screen.blit(imp3, (0, 60))
            font = pygame.font.SysFont('Calibri', 15, True, False)
            text_HP= font.render(str(self.initial_HP),True,BLACK)
            text_DEF= font.render(str(self.initial_DEF),True,BLACK)
            text_stamina= font.render(str(self.initial_stamina),True,BLACK)
            screen.blit(text_HP, [50,25])
            screen.blit(text_DEF, [50,80])
            screen.blit(text_stamina, [50,150])
            
            
            
            
            
        
#left and right        
        if keys[pygame.K_a]:
            self.direction.x=-1
                
            
        elif keys[pygame.K_d]:
            self.direction.x=1
            
        else:
            self.direction.x=0

# sprint
        if keys[pygame.K_LSHIFT] and keys[pygame.K_d]:
            self.direction.x=5
            global current_stamina
            current_stamina=self.initial_stamina-5

            
        if keys[pygame.K_LSHIFT] and keys[pygame.K_a]:
            self.direction.x=-5
            current_stamina=self.initial_stamina-5


#bag/status
        if keys[pygame.K_b]:
            screen.fill("#cd7f32")


            
#load picture 
            ima = pygame.image.load("character_bag.png").convert_alpha()
            ima2 = pygame.image.load("ATK.png").convert_alpha()
            ima3 = pygame.image.load("DEF.png").convert_alpha()
            ima4 = pygame.image.load("HP.png").convert_alpha()
            ima5 = pygame.image.load("recharge.png").convert_alpha()
            ima6 = pygame.image.load("stamina.png").convert_alpha()
            ima7 = pygame.image.load("electric.png").convert_alpha()
            ima8 = pygame.image.load("fire.png").convert_alpha()
            ima9 = pygame.image.load("ice.png").convert_alpha()
            ima10 = pygame.image.load("wind.png").convert_alpha()
            ima11 = pygame.image.load("mastery.png").convert_alpha()
            ima12 = pygame.image.load("bag_edge.png").convert_alpha()
            ima_skill_1 = pygame.image.load("skill1.png").convert_alpha()
            ima_skill_2 = pygame.image.load("skill2.png").convert_alpha()


            #change image size
            imp = pygame.transform.scale(ima,(100,100))
            imp2 = pygame.transform.scale(ima2,(50,50))
            imp3 = pygame.transform.scale(ima3,(50,50))
            imp4 = pygame.transform.scale(ima4,(50,50))
            imp5 = pygame.transform.scale(ima5,(50,50))
            imp6 = pygame.transform.scale(ima6,(50,50))
            imp7 = pygame.transform.scale(ima7,(40,40))
            imp8 = pygame.transform.scale(ima8,(37,37))
            imp9 = pygame.transform.scale(ima9,(40,40))
            imp10 = pygame.transform.scale(ima10,(40,40))
            imp11 = pygame.transform.scale(ima11,(50,50))
            imp12 = pygame.transform.scale(ima12,(50,700))
            
            #text of character details
            pygame.draw.line(screen, "#f1c232", [300, 0], [300, 715], 5)
            pygame.draw.line(screen, "#f1c232", [550, 0], [550, 715], 5)
            font = pygame.font.SysFont('Calibri', 15, True, False)
            font2 = pygame.font.SysFont('Calibri', 30, True, False)
            text1 = font2.render("Skills",True,BLACK)
            text2 = font2.render("Props",True,BLACK)
            text3 = font2.render("Buff",True,BLACK)
            text4 = font2.render("Debuff",True,BLACK)
            text5 = font2.render("Details",True,BLACK)
            text6 = font.render("HP/Max HP:",True,BLACK)
            text7 = font.render("Max Stamina",True,BLACK)
            text8 = font.render("ATK:",True,BLACK)
            text9 = font.render("DEF:",True,BLACK)
            text10 = font.render("CRIT Rate:",True,BLACK)
            text11 = font.render("CRIT DMG:",True,BLACK)
            text12 = font.render("Elemental Mastery:",True,BLACK)
            text13 = font.render("Energy Recharge:",True,BLACK)
            text14 = font.render("Pyro DMG Bonus:",True,BLACK)
            text15 = font.render("Cryo DMG Bonus:",True,BLACK)
            text16 = font.render("Anemo DMG Bonus:",True,BLACK)
            text17 = font.render("Electro DMG Bonus:",True,BLACK)
            text_HP= font.render(str(self.initial_HP),True,BLACK)
            text_ATK= font.render(str(self.initial_ATK),True,BLACK)
            text_DEF= font.render(str(self.initial_DEF),True,BLACK)
            text_stamina= font.render(str(self.initial_stamina),True,BLACK)
            text_crit_rate= font.render(str(self.initial_crit_rate),True,BLACK)
            text_crit_DMG= font.render(str(self.initial_crit_DMG),True,BLACK)
            text_energy_recharge= font.render(str(self.initial_energy_recharge),True,BLACK)
            text_elemental_mastery= font.render(str(self.initial_elemental_mastery),True,BLACK)
            text_Pyro_DMG_Bonus= font.render(str(self.initial_Pyro_DMG_Bonus),True,BLACK)
            text_Cryo_DMG_Bonus= font.render(str(self.initial_Cryo_DMG_Bonus),True,BLACK)
            text_Anemo_DMG_Bonus= font.render(str(self.initial_Anemo_DMG_Bonus),True,BLACK)
            text_Electro_DMG_Bonus= font.render(str(self.initial_Electro_DMG_Bonus),True,BLACK)
            #show on the screen, text
            screen.blit(text1, [400, 80])
            screen.blit(text2, [400, 400])
            screen.blit(text3, [100, 80])
            screen.blit(text4, [100, 400])
            screen.blit(text5, [800, 280])
            screen.blit(text6, [625, 320])
            screen.blit(text7, [625, 350])
            screen.blit(text8, [625, 380])
            screen.blit(text9, [625, 410])
            screen.blit(text10, [625, 440])
            screen.blit(text11, [625, 470])
            screen.blit(text12, [625, 500])
            screen.blit(text13, [625, 540])
            screen.blit(text14, [625, 570])
            screen.blit(text15, [625, 600])
            screen.blit(text16, [625, 630])
            screen.blit(text17, [625, 660])
            #changing details data
            screen.blit(text_HP, [1000, 320])
            screen.blit(text_ATK, [1000, 380])
            screen.blit(text_DEF, [1000, 410])
            screen.blit(text_stamina, [1000, 350])
            screen.blit(text_crit_rate, [1000, 440])
            screen.blit(text_crit_DMG, [1000, 470])
            screen.blit(text_energy_recharge, [1000, 540])
            screen.blit(text_elemental_mastery, [1000, 500])
            screen.blit(text_Pyro_DMG_Bonus, [1000, 570])
            screen.blit(text_Cryo_DMG_Bonus, [1000, 600])
            screen.blit(text_Anemo_DMG_Bonus, [1000, 630])
            screen.blit(text_Electro_DMG_Bonus, [1000, 660])
            
            
            
 #show on the screen image
            screen.blit(imp, (750, 10))
            screen.blit(imp2, (560, 360))
            screen.blit(imp3, (560, 390))
            screen.blit(imp4, (560, 300))
            screen.blit(imp5, (560, 520))
            screen.blit(imp6, (560, 330))
            screen.blit(imp7, (570, 640))
            screen.blit(imp8, (570, 550))
            screen.blit(imp9, (570, 580))
            screen.blit(imp10, (570, 610))
            screen.blit(imp11, (560, 480))
            screen.blit(imp12, (1150, 10))
            screen.blit(ima_skill_1, (440, 130))
            screen.blit(ima_skill_2, (270, 100))
            
#update portion of the screen 
            pygame.display.flip()
            status = True
            while (status):
                  # iterate over the list of Event objects
                  # that was returned by pygame.event.get() method.
                for i in pygame.event.get():
 
                    # if event object type is QUIT
                    # then quitting the pygame
                    # and program both.
                    if i.type == pygame.QUIT:
                        status = False
            
    def update(self):
        self.input()
        self.determine_position()
        self.rect.center+=self.direction*self.speed
            
            
class CameraGroup(pygame.sprite.Group): 
    def __init__(self):
        super().__init__()
        self.display_surface=pygame.display.get_surface()

        #camera offset
        self.offset=pygame.math.Vector2()
        self.half_w=self.display_surface.get_size()[0]//2
        self.half_h=self.display_surface.get_size()[1]//2

        #ground
        backgroundimg = pygame.image.load("level1ground.jpg").convert_alpha()
        backgroundimg2 = pygame.transform.scale(backgroundimg,(1200,1000))
        self.ground_surf=backgroundimg2
        self.ground_rect=self.ground_surf.get_rect(topleft=(0,0))
        #camera offset
    def center_target_camera(self,target):
        self.offset.x=target.rect.centerx-self.half_w
        self.offset.y=target.rect.centery-self.half_h
        

    def custom_draw(self,player):
        self.center_target_camera(player)
        #ground
        ground_offset=self.ground_rect.topleft-self.offset
        self.display_surface.blit(self.ground_surf,ground_offset)
        #active
        for sprite in sorted(self.sprites(),key=lambda sprite:sprite.rect.centery):
            offset_pos=sprite.rect.topleft-self.offset
            self.display_surface.blit(sprite.image,offset_pos)
            
pygame.init()
screen=pygame.display.set_mode((1200,715))
clock=pygame.time.Clock()
#set up
camera_group=CameraGroup()
player=Player((640,360),camera_group)
#trees
for i in range(60):
    random_x=randint(0,3000)
    random_y=randint(0,3000)
    Tree((random_x,random_y),camera_group)


goblin_Xchange=[]
goblin_Ychange=[]

for i in range(10):
    random_x=randint(0,3000)
    random_y=randint(0,3000)
    enemy_goblin((random_x,random_y),camera_group)
'''    goblin_Xchange.append=[1.2]
    goblin_Ychange.append=[50]

'''
    
while True:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill("#71ddee")

    camera_group.update()
    camera_group.custom_draw(player)
    
    pygame.display.update()
    clock.tick(100)








    
