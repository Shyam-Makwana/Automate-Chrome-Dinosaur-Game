from PIL import Image, ImageGrab # pip install pillow

def draw_shape(image):

    data = image.load() 

    # Draw the rectangle for birds
    for i in range(250,300):
        for j in range(410,563):
            data[i, j] = 255

    # Draw the rectangle for cactus
    for i in range(275,325):
        for j in range(563,650):
            data[i, j] = 0
        
    image.show()