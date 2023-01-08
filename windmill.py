import pygame
import sys
import numpy as np
import math
import os

# 게임 윈도우 크기
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
SKYBLUE=(135,206,235)
DEEPBROWN=(101,67,33)

#함수:로테이션과 이동, 함수변경

def Rmat(degree):
    radian = np.deg2rad(degree)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array( [[ c, -s, 0], [s, c, 0], [0, 0, 1] ] )
    return R

def Tmat(a,b):
    H = np.eye(3)
    H[0,2] = a
    H[1,2] = b
    return H

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("20171829Kwon_Windmill")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

#이미지 로드
tile_img=pygame.image.load(os.path.join(assets_path,'tile.jpg'))
tile_img=pygame.transform.scale(tile_img,(400,500))
tile_rect=tile_img.get_rect()
tile_rect.x=WINDOW_WIDTH/2-200
tile_rect.y=380

# 게임 종료 전까지 반복
done = False

# poly: 4 x 3 matrix
poly = np.array( [[0, 0, 1], [80, 20, 1], [100, 0, 1], [80, -20, 1]])

"""ver1
poly2 = np.array( [[0, 0, 1], [200, 80, 1], [300, 0, 1], [200, -80, 1]])
poly3 = np.array( [[0, 0, 1], [80, 200, 1], [0,300, 1], [-80, 200, 1]])
poly4 = np.array( [[0, 0, 1], [-200, -80, 1], [-300,0, 1], [-200, -80, 1]])
poly5 = np.array( [[0, 0, 1], [-80,-200, 1], [0,-300, 1], [-80,-200, 1]])
"""

#ver2
poly2 = np.array( [[0, 0, 1], [200, 80, 1], [300, 0, 1], [200, -80, 1]])
poly3 = np.array( [[0, 0, 1], [200, 80, 1], [300, 0, 1], [200, -80, 1]])
poly4 = np.array( [[0, 0, 1], [200, 80, 1], [300, 0, 1], [200, -80, 1]])
poly5 = np.array( [[0, 0, 1], [200, 80, 1], [300, 0, 1], [200, -80, 1]])


poly = poly.T # 3x4 matrix 
poly2= poly2.T
poly3= poly3.T
poly4= poly4.T
poly5= poly5.T

cor = np.array([10, 10, 1])

degree = 10
degree2= 10
degree3= 100
degree4= 190
degree5= 280

degreev=1

# 폰트 선택(폰트, 크기, 두껍게, 기울기)
font = pygame.font.SysFont('arial', 20, True, True)

# 게임 반복 구간
while not done:
# 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # 키가 눌릴 경우
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                degreev+=1
            elif event.key == pygame.K_DOWN:
                degreev-=1
            elif event.key == pygame.K_SPACE:
                degreev=0
        # 키가 놓일 경우
#        elif event.type == pygame.KEYUP:
#            if event.key == pygame.K_UP:
#                degreev-=1
#            elif event.key == pygame.K_DOWN:
#                degreev+=1


    # 윈도우 화면 채우기
    screen.fill(SKYBLUE)

    # 이미지 그리기
    screen.blit(tile_img,tile_rect)

    # 다각형 그리기
    # poly: 3xN 
    pygame.draw.polygon(screen, GREEN, ((400,WINDOW_HEIGHT),(500,WINDOW_HEIGHT-200),(WINDOW_WIDTH-500,WINDOW_HEIGHT-200),(WINDOW_WIDTH-400,WINDOW_HEIGHT)))

    pygame.draw.polygon(screen, SKYBLUE, ((300,WINDOW_HEIGHT-200),(800,WINDOW_HEIGHT-200),(850,WINDOW_HEIGHT-600),(300,WINDOW_HEIGHT-600)))
    pygame.draw.polygon(screen, SKYBLUE, ((300,WINDOW_HEIGHT-600),(850,WINDOW_HEIGHT-600),(WINDOW_WIDTH/2,WINDOW_HEIGHT-700),(300,WINDOW_HEIGHT-700)))

    pygame.draw.polygon(screen, SKYBLUE, ((WINDOW_WIDTH-300,WINDOW_HEIGHT-200),(WINDOW_WIDTH-800,WINDOW_HEIGHT-200),(WINDOW_WIDTH-850,WINDOW_HEIGHT-600),(WINDOW_WIDTH-300,WINDOW_HEIGHT-600)))
    pygame.draw.polygon(screen, SKYBLUE, ((WINDOW_WIDTH-300,WINDOW_HEIGHT-600),(WINDOW_WIDTH-850,WINDOW_HEIGHT-600),(WINDOW_WIDTH/2,WINDOW_HEIGHT-700),(WINDOW_WIDTH-300,WINDOW_HEIGHT-700)))

    pygame.draw.polygon(screen, BLACK, ((800,WINDOW_HEIGHT-200),(850,WINDOW_HEIGHT-600),(WINDOW_WIDTH/2,WINDOW_HEIGHT-700),
        (WINDOW_WIDTH-850,WINDOW_HEIGHT-600),(WINDOW_WIDTH-800,WINDOW_HEIGHT-200)), 4)


    degree += 1
    degree2 += degreev
    degree3 += degreev
    degree4 += degreev
    degree5 += degreev

    H = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT-700) @ Tmat(0,0) @ Rmat(degree) @ Tmat(0,0)
    H2 = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT-700) @ Tmat(0,0) @ Rmat(degree2) @ Tmat(0,0)
    H3 = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT-700) @ Tmat(0,0) @ Rmat(degree3) @ Tmat(0,0) 
    H4 = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT-700) @ Tmat(0,0) @ Rmat(degree4)@ Tmat(0,0) 
    H5 = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT-700) @ Tmat(0,0) @ Rmat(degree5)@ Tmat(0,0)

    pp = H @ poly
    pp2 = H2 @ poly2
    pp3 = H3 @ poly3
    pp4 = H4 @ poly4
    pp5 = H5 @ poly5

    corp = H @ cor

    pygame.draw.polygon(screen, WHITE, pp2[0:2, :].T)
    pygame.draw.polygon(screen, WHITE, pp3[0:2, :].T)
    pygame.draw.polygon(screen, WHITE, pp4[0:2, :].T)
    pygame.draw.polygon(screen, WHITE, pp5[0:2, :].T)

    pygame.draw.polygon(screen, DEEPBROWN, pp2[0:2, :].T,4)
    pygame.draw.polygon(screen, DEEPBROWN, pp3[0:2, :].T,4)
    pygame.draw.polygon(screen, DEEPBROWN, pp4[0:2, :].T,4)
    pygame.draw.polygon(screen, DEEPBROWN, pp5[0:2, :].T,4)
    pygame.draw.circle(screen,BLACK,(WINDOW_WIDTH/2,WINDOW_HEIGHT-700),10)


    # 안티얼리어스를 적용하고 검은색 문자열 렌더링
    text = font.render("20171829 KWON_WINDMILL", True, BLACK)
    text2 = font.render("Press UP key for faster blade!", True, BLACK)
    text3 = font.render("Press Down for slower blade!", True, BLACK)
    text4 = font.render("Press SPACE to stop the blade!", True, BLACK)
    screen.blit(text, [WINDOW_WIDTH*3/4, WINDOW_HEIGHT/7])
    screen.blit(text2, [WINDOW_WIDTH*3/4, WINDOW_HEIGHT/7+25])
    screen.blit(text3, [WINDOW_WIDTH*3/4, WINDOW_HEIGHT/7+50])
    screen.blit(text4, [WINDOW_WIDTH*3/4, WINDOW_HEIGHT/7+75])

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()
