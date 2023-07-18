#import modules
import math
import pygame as pg
import sys

# Colors
blue = pg.Color('blue')
red = pg.Color('red')

# Define main function
def main():
    running = True
    
    # Initialize some variables needed later and create pygame surface
    pi = math.pi

    black = (0, 0, 0)
    white = (255, 255, 255)

    dt = 0.01

    l1_1 = 100
    l2_1 = 100

    l1_2 = 100
    l2_2 = 100
    
    l1_3 = 100
    l2_3 = 100
    
    m1_1 = 50
    m2_1 = 50
    
    m1_2 = 51
    m2_2 = 51
    
    m1_3 = 52
    m2_3 = 52
    
    thetha1_1 = pi/3
    thetha2_1 = pi/8
    
    thetha1_2 = pi/3
    thetha2_2 = pi/8
    
    thetha1_3 = pi/3
    thetha2_3 = pi/8
    
    v1_1 = 0
    v2_1 = 0
    
    v1_2 = 0
    v2_2 = 0
    
    v1_3 = 0
    v2_3 = 0
    
    g = 50
    
    s = pg.display.set_mode([500, 500])
    
    while running:
        x1_1 = l1_1 * math.sin(thetha1_1) + 250
        y1_1 = l1_1 * math.cos(thetha1_1) + 250
        
        x2_1 = l2_1 * math.sin(thetha2_1) + x1_1
        y2_1 = l2_1 * math.cos(thetha2_1) + y1_1
        
        x1_2 = l1_2 * math.sin(thetha1_2) + 250
        y1_2 = l1_2 * math.cos(thetha1_2) + 250
        
        x2_2 = l2_2 * math.sin(thetha2_2) + x1_2
        y2_2 = l2_2 * math.cos(thetha2_2) + y1_2
        
        x1_3 = l1_3 * math.sin(thetha1_3) + 250
        y1_3 = l1_3 * math.cos(thetha1_3) + 250
        
        x2_3 = l2_3 * math.sin(thetha2_3) + x1_3
        y2_3 = l2_3 * math.cos(thetha2_3) + y1_3
        
        s.fill(white)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        # Double Pendulum 1       
        pg.draw.line(
            start_pos=(30, 250), end_pos=(470, 250), color=black, surface=s
        )
        pg.draw.line(
            start_pos=(250, 250), end_pos=(x1_1, y1_1), color=black, surface=s
        )
        pg.draw.circle(
            center=(x1_1, y1_1), radius=(m1_1 * 0.1), color=black, surface=s
        )
        pg.draw.line(
            start_pos=(x1_1, y1_1), end_pos=(x2_1, y2_1), color=black, surface=s
        )
        pg.draw.circle(
            center=(x2_1, y2_1), radius=(m2_1 * 0.1), color=black, surface=s
        )
        
        # Double Pendulum 2
        pg.draw.line(
            start_pos=(30, 250), end_pos=(470, 250), color=black, surface=s
        )
        pg.draw.line(
            start_pos=(250, 250), end_pos=(x1_2, y1_2), color=black, surface=s
        )
        pg.draw.circle(
            center=(x1_2, y1_2), radius=(m1_2 * 0.1), color=blue, surface=s
        )
        pg.draw.line(
            start_pos=(x1_2, y1_2), end_pos=(x2_2, y2_2), color=black, surface=s
        )
        pg.draw.circle(
            center=(x2_2, y2_2), radius=(m2_2 * 0.1), color=blue, surface=s
        )
        
        # Double Pendulum 3 
        pg.draw.line(
            start_pos=(30, 250), end_pos=(470, 250), color=black, surface=s
        )
        pg.draw.line(
            start_pos=(250, 250), end_pos=(x1_3, y1_3), color=black, surface=s
        )
        pg.draw.circle(
            center=(x1_3, y1_3), radius=(m1_3 * 0.1), color=red, surface=s
        )
        pg.draw.line(
            start_pos=(x1_3, y1_3), end_pos=(x2_3, y2_3), color=black, surface=s
        )
        pg.draw.circle(
            center=(x2_3, y2_3), radius=(m2_3 * 0.1), color=red, surface=s
        )
        # Physics of 1
        a1_1 = ((-g * (2 * m1_1 + m2_1) * math.sin(thetha1_1)) - (m2_1 * g * math.sin(thetha1_1-(2*thetha2_1))) - (2 * math.sin(thetha1_1-thetha2_1) * m2_1 * ((v2_1 ** 2 * l2_1) + (v1_1 * l1_1 * math.cos(thetha1_1-thetha2_1))))) / (l1_1 * (2 * l1_1 + m2_1 - (m2_1 * math.cos(2 * thetha1_1 - 2 * thetha2_1))))
        v1_1 = v1_1 + (a1_1 * dt)
        thetha1_1 = thetha1_1 + (v1_1 * dt)
        
        a2_1 = ((2 * math.sin(thetha1_1-thetha2_1)) * (((v1_1**2 * l1_1 * (m1_1 + m2_1))) + ((g * (m1_1 + m2_1) * math.cos(thetha1_1))) + ((v2_1 ** 2 * l2_1 * m2_1 * math.cos(thetha1_1 - thetha2_1))))) / (l2_1 * (2 * m1_1 + m2_1 -(m2_1 * math.cos(2 * thetha1_1 - 2 * thetha2_1))))
        v2_1 = v2_1 + (a2_1 * dt)
        thetha2_1 = thetha2_1 + (v2_1 * dt)
        
        # Physics of 2
        a1_2 = ((-g * (2 * m1_2 + m2_2) * math.sin(thetha1_2)) - (m2_2 * g * math.sin(thetha1_2-(2*thetha2_2))) - (2 * math.sin(thetha1_2-thetha2_2) * m2_2 * ((v2_2 ** 2 * l2_2) + (v1_2 * l1_2 * math.cos(thetha1_2-thetha2_2))))) / (l1_2 * (2 * l1_2 + m2_2 - (m2_2 * math.cos(2 * thetha1_2 - 2 * thetha2_2))))
        v1_2 = v1_2 + (a1_2 * dt)
        thetha1_2 = thetha1_2 + (v1_2 * dt)
        
        a2_2 = ((2 * math.sin(thetha1_2-thetha2_2)) * (((v1_2**2 * l1_2 * (m1_2 + m2_2))) + ((g * (m1_2 + m2_2) * math.cos(thetha1_2))) + ((v2_2 ** 2 * l2_2 * m2_2 * math.cos(thetha1_2 - thetha2_2))))) / (l2_2 * (2 * m1_2 + m2_2 -(m2_2 * math.cos(2 * thetha1_2 - 2 * thetha2_2))))
        v2_2 = v2_2 + (a2_2 * dt)
        thetha2_2 = thetha2_2 + (v2_2 * dt)
        
        # Physics of 3
        a1_3 = ((-g * (2 * m1_3 + m2_3) * math.sin(thetha1_3)) - (m2_3 * g * math.sin(thetha1_3-(2*thetha2_3))) - (2 * math.sin(thetha1_3-thetha2_3) * m2_3 * ((v2_3 ** 2 * l2_3) + (v1_3 * l1_3 * math.cos(thetha1_3-thetha2_3))))) / (l1_3 * (2 * l1_3 + m2_3 - (m2_3 * math.cos(2 * thetha1_3 - 2 * thetha2_3))))
        v1_3 = v1_3 + (a1_3 * dt)
        thetha1_3 = thetha1_3 + (v1_3 * dt)

        a2_3 = ((2 * math.sin(thetha1_3-thetha2_3)) * (((v1_3**2 * l1_3 * (m1_3 + m2_3))) + ((g * (m1_3 + m2_3) * math.cos(thetha1_3))) + ((v2_3 ** 2 * l2_3 * m2_3 * math.cos(thetha1_3 - thetha2_3))))) / (l2_3 * (2 * m1_3 + m2_3 -(m2_3 * math.cos(2 * thetha1_3 - 2 * thetha2_3))))
        v2_3 = v2_3 + (a2_3 * dt)
        thetha2_3 = thetha2_3 + (v2_3 * dt)
        
        #sleep and update screen for smooth fps
        pg.time.wait(1)
        pg.display.update()      

#execute main function        
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()