import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton =pg.image.load("fig/3.png")
    koukaton=pg.transform.flip(koukaton,True,False)
    bg_img_2=pg.transform.flip(bg_img,True,False)

    kk_rct=koukaton.get_rect()
    kk_rct.center=300,200
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst=pg.key.get_pressed()
        
        if key_lst[pg.K_UP]:
            X,y=-1,-1
        elif key_lst[pg.K_DOWN]:
            X,y=-1,1
        elif key_lst[pg.K_LEFT]:
            X,y=-1,0
        elif key_lst[pg.K_RIGHT]:
            X,y=1,0
        else:
            X,y=-1,0
        kk_rct.move_ip(X,y)


        
        
        x=tmr%3201
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_2,[-x+1600,0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(koukaton,kk_rct)
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()