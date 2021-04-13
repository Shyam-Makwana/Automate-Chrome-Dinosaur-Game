from Button import button_clicked

def is_collision(data):

    # Check collison for birds
    for i in range(250,300):
        for j in range(410,563):
            if data[i, j] < 100:
                button_clicked("down")
                return
                
    # Check collison for cactus
    for i in range(275,325):
        for j in range(563,650):
            if data[i, j] < 100:
                button_clicked("up")
                return
    return    