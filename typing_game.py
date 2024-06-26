import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 屏幕尺寸
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 设置屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('打字练习游戏')

# 设置字体
font = pygame.font.Font(None, 74)

# 随机词列表
words = ["hello", "world", "python", "game", "pygame", "raspberry", "pi", "keyboard", "screen", "black", "white"]

# 初始设置
current_word = random.choice(words)
typed_word = ''
clock = pygame.time.Clock()
score = 0
timer = 60  # 游戏时间 60 秒

def draw_text(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    line_spacing = -2

    # get the height of the font
    font_height = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + font_height > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += font_height + line_spacing

        # remove the text we just blitted
        text = text[i:]

    return text

def display_message(message):
    screen.fill(BLACK)
    draw_text(screen, message, WHITE, (20, 250, SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40), font)
    pygame.display.flip()
    pygame.time.wait(2000)

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.unicode.isalpha():
                typed_word += event.unicode
                if current_word.startswith(typed_word):
                    if current_word == typed_word:
                        score += 1
                        current_word = random.choice(words)
                        typed_word = ''
                else:
                    display_message("错了! 再试一次.")
                    typed_word = ''

    # 更新屏幕
    screen.fill(BLACK)
    draw_text(screen, "得分: " + str(score), WHITE, (20, 10, 200, 50), font)
    draw_text(screen, current_word, WHITE, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 50), font)
    draw_text(screen, typed_word, WHITE, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50), font)

    pygame.display.flip()
    clock.tick(30)

    # 减少计时器
    timer -= 1 / 30
    if timer <= 0:
        running = False

display_message("时间到! 你的得分是: " + str(score))
pygame.quit()
sys.exit()
