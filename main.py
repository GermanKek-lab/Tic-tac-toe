# подключаем билиотеки
import pygame
import sys
from time import sleep

# функция для проверки выиграша
def check_win(mas, sign):
  zeroes = 0
  for row in mas:
    zeroes += row.count(0)
    if row.count(sign)==3:
      return sign
  for col in range(3):
    if mas[0][col]==sign and mas[1][col]==sign and mas[2][col]==sign:
      return sign
  if mas[0][0]==sign and mas[1][1]==sign and mas[2][2] == sign:
    return sign
  if mas[0][2]==sign and mas[1][1]==sign and mas[2][0] == sign:
    return sign
  if zeroes == 0:
    return 'Piece'
  return False

pygame.init()
# задаём размеры
size_block = 100
margin = 15
width = height = size_block*3 + margin*4

# создаём окно игры
size_window = (width,height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики-нолики")

# цвета
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

mas = [[0]*3 for i in range(3)]
win_O = 0
win_X = 0
query = 0

game_moment = True

# цикл игры
while True:
  # просматриваем действи пользователя
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    elif event.type == pygame.MOUSEBUTTONDOWN and game_moment:
      x_mouse, y_mouse = pygame.mouse.get_pos()
      col = x_mouse // (size_block + margin)
      row = y_mouse // (size_block + margin)
      try:
        if mas[row][col] == 0:
          if query % 2 == 0:
            mas[row][col] = 'o'
            query += 1
          else:
            mas[row][col] = 'x'
            query += 1
      except:
        pass
    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN and not(game_moment):
      game_over = False
      mas = [[0]*3 for i in range(3)]
      query = 0
      screen.fill(black)
      
      game_moment = True
    else:
      pass
  
  # рисуем поле
  for row in range(3):
    for col in range(3):
      if mas[row][col] == 'x':
        color = red
      elif mas[row][col] == 'o':
        color = green
        
      else:
        color = white
      x = col*size_block + (col + 1) * margin
      y = row * size_block + (row + 1) * margin
      pygame.draw.rect(screen, color, (x, y, size_block, size_block))
      if color == red:
        pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 3)
        pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 3)
      elif color == green:
        pygame.draw.circle(screen, white, (x + size_block//2, y + size_block//2), size_block//2 - 3, 3)
  # проверка выйграша
  if (query-1) % 2 == 0:
      game_over = check_win(mas, 'o')
  else:
      game_over = check_win(mas, 'x')
  
  # окно окончание
  if game_over:
    if game_over == 'x' and game_moment:
      win_X += 1
    elif game_over == 'o' and game_moment:
      win_O += 1

    X_O_text = str(win_O) + ' : ' + str(win_X) 
    word = 'Нажмите ПРОБЕЛ для продолжения'
    screen.fill(black)

    font = pygame.font.SysFont('stxingkai', 80)
    font1 = pygame.font.SysFont('stxingkai', 20)

    text1 = font.render(game_over, True, white)
    text2 = font1.render(word, True, white)
    text3 = font.render(X_O_text, True, white)
    text_rect = text1.get_rect()
    text_rect1 = text2.get_rect()
    text_rect2 = text3.get_rect()
    
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    text_x1 = (screen.get_width() / 2 - text_rect1.width / 2)
    text_y1 = (screen.get_height() / 2 - text_rect1.height / 2) + 60
    text_x2 = screen.get_width() / 2 - text_rect2.width / 2
    text_y2 = screen.get_height() / 2 - text_rect2.height / 2
    
    if game_moment:
      screen.blit(text1, (text_x, text_y))
      pygame.display.update()
    sleep(1)
    screen.fill(black)
    screen.blit(text2, (text_x1, text_y1))
    screen.blit(text3, (text_x2, text_y2))
    
    game_moment = False

  pygame.display.update() # метод для обновления дисплея
  