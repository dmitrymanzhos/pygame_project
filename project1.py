import os
import pygame

pygame.init()  # начальная инициализация
size = WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
all_sprites = pygame.sprite.Group()


def terminate():  # выход
    pygame.quit()
    exit()


def load_image(name, colorkey=None):  # загрузка изображений
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):  # загрузка уровня из файла
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip().split('|') for line in mapFile]
    return level_map


def success(coins, lvl_num):  # финальное окно
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 70)
    text1 = font.render('Лабиринт пройден', True, (250, 250, 250))
    screen.blit(text1, (200, 130))
    text2 = font.render(f"Ваш результат: {coins} монет", True, (250, 250, 250))
    screen.blit(text2, (200, 200))
    text3 = font.render('Нажмите в любом месте', True, (200, 200, 200))
    screen.blit(text3, (200, 430))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start(lvl_num=lvl_num + 1)
        pygame.display.flip()


def start_screen():  # начальный экран
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
                    return start(lvl_num=1)
                elif 350 <= x <= 650 and 360 <= y <= 460:
                    return rules()
                elif 350 <= x <= 650 and 470 <= y <= 570:
                    return choose_level()
        pygame.display.flip()
        clock.tick(FPS)


def start(lvl_num=1):  # запуск уровня
    if lvl_num == 1:
        level = Level('level1.txt', 370, 470, 1)
        level.play(screen)
    elif lvl_num == 2:
        level = Level('level2.txt', 680, 780, 2)
        level.play(screen)
    else:
        return start_screen()


def rules():  # окно с правилами
    intro_text = ["ПРАВИЛА ИГРЫ", "",
                  "Вы находитесь в лабиринте. Цель игры - найти выход, собрав как можно больше монет.",
                  "Собранные кристаллы увеличивают область видимости",
                  "Управление с помощью WASD"]

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


def choose_level():  # окно выбора уровня
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 250, 300, 100), width=3)
    font = pygame.font.Font(None, 70)
    text1 = font.render('Уровень 1', True, (150, 150, 150))
    screen.blit(text1, (390, 280))
    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 360, 300, 100), width=3)
    text2 = font.render('Уровень 2', True, (150, 150, 150))
    screen.blit(text2, (390, 390))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if 650 >= x >= 350 >= y >= 250:
                    pygame.draw.rect(screen, pygame.Color((250, 250, 250)), (350, 250, 300, 100), width=3)
                    new_text1 = font.render('Уровень 1', True, (250, 250, 250))
                    screen.blit(new_text1, (390, 280))
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 360, 300, 100), width=3)
                    screen.blit(text2, (390, 390))

                elif 350 <= x <= 650 and 360 <= y <= 460:
                    pygame.draw.rect(screen, pygame.Color((250, 250, 250)), (350, 360, 300, 100), width=3)
                    new_text2 = font.render('Уровень 2', True, (250, 250, 250))
                    screen.blit(new_text2, (390, 390))
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 250, 300, 100), width=3)
                    screen.blit(text1, (390, 280))

                else:
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 250, 300, 100), width=3)
                    screen.blit(text1, (390, 280))
                    pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (350, 360, 300, 100), width=3)
                    screen.blit(text2, (390, 390))

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 650 >= x >= 350 >= y >= 250:
                    return start(lvl_num=1)
                elif 350 <= x <= 650 and 360 <= y <= 460:
                    return start(lvl_num=2)
        pygame.display.flip()
        clock.tick(FPS)


class Board:  # класс поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        self.left = 10
        self.top = 10
        self.cell_size = 100

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, x, y):  # получение клетки, в которой находится точка
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

    def find_distanse(self, cell, x, y):  # нахождение расстояния от центра клетки до точки
        return ((self.cell_size * (cell[0] + 0.5) - x) ** 2 + (self.cell_size * (cell[1] + 0.5) - y) ** 2) ** 0.5


class Player(pygame.sprite.Sprite):  # класс персонажа
    def __init__(self):
        super().__init__(all_sprites)
        self.v = 5
        self.frames = []
        self.cut_sheet(pygame.transform.scale(load_image('player1.png', colorkey=-1), (300, 400)), 3, 4)
        self.image = pygame.transform.scale(self.frames[1], (70, 70))
        self.rect = self.rect.move(100, 100)

    def cut_sheet(self, sheet, columns, rows):  # разрезание png персонажа на части
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):  # изменение размера изображения персонажа
        self.image = pygame.transform.scale(self.image, (70, 70))


class Camera:  # класс камеры
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def apply(self, obj, plus_or_min=0):  # смещение персонажа для отрисовки
        if plus_or_min == 0:
            obj.rect.x += self.dx
            obj.rect.y += self.dy
        else:
            obj.rect.x -= self.dx
            obj.rect.y -= self.dy

    def update(self, target):  # обновление смещения
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


class Level(Board):  # класс уровня
    def __init__(self, filename, start_x, start_y, lvl_num):
        all_sprites.empty()
        self.board = load_level(filename)
        self.player = Player()
        self.player.rect = self.player.image.get_rect()
        self.player.rect.x, self.player.rect.y = start_x, start_y
        self.camera = Camera(start_x, start_y)
        self.camera.update(self.player)
        self.lvl_num = lvl_num
        super().__init__(len(self.board[0]), len(self.board))
        self.board = load_level(filename)
        self.rad = 200
        self.al = []
        print(self.board)
        self.coins = 0

    def check_if_available(self, side):  # проверка возможности перемещения персонажа
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

    def play(self, screen):  # запуск уровня
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
        fl = pygame.transform.scale(load_image('floor1.png'), (self.cell_size, self.cell_size))
        cr = pygame.transform.scale(load_image('cristall.png'), (self.cell_size, self.cell_size))
        coin = pygame.transform.scale(load_image('coin.png'), (self.cell_size, self.cell_size))
        font = pygame.font.Font(None, 30)
        text = font.render('Назад', True, (150, 150, 150))
        new_text = font.render('Назад', True, (250, 250, 250))
        back_col = 0

        while running:  # основной угровой цикл
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(self.al)
                    terminate()
                elif event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    if 850 <= x <= 990 and 10 <= y <= 60:
                        back_col = 1
                        pygame.draw.rect(screen, pygame.Color((250, 250, 250)), (850, 10, 140, 50), width=3)
                        screen.blit(new_text, (890, 27))
                    else:
                        back_col = 0
                        pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (850, 10, 140, 50), width=3)
                        screen.blit(text, (890, 27))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 850 <= x <= 990 and 10 <= y <= 60:
                        return start_screen()

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
            # перемещение персонажа
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
            if self.player.cell:
                if 'cr' in self.board[self.player.cell[1]][self.player.cell[0]]:
                    self.board[self.player.cell[1]][self.player.cell[0]] = \
                        ''.join(self.board[self.player.cell[1]][self.player.cell[0]].split('cr'))
                    self.rad += 40
                if 'coin' in self.board[self.player.cell[1]][self.player.cell[0]]:
                    self.board[self.player.cell[1]][self.player.cell[0]] = \
                        ''.join(self.board[self.player.cell[1]][self.player.cell[0]].split('coin'))
                    self.coins += 1
            else:
                return success(self.coins, self.lvl_num)
            self.camera.update(self.player)
            self.screen.fill(pygame.Color(50, 50, 50))

            if back_col == 0:
                pygame.draw.rect(screen, pygame.Color((150, 150, 150)), (850, 10, 140, 50), width=3)
                screen.blit(text, (890, 27))
            elif back_col == 1:
                pygame.draw.rect(screen, pygame.Color((250, 250, 250)), (850, 10, 140, 50), width=3)
                screen.blit(new_text, (890, 27))

            for i in range(len(self.board[0])):
                for j in range(len(self.board)):
                    if self.find_distanse((i, j), self.player.rect.x + 0.5 * self.player.rect.w,
                                          self.player.rect.y + 0.5 * self.player.rect.h) <= self.rad:
                        self.screen.blit(fl, (self.cell_size * i + self.left + self.camera.dx,
                                              self.cell_size * j + self.top + self.camera.dy))
                        if 'cr' in self.board[j][i]:
                            self.screen.blit(cr, (self.cell_size * i + self.left + self.camera.dx,
                                                  self.cell_size * j + self.top + self.camera.dy))
                        elif 'coin' in self.board[j][i]:
                            self.screen.blit(coin, (self.cell_size * i + self.left + self.camera.dx,
                                                    self.cell_size * j + self.top + self.camera.dy))

            for i in range(len(self.board[0])):
                for j in range(len(self.board)):
                    if self.find_distanse((i, j), self.player.rect.x + 0.5 * self.player.rect.w,
                                          self.player.rect.y + 0.5 * self.player.rect.h) <= self.rad:
                        if '2' in self.board[j][i]:
                            pygame.draw.line(self.screen, pygame.Color((0, 50, 250)),
                                             (self.cell_size * i + self.left + self.camera.dx,
                                              self.cell_size * (j + 1) + self.top + self.camera.dy),
                                             (self.cell_size * (i + 1) + self.left + self.camera.dx,
                                              self.cell_size * (j + 1) + self.top + self.camera.dy),
                                             width=5)
                            if (self.cell_size * i + self.left, self.cell_size * (j + 1) + self.top,
                                self.cell_size * (i + 1) + self.left,
                                self.cell_size * (j + 1) + self.top) not in self.al:
                                self.al.append((self.cell_size * i + self.left,
                                                self.cell_size * (j + 1) + self.top,
                                                self.cell_size * (i + 1) + self.left,
                                                self.cell_size * (j + 1) + self.top))

                        if '6' in self.board[j][i]:
                            pygame.draw.line(self.screen, pygame.Color((0, 50, 250)),
                                             (self.cell_size * (i + 1) + self.left + self.camera.dx,
                                              self.cell_size * j + self.top + self.camera.dy),
                                             (self.cell_size * (i + 1) + self.left + self.camera.dx,
                                              self.cell_size * (j + 1) + self.top + self.camera.dy),
                                             width=5)
                            if (self.cell_size * (i + 1) + self.left, self.cell_size * j + self.top,
                                self.cell_size * (i + 1) + self.left,
                                self.cell_size * (j + 1) + self.top) not in self.al:
                                self.al.append((self.cell_size * (i + 1) + self.left,
                                                self.cell_size * j + self.top,
                                                self.cell_size * (i + 1) + self.left,
                                                self.cell_size * (j + 1) + self.top))

                        if '4' in self.board[j][i]:
                            pygame.draw.line(self.screen, pygame.Color((0, 50, 250)),
                                             (self.cell_size * i + self.left + self.camera.dx,
                                              self.cell_size * j + self.top + self.camera.dy),
                                             (self.cell_size * i + self.left + self.camera.dx,
                                              self.cell_size * (j + 1) + self.top + self.camera.dy),
                                             width=5)
                            if (self.cell_size * i + self.left, self.cell_size * j + self.top,
                                self.cell_size * i + self.left, self.cell_size * (j + 1) + self.top) not in self.al:
                                self.al.append((self.cell_size * i + self.left, self.cell_size * j + self.top,
                                                self.cell_size * i + self.left, self.cell_size * (j + 1) + self.top))

                        if '8' in self.board[j][i]:
                            pygame.draw.line(self.screen, pygame.Color((0, 50, 250)),
                                             (self.cell_size * i + self.left + self.camera.dx,
                                              self.cell_size * j + self.top + self.camera.dy),
                                             (self.cell_size * (i + 1) + self.left + self.camera.dx,
                                              self.cell_size * j + self.top + self.camera.dy),
                                             width=5)
                            if (self.cell_size * i + self.left, self.cell_size * j + self.top,
                                self.cell_size * (i + 1) + self.left, self.cell_size * j + self.top) not in self.al:
                                self.al.append((self.cell_size * i + self.left, self.cell_size * j + self.top,
                                                self.cell_size * (i + 1) + self.left, self.cell_size * j + self.top))
            self.camera.apply(self.player)
            all_sprites.draw(self.screen)
            self.camera.apply(self.player, plus_or_min=1)

            pygame.display.flip()
            clock.tick(FPS)


start_screen()
