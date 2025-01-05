import pygame, random, copy, word_list


pygame.init()

conjug_list = word_list.get_conjug_list("Indicativo", "Presente")
len_indexes = []
length = 1

conjug_list.sort(key=len)
for i in range (len(conjug_list)):
    if len(conjug_list[i]) > length:
        length += 1
        len_indexes.append(i)
len_indexes.append(len(conjug_list))
# print(len_indexes)

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Typing Racer in Python!")
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
timer = pygame.time.Clock()
fps = 60

#game variables
level = 0
active_string = "test string"
score = 0
high_score = 1
lives = 5
paused = False
submit = ""
word_objects = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ñ','á','é','í','ó','ú','ü']
new_level = True
# 2 - 8 level
choices = [False, True, False, False, False, False, False]
#TODO: load assets
header_font = pygame.font.Font("assets/fonts/square.ttf", 50)
button_font = pygame.font.Font("assets/fonts/1up.ttf", 38)
banner_font = pygame.font.Font("assets/fonts/1up.ttf", 28)
font = pygame.font.Font("assets/fonts/AldotheApache.ttf", 48)


class Word:
    def __init__(self, text, speed, y_pos, x_pos, ):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.speed = speed

    def draw(self):
        color = "black"
        screen.blit(font.render(self.text, True, color), (self.x_pos, self.y_pos))
        act_len = len(active_string)
        if active_string == self.text[:act_len]:
            screen.blit(font.render(active_string, True, 'green'), (self.x_pos, self.y_pos))

    def update(self):
        self.x_pos -= self.speed


class Button:
    def __init__(self, x_pos, y_pos, text, clicked, surf):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.clicked = clicked
        self.surf = surf


    def draw(self):
        circle = pygame.draw.circle(self.surf, (45, 89, 135), (self.x_pos, self.y_pos), 35)
        if circle.collidepoint(pygame.mouse.get_pos()):
            btns = pygame.mouse.get_pressed()
            if btns[0]:
                pygame.draw.circle(self.surf, (190, 35, 35), (self.x_pos, self.y_pos), 35)
                self.clicked = True
            else:
                pygame.draw.circle(self.surf, (190, 89, 135), (self.x_pos, self.y_pos), 35)
        pygame.draw.circle(self.surf, "white", (self.x_pos, self.y_pos), 35, 3)
        self.surf.blit(button_font.render(self.text, True, "white"), (self.x_pos - 15.5, self.y_pos - 27))


def draw_screen():
    # screen outlines for background shapes and title bar areas
    # pygame draw pic one on top of the other
    pygame.draw.rect(screen, (32, 42, 68), [0, HEIGHT - 100, WIDTH, 100], 0)
    pygame.draw.rect(screen, "white", [0, 0, WIDTH, HEIGHT], 5)
    pygame.draw.line(screen, "white", (250, HEIGHT - 100), (250, HEIGHT), 2)
    pygame.draw.line(screen, "white", (700, HEIGHT - 100), (700, HEIGHT), 2)
    pygame.draw.line(screen, "white", (0, HEIGHT - 100), (WIDTH, HEIGHT - 100), 2)
    pygame.draw.rect(screen, "black", [0, 0, WIDTH, HEIGHT], 2)

    # text for showing the current level, player's current input, high score, score, lives and pause
    screen.blit(header_font.render(f"Level: {level}", True, "white"), (10, HEIGHT - 75))
    screen.blit(header_font.render(f"{active_string}", True, "white"), (270, HEIGHT - 75))
    # TODO: put pause button here
    pause_btn = Button(748, HEIGHT -52, "II", False, screen)
    pause_btn.draw()
    screen.blit(banner_font.render(f"Score: {score}", True, "black"), (260, 10))
    screen.blit(banner_font.render(f"Best: {high_score}", True, "black"), (525, 10))
    screen.blit(banner_font.render(f"Lives: {lives}", True, "black"), (10, 10))
    return pause_btn.clicked


def draw_pause():
    pass

def check_answer(scor):
    for word in word_objects:
        if word.text == submit:
            points = word.speed * len(word.text) * 10 * (len(word.text) / 4)
            scor += int(points)
            word_objects.remove(word)

    return scor


def generate_level():
    word_objs = []
    include = []
    vertical_spacing = (HEIGHT - 250)
    if True not in choices:
        choices[0] = True
    for i in range(len(choices)):
        if choices[i]:
            include.append((len_indexes[i], len_indexes[i+1]))
    for i in range(level):
        speed = random.randint(2, 3)
        y_pos = random.randint(10 + (i * vertical_spacing), (i + 1) * vertical_spacing)
        x_pos = random.randint(WIDTH, WIDTH + 500)
        ind_sel = random.choice(include)
        index = random.randint(ind_sel[0], ind_sel[1])
        text = conjug_list[index].lower()
        new_word = Word(text, speed, y_pos, x_pos)
        word_objs.append(new_word) 
    return word_objs


run = True
while run:
    screen.fill("gray")
    timer.tick(fps)
    # draw background screen stuff and statuses and get pause button status
    pause_btn = draw_screen()
    if paused:
        draw_pause()
    if new_level and not paused:
        word_objects = generate_level()
        new_level = False
    else:
        for w in word_objects:
            w.draw()
            if not paused:
                w.update()
            if w.x_pos < - 200:
                word_objects.remove(w)
                lives -= 1
    if len(word_objects) <= 0 and not paused:
        level += 1
        new_level = True

    if submit != "":
        init = score
        socre = check_answer(score)
        submit = ""
        if init == score:
            # wrong entry sound
            pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if not paused:
                if event.unicode.lower() in letters:
                    active_string += event.unicode.lower()
                if event.key == pygame.K_BACKSPACE and len(active_string) > 0:
                    active_string = active_string[:-1]
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    submit = active_string
                    active_string = " "

    pygame.display.flip()
pygame.quit()