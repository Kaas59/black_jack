# === 操作方法 ===
#
# Step1 「はじめる」をクリックしてゲームをスタート
# 
# Step2 「続けてカードを引きますか？」と表示されたら自分の手札が21を超えないように「はい」または「いいえ」をクリックする
#
# Step3 勝敗が確定したら「おわる」をクリックしてゲーム終了
#
# ※エース(A)はかならず1として扱われます
# 
# ================


# -*- coding: utf-8 -*-
import sys
import pygame
from random import shuffle


# === カラープロパティ ===
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GOLD  = (255, 216,   0)
SILVER= (192, 192, 192)
COPPER = (192, 112, 48)

# === カード画像読み込み ===
card_club = [
  pygame.image.load("img/card/card_club_01.png"),
  pygame.image.load("img/card/card_club_02.png"),
  pygame.image.load("img/card/card_club_03.png"),
  pygame.image.load("img/card/card_club_04.png"),
  pygame.image.load("img/card/card_club_05.png"),
  pygame.image.load("img/card/card_club_06.png"),
  pygame.image.load("img/card/card_club_07.png"),
  pygame.image.load("img/card/card_club_08.png"),
  pygame.image.load("img/card/card_club_09.png"),
  pygame.image.load("img/card/card_club_10.png"),
  pygame.image.load("img/card/card_club_11.png"),
  pygame.image.load("img/card/card_club_12.png"),
  pygame.image.load("img/card/card_club_13.png")
]

card_diamond = [
  pygame.image.load("img/card/card_diamond_01.png"),
  pygame.image.load("img/card/card_diamond_02.png"),
  pygame.image.load("img/card/card_diamond_03.png"),
  pygame.image.load("img/card/card_diamond_04.png"),
  pygame.image.load("img/card/card_diamond_05.png"),
  pygame.image.load("img/card/card_diamond_06.png"),
  pygame.image.load("img/card/card_diamond_07.png"),
  pygame.image.load("img/card/card_diamond_08.png"),
  pygame.image.load("img/card/card_diamond_09.png"),
  pygame.image.load("img/card/card_diamond_10.png"),
  pygame.image.load("img/card/card_diamond_11.png"),
  pygame.image.load("img/card/card_diamond_12.png"),
  pygame.image.load("img/card/card_diamond_13.png")
]

card_heart = [
  pygame.image.load("img/card/card_heart_01.png"),
  pygame.image.load("img/card/card_heart_02.png"),
  pygame.image.load("img/card/card_heart_03.png"),
  pygame.image.load("img/card/card_heart_04.png"),
  pygame.image.load("img/card/card_heart_05.png"),
  pygame.image.load("img/card/card_heart_06.png"),
  pygame.image.load("img/card/card_heart_07.png"),
  pygame.image.load("img/card/card_heart_08.png"),
  pygame.image.load("img/card/card_heart_09.png"),
  pygame.image.load("img/card/card_heart_10.png"),
  pygame.image.load("img/card/card_heart_11.png"),
  pygame.image.load("img/card/card_heart_12.png"),
  pygame.image.load("img/card/card_heart_13.png")
]

card_spade = [
  pygame.image.load("img/card/card_spade_01.png"),
  pygame.image.load("img/card/card_spade_02.png"),
  pygame.image.load("img/card/card_spade_03.png"),
  pygame.image.load("img/card/card_spade_04.png"),
  pygame.image.load("img/card/card_spade_05.png"),
  pygame.image.load("img/card/card_spade_06.png"),
  pygame.image.load("img/card/card_spade_07.png"),
  pygame.image.load("img/card/card_spade_08.png"),
  pygame.image.load("img/card/card_spade_09.png"),
  pygame.image.load("img/card/card_spade_10.png"),
  pygame.image.load("img/card/card_spade_11.png"),
  pygame.image.load("img/card/card_spade_12.png"),
  pygame.image.load("img/card/card_spade_13.png")
]

card_other = [
  pygame.image.load("img/card/card_back.png"),
  pygame.image.load("img/card/card_joker.png")
]

pygame.init()
pygame.display.set_caption("ブラックジャック")

# スクリーン
screen = pygame.display.set_mode((900, 600))

# フォント
font60 = pygame.font.Font("font/mplus-1m-medium.ttf", 60)
font50 = pygame.font.Font("font/mplus-1m-medium.ttf", 50)
font40 = pygame.font.Font("font/mplus-1m-medium.ttf", 40)
font30 = pygame.font.Font("font/mplus-1m-medium.ttf", 30)

# ボタン 設定
start_button = pygame.Rect(355, 405, 170, 45)
end_button = pygame.Rect(700, 535, 150, 45)
yes_button = pygame.Rect(305, 530, 130, 50)
no_button = pygame.Rect(455, 530, 130, 50)

# テキスト 設定
title = font60.render("ブラック　ジャック", True, SILVER)
start_text = font40.render("はじめる", True, WHITE)
end_text = font40.render("おわる", True, WHITE)
continue_text = font50.render("続けてカードを引きますか？", True, WHITE)
yes_text = font40.render("はい", True, WHITE)
no_text = font40.render("いいえ", True, WHITE)
win_text = font60.render("あなたの勝ちです！！", True, WHITE)
lose_text = font60.render("あなたの負けです。。", True, WHITE)
drow_text = font60.render("引き分けです。。", True, WHITE)

# 背景
backimage = pygame.image.load("img/black_jack_table.jpg")
backimage = pygame.transform.scale(backimage, (900, 600))

class Deck:
  def __init__(self):
    suits = ['club', 'diamond', 'heart', 'spade']
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    self.deck = []
    for i in suits:
      for j in values:
        self.deck.append([i, j])
    shuffle(self.deck)

  def draw(self):
    return self.deck.pop(0)

class Person:
  def __init__(self):
    self.hands = []
    self.point = 0

  def add(self, card):
    self.hands.append(card)

  def point_sum(self):
    self.point = 0
    for i in self.hands:
      if i[1] in [11, 12, 13]:
        self.point += 10
      else:
        self.point += i[1]
    return self.point

def base_draw():
  screen.blit(backimage, (0, 0))
  pygame.display.update()

def start_draw():
  screen.blit(title, (180,130))
  pygame.draw.rect(screen, RED, start_button)
  screen.blit(start_text, (360, 400))
  pygame.display.update()

def end_draw():
  pygame.draw.rect(screen, RED, end_button)
  screen.blit(end_text, (715, 530))
  pygame.display.update()

def draw_check():
  pygame.draw.rect(screen, RED, yes_button)
  pygame.draw.rect(screen, BLUE, no_button)
  screen.blit(continue_text, (150, 450))
  screen.blit(yes_text, (330, 530))
  screen.blit(no_text, (460, 530))

def card_front(player, dealer):
  base_draw()
  for value in range(len(dealer.hands)):
    if dealer.hands[value][0] == 'club':
      card_image = card_club[dealer.hands[value][1] - 1]
    elif dealer.hands[value][0] == 'diamond':
      card_image = card_diamond[dealer.hands[value][1] - 1]
    elif dealer.hands[value][0] == 'heart':
      card_image = card_heart[dealer.hands[value][1] - 1]
    else:
      card_image = card_spade[dealer.hands[value][1] - 1]
    card_image = pygame.transform.scale(card_image, (78, 100))
    screen.blit(card_image, (300 + 90 * value, 180))
    pygame.display.update()
  for value in range(len(player.hands)):
    if player.hands[value][0] == 'club':
      card_image = card_club[player.hands[value][1] - 1]
    elif player.hands[value][0] == 'diamond':
      card_image = card_diamond[player.hands[value][1] - 1]
    elif player.hands[value][0] == 'heart':
      card_image = card_heart[player.hands[value][1] - 1]
    else:
      card_image = card_spade[player.hands[value][1] - 1]
    card_image = pygame.transform.scale(card_image, (78, 100))
    screen.blit(card_image, (300 + 90 * value, 380))
    pygame.display.update()

def card_back(player, dealer):
  for value in range(len(dealer.hands)):
    if value == 0:
      card_image = card_other[0] 
    elif dealer.hands[value][0] == 'club':
      card_image = card_club[dealer.hands[value][1] - 1]
    elif dealer.hands[value][0] == 'diamond':
      card_image = card_diamond[dealer.hands[value][1] - 1]
    elif dealer.hands[value][0] == 'heart':
      card_image = card_heart[dealer.hands[value][1] - 1]
    else:
      card_image = card_spade[dealer.hands[value][1] - 1]
    card_image = pygame.transform.scale(card_image, (78, 100))
    screen.blit(card_image, (300 + 90 * value, 150))
    pygame.display.update()
  for value in range(len(player.hands)):
    if player.hands[value][0] == 'club':
      card_image = card_club[player.hands[value][1] - 1]
    elif player.hands[value][0] == 'diamond':
      card_image = card_diamond[player.hands[value][1] - 1]
    elif player.hands[value][0] == 'heart':
      card_image = card_heart[player.hands[value][1] - 1]
    else:
      card_image = card_spade[player.hands[value][1] - 1]
    card_image = pygame.transform.scale(card_image, (78, 100))
    screen.blit(card_image, (300 + 90 * value, 350))
    pygame.display.update()

def result(message):
  if message == 'win':
    screen.blit(win_text, (180,90))
  elif message == 'lose':
    screen.blit(lose_text, (180,90))
  else:
    screen.blit(drow_text, (180,90))
  end_draw()

def drawing(class1, class2, name):
  card = class1.draw()
  class2.add(card)


def main():
  base_draw()
  start_draw()
  end_status = False

  flag = True
  while flag:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if start_button.collidepoint(event.pos):
          flag = False
          base_draw()

  d = Deck()
  player = Person()
  dealer = Person()

  drawing(d, player, ' プレイヤー')
  drawing(d, player, ' プレイヤー')

  drawing(d, dealer, ' ディーラー')
  drawing(d, dealer, ' ディーラー')

  card_image = card_spade[0]
  

  player_point = player.point_sum()
  cpu_point = dealer.point_sum()

  flag = True
  first_write = True
  while flag:
    pygame.display.update()  
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if end_button.collidepoint(event.pos) and end_status == True:
          pygame.quit()
          sys.exit()
    if first_write:
      if player_point == cpu_point == 21:
        card_front(player, dealer)
        result('drow')
        end_status = True
      elif player_point == 21:
        card_front(player, dealer)
        result('win')
        end_status = True
      elif cpu_point == 21:
        card_front(player, dealer)
        result('lose')
        end_status = True
      else:
        card_back(player, dealer)
        draw_check()
        flag = False
      first_write = False

  flag = True
  while True:
    pygame.display.update()  
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if yes_button.collidepoint(event.pos) and end_status == False:
          drawing(d, player, ' プレイヤー')
          card_back(player, dealer)
          player_point = player.point_sum()
          if player_point >= 22:
            base_draw()
            card_front(player, dealer)
            result('lose')
            end_status = True
        if no_button.collidepoint(event.pos) and end_status == False:
          while flag:
            cpu_point = dealer.point_sum()
            if cpu_point < 17:
              drawing(d, dealer, ' ディーラー')
              cpu_point = dealer.point_sum()
            elif cpu_point >= 22:
              base_draw()
              card_front(player, dealer)
              result('win')
              end_status = True
              flag = False
            elif cpu_point == player_point:
              base_draw()
              card_front(player, dealer)
              result('drow')
              end_status = True
              flag = False
            elif cpu_point >= 17 and cpu_point > player_point:
              base_draw()
              card_front(player, dealer)
              result('lose')
              end_status = True
              flag = False
        if end_button.collidepoint(event.pos) and end_status == True:
          pygame.quit()
          sys.exit()

if __name__ == '__main__':
  main()