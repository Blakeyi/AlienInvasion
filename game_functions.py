import sys, os
import pygame
from PyQt5.QtWidgets import QDialog, QApplication
from bullet import Bullet
from alien import Alien
from time import sleep
import game_setting
import about

def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def message_diaplay(srceen, text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((300 / 2), (100 / 2))
    srceen.blit(TextSurf, TextRect)
    pygame.display.update()


def check_keydown_events(event, ai_settings, screen, ship, bullets, game_sounds):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #  创建一颗子弹，并将其加入到编组 bullets 中
        if ship.bullet_num == 0:
            print('没子弹了！！！')
            #message_diaplay(screen, '没子弹了！！！')
        else:
            ship.bullet_num -= 1
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
            game_sounds[0].play()
    elif event.key == pygame.K_q:
        sys.exit()


def check_click_button(ai_settings, stats, button_list, mouse_x, mouse_y):
    """ 在玩家单击 Play 按钮时开始新游戏 """
    print(mouse_x, mouse_y)
    if button_list[2].rect.collidepoint(mouse_x, mouse_y + 20):
        stats.reset_stats()
        stats.game_active = True


def check_keyup_events(event, ship):
    """ 响应松开 """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets, stats, play_button, game_sounds):
    """ 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os._exit(0)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, game_sounds)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_click_button(ai_settings, stats, play_button, mouse_x, mouse_y)


def get_number_aliens_x(ai_settings, alien_width):
    """ 计算每行可容纳多少个外星人 """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ 创建一个外星人并将其放在当前行 """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """ 计算屏幕可容纳多少行外星人 """
    available_space_y = (ai_settings.screen_height -
                        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(ai_settings, screen, ship, aliens):
    """ 创建外星人群 """
    #  创建一个外星人，并计算每行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)
    #  创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """ 有外星人到达边缘时采取相应的措施 """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break 


def change_fleet_direction(ai_settings, aliens):
    """ 将整群外星人下移，并改变它们的方向 """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
    ai_settings.alien_fleet_direction *= -1

def update_bullets(bullets, aliens, stats, game_sounds):
    for bullet in bullets.sprites():
        bullet.update()
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        else:
            bullet.draw()
    #  检查是否有子弹击中了外星人
    #  如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        game_sounds[1].play()
        print("消灭了 " + str(len(collisions)) + " 个外星人")
        stats.current_score += 5 * len(collisions)
        stats.kill_num += len(collisions)


def update_ship(ship):
    ship.update()


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    for alien in aliens.sprites():
        alien.update()
        alien.draw()
    #  检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def update_screen(ai_settings, screen, ship, bullets, aliens, stats, button_list, game_sounds):
    """更新屏幕上图像，并切换到新的屏幕"""

    screen.fill(ai_settings.bg_color)
    if not stats.game_active:
        for button in button_list:
            button.draw()
        sleep(1)
    else:
        update_bullets(bullets, aliens, stats, game_sounds)
        update_aliens(ai_settings, stats, screen, ship, aliens, bullets) 
        update_ship(ship)
        stats.draw() 
   
    pygame.display.flip()


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """ 检查是否有外星人到达了屏幕底端 """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #  像飞船被撞到一样进行处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """ 响应被外星人撞到的飞船 """
    stats.ships_left -= 1
    if(stats.ships_left == 0):
        stats.game_active = False
        print("游戏结束")
    else:
        print("还剩下" + str(stats.ships_left) + '条命')
    aliens.empty()
    bullets.empty()

    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    sleep(3)
