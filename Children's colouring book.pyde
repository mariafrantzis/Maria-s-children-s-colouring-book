# Variable to track whether we're on the first, second, or other pages
current_page = 1
selected_option = ""  # To track the user's quiz choice

def setup():
    size(700, 500)
    textSize(40)
    textAlign(CENTER, CENTER)

def draw():
    global current_page
    
    if current_page == 1:
        # Page 1: Display the title with jiggling text
        colorful_background()
        jiggling_text("Children's", width / 2, height / 2 - 50)
        jiggling_text("Colouring Book", width / 2, height / 2 + 50)
        draw_arrow()  # Draw arrow to next page
    
    elif current_page == 2:
        # Page 2: Quiz page with text options
        background(255)  # White background for the second page
        fill(0)
        textSize(60)
        text("Pick your image", width / 2, 100)
        
        # Display the quiz options
        textSize(40)
        text("1. House", width / 2, 200)
        text("2. Dog", width / 2, 300)
        text("3. Pumpkin", width / 2, 400)
        
        draw_backward_arrow()  # Draw back arrow
    
    elif current_page == 3:
        # Page 3: Display the house drawing
        draw_house()
        draw_backward_arrow()  # Draw back arrow
    
    elif current_page == 4:
        # Page 4: Display the pumpkin drawing
        draw_pumpkin()
        draw_backward_arrow()  # Draw back arrow
    
    elif current_page == 5:
        # Page 5: Display the dog drawing
        draw_dog()
        draw_backward_arrow()  # Draw back arrow

def colorful_background():
    for y in range(height):
        r = map(y, 0, height, 255, 50)
        g = map(y, 0, height, 100, 255)
        b = map(y, 0, height, 150, 200)
        stroke(r, g, b)
        line(0, y, width, y)

def jiggling_text(message, x, y):
    t = millis() / 500.0
    for i, letter in enumerate(message):
        x_offset = x - (len(message) * 22) + i * 45
        y_offset = y + sin(t + i) * 10
        fill(0)
        text(letter, x_offset, y_offset)

# Draw a simple forward arrow button at the bottom right of the page
def draw_arrow():
    fill(0)  # Black arrow
    noStroke()
    triangle(width - 50, height - 50, width - 30, height - 30, width - 50, height - 10)

# Draw a simple backward arrow button at the bottom left of the page
def draw_backward_arrow():
    fill(0)  # Black arrow
    noStroke()
    triangle(50, height - 50, 30, height - 30, 50, height - 10)

def mousePressed():
    global current_page, selected_option
    # Check if the forward arrow is clicked on page 1
    if current_page == 1 and mouseX > width - 50 and mouseX < width - 30 and mouseY > height - 50 and mouseY < height - 10:
        current_page = 2  # Go to next page
    
    # Check for quiz options on page 2
    elif current_page == 2:
        if mouseY > 175 and mouseY < 225:  # Option 1: House
            selected_option = "House"
            current_page = 3  # Go to house page
        elif mouseY > 275 and mouseY < 325:  # Option 2: Dog
            selected_option = "Dog"
            current_page = 5  # Go to dog page
        elif mouseY > 375 and mouseY < 425:  # Option 3: Pumpkin
            selected_option = "Pumpkin"
            current_page = 4  # Go to pumpkin page
    
    # Check if the backward arrow is clicked to go back to the previous page
    if mouseX > 30 and mouseX < 50 and mouseY > height - 50 and mouseY < height - 10:
        if current_page == 2:
            current_page = 1  # Go back to page 1
        elif current_page in [3, 4, 5]:
            current_page = 2  # Go back to quiz page

# Function to draw a simple house
def draw_house():
    background(255)  # White background
    
    stroke(0)  # Black outline
    noFill()  # No fill for the shapes
    
    # Draw the ground
    rect(0, 350, 800, 100)  # Rectangle for the ground
    
    # Draw the house body
    rect(250, 200, 150, 150)  # Rectangle for the house body
    
    # Draw the roof
    triangle(225, 200, 415, 200, 320, 125)  # Triangle for the roof
    
    # Draw the door
    rect(310, 275, 30, 75)  # Rectangle for the door
    
    # Draw windows
    rect(270, 220, 30, 30)  # Left window
    rect(350, 220, 30, 30)  # Right window

    # Draw the sun
    ellipse(100, 100, 80, 80)  # Sun
    
    # Draw a simple tree
    rect(450, 250, 20, 100)  # Tree trunk
    ellipse(460, 210, 80, 80)  # Tree leaves

# Function to draw a pumpkin
def draw_pumpkin():
    background(255)  # White background
    stroke(0)  # Black outline
    noFill()  # No fill for the shapes
    
    # Stem
    strokeWeight(10)
    line(width / 2, height / 4, width * 0.6, height * 0.15)
    
    # Pumpkin body
    strokeWeight(2)
    for i in range(6):
        ellipse(width / 2, height / 2, width * (0.75 - i * 0.125), height / 2)
    
    # Eyes
    triangle(width * 0.4, height * 0.35, width * 0.35, height * 0.45, width * 0.45, height * 0.45)
    triangle(width * 0.6, height * 0.35, width * 0.55, height * 0.45, width * 0.65, height * 0.45)
    
    # Mouth
    arc(width * 0.5, height * 0.65, width * 0.4, height * 0.2, 3.14, 2 * 3.14)
    line(width * 0.3, height * 0.65, width * 0.7, height * 0.65)

    noLoop()

# Function to draw a simple dog
def draw_dog():
    background(255)  # White background
    
    stroke(0)  # Black outline
    noFill()  # No fill for the shapes
    
    # Dog body
    ellipse(200, 260, 180, 100)  # Body
    
    # Dog head
    ellipse(200, 170, 100, 80)  # Head

    # Dog ears
    ellipse(160, 115, 30, 50)  # Left ear
    ellipse(240, 115, 30, 50)  # Right ear

    # Dog eyes
    ellipse(180, 160, 15, 15)  # Left eye
    ellipse(220, 160, 15, 15)  # Right eye
    
    # Dog nose
    ellipse(200, 180, 15, 10)  # Nose
    
    # Dog mouth
    noFill()
    arc(200, 190, 30, 20, 0, PI)  # Smile
    
    # Dog legs
    rect(150, 310, 20, 40)  # Left front leg
    rect(230, 310, 20, 40)  # Right front leg
    rect(170, 310, 20, 40)  # Left back leg
    rect(210, 310, 20, 40)  # Right back leg

    # Dog tail
    strokeWeight(8)
    line(280, 240, 320, 220)  # Tail
