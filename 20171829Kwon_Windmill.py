import pygame
import numpy as np
import math

# 게임 윈도우 크기
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DEEPBROWN=(101,67,33)

#함수:로테이션과 이동, 함수변경

def Rmat(deg):
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

def Dimension(pp):
    q=pp[0:2, :].T
    return q

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Drawing")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 전까지 반복
done = False

# poly: 4 x 3 matrix
poly = np.array( [[0, 0, 1], [100, 0, 1], [100, 20, 1], [0, 20, 1]])
poly = poly.T # 3x4 matrix 
cor = np.array([10, 10, 1])
degree = 10

poly2=np.array( [[0,0,1], [200,-100,1], [300,0,1], [200,100,1]])
poly2=poly2.T
cor2=np.array([10,10,1])
degree2=100

poly3=np.array( [[0,0,1], [200,-100,1], [300,0,1], [200,100,1]])
poly3=poly3.T
cor3=np.array([10,10,1])
degree3=190

poly4=np.array( [[0,0,1], [200,-100,1], [300,0,1], [200,100,1]])
poly4=poly4.T
cor4=np.array([10,10,1])
degree4=280

poly5=np.array( [[0,0,1], [200,-100,1], [300,0,1], [200,100,1]])
poly5=poly5.T
cor5=np.array([10,10,1])
degree5=370


# 폰트 선택(폰트, 크기, 두껍게, 이탤릭)
font = pygame.font.SysFont('arial', 20, True, False)

# 게임 반복 구간
while not done:
# 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 윈도우 화면 채우기
    screen.fill((255,255,255))

    # 다각형 그리기
    # poly: 3xN 
#    pygame.draw.polygon(screen, WHITE, poly[:2].T, 4)
    pygame.draw.polygon(screen, GREEN, ((400,WINDOW_HEIGHT),(500,WINDOW_HEIGHT-200),(WINDOW_WIDTH-500,WINDOW_HEIGHT-200),(WINDOW_WIDTH-400,WINDOW_HEIGHT)))
    pygame.draw.polygon(screen, BLACK, ((800,WINDOW_HEIGHT-200),(850,WINDOW_HEIGHT-600),(WINDOW_WIDTH/2,WINDOW_HEIGHT-700),
        (WINDOW_WIDTH-850,WINDOW_HEIGHT-600),(WINDOW_WIDTH-800,WINDOW_HEIGHT-200)), 4)
#    pygame.draw.polygon(screen, RED, poly2[:2].T, 4)
    

    degree += 1
    H = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT-700) @ Tmat(0,0) @ Rmat(degree) @ Tmat(0,0)
    pp = H @ poly
    corp = H @ cor
    # print(pp.shape, pp, pp.T )
    q = pp[0:2, :].T # N x 2 matrix
#    pygame.draw.polygon(screen, RED, q, 4)
#    pygame.draw.circle(screen, (255, 128, 128), corp[:2], 3)

    degree2 += 1
    H2 = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT-700) @ Tmat(0,0) @ Rmat(degree2) @ Tmat(0,0) @ Rmat(90)
    pp2 = H2 @ poly2
    corp2 = H2 @ cor2
    q2 = pp2[0:2, :].T # N x 2 matrix
    pygame.draw.polygon(screen, DEEPBROWN, q2)

    degree3 += 1
    H3 = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT-700) @ Tmat(0,0) @ Rmat(degree3) @ Tmat(0,0) @ Rmat(180)
    pp3 = H3 @ poly3
    corp3 = Rmat(180)@ H3 @ cor3
    q3 = pp2[0:2, :].T # N x 2 matrix
    pygame.draw.polygon(screen, DEEPBROWN, q3)

    degree4 += 1
    H4 = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT-700) @ Tmat(0,0) @ Rmat(degree4) @ Tmat(0,0)
    pp4 = H4 @ poly4
    corp4 = H2 @ cor4
    q4 = pp4[0:2, :].T # N x 2 matrix
    pygame.draw.polygon(screen, DEEPBROWN, q4)

    degree5 += 1
    H5 = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT-700) @ Tmat(0,0) @ Rmat(degree5) @ Tmat(0,0)
    pp5 = H5 @ poly5
    corp5 = H2 @ cor5
    q5 = pp5[0:2, :].T # N x 2 matrix
    pygame.draw.polygon(screen, DEEPBROWN, q5)


    # 안티얼리어스를 적용하고 검은색 문자열 렌더링
    text = font.render("20171829 KWON_WINDMILL", True, BLACK)
    screen.blit(text, [WINDOW_WIDTH*3/4, WINDOW_HEIGHT/7])

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()
