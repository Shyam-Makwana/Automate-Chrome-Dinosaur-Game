from PIL import Image, ImageGrab # pip install pillow

import time
from Button import button_clicked
from Collision import is_collision
from ShowShape import draw_shape

if __name__ == "__main__":

    time.sleep(3)
    button_clicked('up') 
    
    while True:

        image = ImageGrab.grab().convert('L')  
        
        # draw_shape(image)
        # break

        data = image.load() 

        is_collision(data)

        