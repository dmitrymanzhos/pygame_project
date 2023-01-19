import os
import sys
import pygame

pygame.init()
size = WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
all_sprites = pygame.sprite.Group()


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip().split('|') for line in mapFile]
    return level_map


def try_again():
    screen.fill((0, 0, 0))


def success():
    pass


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, x, y):
        if x < self.left or y < self.top:
            return None

        elif x > self.cell_size * self.width + self.left or y > self.cell_size * self.height + self.top:
            return None

        else:
            for i in range(self.height):
                for j in range(self.width):
                    if self.cell_size * j + self.left <= x <= self.cell_size * (j + 1) + self.left:
                        if self.cell_size * i + self.top <= y <= self.cell_size * (i + 1) + self.top:
                            return j, i

            for i in range(self.height):
                for j in range(self.width):
                    if self.cell_size * j + self.left <= x <= self.cell_size * (j + 1) + self.left:
                        if self.cell_size * i + self.top <= y <= self.cell_size * (i + 1) + self.top:
                            return j, i

    def find_distanse(self, cell, x, y):
        return ((self.cell_size * (cell[0] + 0.5) - x) ** 2 + (self.cell_size * (cell[1] + 0.5) - y) ** 2) ** 0.5


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 250, 300, 100), width=3)
    font = pygame.font.Font(None, 70)
    text1 = font.render('Начать', True, (150, 150, 150))
    screen.blit(text1, (410, 280))
    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 360, 300, 100), width=3)
    text2 = font.render('Правила', True, (150, 150, 150))
    screen.blit(text2, (390, 390))
    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 470, 300, 100), width=3)
    font1 = pygame.font.Font(None, 59)
    text3 = font1.render('Выбор уровня', True, (150, 150, 150))
    screen.blit(text3, (358, 500))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if 650 >= x >= 350 >= y >= 250:
                    pygame.draw.rect(screen, pygame.Color((250, 250, 250)), (350, 250, 300, 100), width=3)
                    new_text1 = font.render('Начать', True, (250, 250, 250))
                    screen.blit(new_text1, (410, 280))
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 360, 300, 100), width=3)
                    screen.blit(text2, (390, 390))
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 470, 300, 100), width=3)
                    screen.blit(text3, (358, 500))
                elif 350 <= x <= 650 and 360 <= y <= 460:
                    pygame.draw.rect(screen, pygame.Color((250, 250, 250)), (350, 360, 300, 100), width=3)
                    new_text2 = font.render('Правила', True, (250, 250, 250))
                    screen.blit(new_text2, (390, 390))
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 250, 300, 100), width=3)
                    screen.blit(text1, (410, 280))
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 470, 300, 100), width=3)
                    screen.blit(text3, (358, 500))
                elif 350 <= x <= 650 and 470 <= y <= 570:
                    pygame.draw.rect(screen, pygame.Color((250, 250, 250)), (350, 470, 300, 100), width=3)
                    new_text3 = font1.render('Выбор уровня', True, (250, 250, 250))
                    screen.blit(new_text3, (358, 500))
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 250, 300, 100), width=3)
                    screen.blit(text1, (410, 280))
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 360, 300, 100), width=3)
                    screen.blit(text2, (390, 390))
                else:
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 250, 300, 100), width=3)
                    screen.blit(text1, (410, 280))
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 360, 300, 100), width=3)
                    screen.blit(text2, (390, 390))
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 470, 300, 100), width=3)
                    screen.blit(text3, (358, 500))

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 650 >= x >= 350 >= y >= 250:
                    return start()
                elif 350 <= x <= 650 and 360 <= y <= 460:
                    return rules()
                elif 350 <= x <= 650 and 470 <= y <= 570:
                    return choose_level()
        pygame.display.flip()
        clock.tick(FPS)


def start(lvl_num=1):
    if lvl_num == 1:
        level = Level('level1.txt', 500, 350, None)
        print(level.board)
        print(level.player.rect)
        level.play(screen)


def rules():
    intro_text = ["ПРАВИЛА ИГРЫ", "",
                  "Вы находитесь в лабиринте. Цель игры - найти выход, собрав как можно больше монет.",
                  "",
                  ""]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (850, 10, 140, 50), width=3)
    text = font.render('Назад', True, (150, 150, 150))
    screen.blit(text, (890, 27))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if 850 <= x <= 990 and 10 <= y <= 60:
                    pygame.draw.rect(screen, pygame.Color((250, 250, 250)), (850, 10, 140, 50), width=3)
                    new_text = font.render('Назад', True, (250, 250, 250))
                    screen.blit(new_text, (890, 27))
                else:
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (850, 10, 140, 50), width=3)
                    screen.blit(text, (890, 27))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 850 <= x <= 990 and 10 <= y <= 60:
                    return start_screen()
        pygame.display.flip()
        clock.tick(FPS)


def choose_level():
    pass


# class Tile(pygame.sprite.Sprite):
#     def __init__(self, tile_type, pos_x, pos_y):
#         super().__init__(tiles_group, all_sprites)
#         self.image = tile_images[tile_type]
#         self.rect = self.image.get_rect().move(
#             tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.v = 2
        self.frames = []
        self.cut_sheet(pygame.transform.scale(load_image('player1.png', colorkey=-1), (300, 400)), 3, 4)
        self.cur_frame = 1
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (20, 20))
        self.rect = self.rect.move(100, 100)
        self.rect.x, self.rect.y = pos_x, pos_y

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.image = pygame.transform.scale(self.image, (20, 20))


class Camera:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


class Coin:
    pass


class Level(Board):
    def __init__(self, filename, start_x, start_y, time):
        self.board = load_level(filename)
        self.player = Player(start_x, start_y)
        self.player.rect = self.player.image.get_rect()
        self.camera = Camera(start_x, start_y)
        self.time = time
        super().__init__(len(self.board[0]), len(self.board))
        self.board = load_level(filename)
        self.rad = 100
        self.al = []
        print(self.board)

    def check_if_available(self, side):
        self.player.cell = self.get_cell(self.player.rect.x + 0.5 * self.player.rect.w,
                                         self.player.rect.y + 0.5 * self.player.rect.h)
        if self.player.cell:
            if self.player.cell[1] != 0 or self.player.cell[1] != len(self.board):
                for el in self.al:
                    if side == '8':
                        if '8' in self.board[self.player.cell[1]][self.player.cell[0]]:
                            if self.player.rect.y == self.player.cell[1] * self.cell_size + self.top:
                                return False
                        if self.player.rect.y == el[3]:
                            if self.player.rect.x < el[0] == el[2] < self.player.rect.x + self.player.rect.w:
                                return False
                            elif el[0] < self.player.rect.x < el[2] or \
                                    el[0] < self.player.rect.x + self.player.rect.w < el[2]:
                                return False

                    if side == '4':
                        if '4' in self.board[self.player.cell[1]][self.player.cell[0]]:
                            if self.player.rect.x == self.player.cell[0] * self.cell_size + self.left:
                                return False
                        if self.player.rect.x == el[2]:
                            if self.player.rect.y < el[1] == el[3] < self.player.rect.y + self.player.rect.h:
                                return False
                            elif el[1] < self.player.rect.y < el[3] or \
                                    el[1] < self.player.rect.y + self.player.rect.h < el[3]:
                                return False

                    if side == '2':
                        if '2' in self.board[self.player.cell[1]][self.player.cell[0]]:
                            if self.player.rect.y + self.player.rect.h == \
                                    (self.player.cell[1] + 1) * self.cell_size + self.top:
                                return False
                        if self.player.rect.y + self.player.rect.h == el[1]:
                            if self.player.rect.x < el[0] == el[2] < self.player.rect.x + self.player.rect.w:
                                return False
                            elif el[0] < self.player.rect.x < el[2] or \
                                    el[0] < self.player.rect.x + self.player.rect.w < el[2]:
                                return False

                    if side == '6':
                        if '6' in self.board[self.player.cell[1]][self.player.cell[0]]:
                            if self.player.rect.x + self.player.rect.w == \
                                    (self.player.cell[0] + 1) * self.cell_size + self.left:
                                return False
                            else:
                                return True
                        if self.player.rect.x + self.player.rect.w == el[0]:
                            if self.player.rect.y < el[1] == el[3] < self.player.rect.y + self.player.rect.h:
                                return False
                            elif el[1] < self.player.rect.y < el[3] or \
                                    el[1] < self.player.rect.y + self.player.rect.h < el[3]:
                                return False
        return True

    def play(self, screen):
        self.screen = screen
        self.player.cell = self.get_cell(self.player.rect.x + 0.5 * self.player.rect.w,
                                         self.player.rect.y + 0.5 * self.player.rect.h)
        all_sprites.add(self.player)
        print(self.player.cell)
        print('started')
        running = True
        w_pushed = False
        a_pushed = False
        s_pushed = False
        d_pushed = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(self.al)
                    terminate()
                elif event.type == pygame.MOUSEMOTION:
                    pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        w_pushed = True
                    elif event.key == pygame.K_a:
                        a_pushed = True
                    elif event.key == pygame.K_s:
                        s_pushed = True
                    elif event.key == pygame.K_d:
                        d_pushed = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        w_pushed = False
                    elif event.key == pygame.K_a:
                        a_pushed = False
                    elif event.key == pygame.K_s:
                        s_pushed = False
                    elif event.key == pygame.K_d:
                        d_pushed = False

            if w_pushed:
                if self.check_if_available('8'):
                    self.player.rect.y -= self.player.v
                    self.player.image = self.player.frames[10]
                    self.player.update()
            if a_pushed:
                if self.check_if_available('4'):
                    self.player.rect.x -= self.player.v
                    self.player.image = self.player.frames[4]
                    self.player.update()
            if s_pushed:
                if self.check_if_available('2'):
                    self.player.rect.y += self.player.v
                    self.player.image = self.player.frames[1]
                    self.player.update()
            if d_pushed:
                if self.check_if_available('6'):
                    self.player.rect.x += self.player.v
                    self.player.image = self.player.frames[7]
                    self.player.update()

            self.player.cell = self.get_cell(self.player.rect.x + 0.5 * self.player.rect.w,
                                             self.player.rect.y + 0.5 * self.player.rect.h)

            fl = pygame.transform.scale(load_image('floor1.png'), (self.cell_size, self.cell_size))
            self.screen.fill(pygame.Color(0, 0, 0))
            for i in range(len(self.board[0])):
                for j in range(len(self.board)):
                    if self.find_distanse((i, j), self.player.rect.x + 0.5 * self.player.rect.w,
                                          self.player.rect.y + 0.5 * self.player.rect.h) <= self.rad:
                        self.screen.blit(fl, (self.cell_size * i + self.left, self.cell_size * j + self.top))

            for i in range(len(self.board[0])):
                for j in range(len(self.board)):
                    if self.find_distanse((i, j), self.player.rect.x + 0.5 * self.player.rect.w,
                                          self.player.rect.y + 0.5 * self.player.rect.h) <= self.rad:
                        if '2' in self.board[j][i]:
                            pygame.draw.line(self.screen, pygame.Color((250, 50, 250)),
                                             (self.cell_size * i + self.left, self.cell_size * (j + 1) + self.top),
                                             (self.cell_size * (i + 1) + self.left,
                                              self.cell_size * (j + 1) + self.top),
                                             width=3)
                            if (self.cell_size * i + self.left, self.cell_size * (j + 1) + self.top,
                                self.cell_size * (i + 1) + self.left,
                                self.cell_size * (j + 1) + self.top) not in self.al:
                                self.al.append((self.cell_size * i + self.left,
                                                self.cell_size * (j + 1) + self.top,
                                                self.cell_size * (i + 1) + self.left,
                                                self.cell_size * (j + 1) + self.top))

                        if '6' in self.board[j][i]:
                            pygame.draw.line(self.screen, pygame.Color((250, 50, 250)),
                                             (self.cell_size * (i + 1) + self.left, self.cell_size * j + self.top),
                                             (self.cell_size * (i + 1) + self.left,
                                              self.cell_size * (j + 1) + self.top),
                                             width=3)
                            if (self.cell_size * (i + 1) + self.left, self.cell_size * j + self.top,
                                self.cell_size * (i + 1) + self.left,
                                self.cell_size * (j + 1) + self.top) not in self.al:
                                self.al.append((self.cell_size * (i + 1) + self.left,
                                                self.cell_size * j + self.top,
                                                self.cell_size * (i + 1) + self.left,
                                                self.cell_size * (j + 1) + self.top))

                        if '4' in self.board[j][i]:
                            pygame.draw.line(self.screen, pygame.Color((250, 50, 250)),
                                             (self.cell_size * i + self.left, self.cell_size * j + self.top),
                                             (self.cell_size * i + self.left, self.cell_size * (j + 1) + self.top),
                                             width=3)
                            if (self.cell_size * i + self.left, self.cell_size * j + self.top,
                                self.cell_size * i + self.left, self.cell_size * (j + 1) + self.top) not in self.al:
                                self.al.append((self.cell_size * i + self.left, self.cell_size * j + self.top,
                                                self.cell_size * i + self.left, self.cell_size * (j + 1) + self.top))

                        if '8' in self.board[j][i]:
                            pygame.draw.line(self.screen, pygame.Color((250, 50, 250)),
                                             (self.cell_size * i + self.left, self.cell_size * j + self.top),
                                             (self.cell_size * (i + 1) + self.left, self.cell_size * j + self.top),
                                             width=3)
                            if (self.cell_size * i + self.left, self.cell_size * j + self.top,
                                self.cell_size * (i + 1) + self.left, self.cell_size * j + self.top) not in self.al:
                                self.al.append((self.cell_size * i + self.left, self.cell_size * j + self.top,
                                                self.cell_size * (i + 1) + self.left, self.cell_size * j + self.top))

            all_sprites.draw(self.screen)

            pygame.display.flip()
            clock.tick(FPS)


start_screen()
