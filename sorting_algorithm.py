import pygame
import sys
import random
# deneme
sortList = []
WIDTH = 1000
HEIGHT = 850
WHITE = (240, 240, 240)
BLACK = (30, 30, 30)
RED = (143, 16, 26)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sorting')
screen.fill(BLACK)


def selection():
    pygame.draw.rect(screen, RED, [25, 50, 150, 50])
    pygame.draw.rect(screen, RED, [225, 50, 150, 50])
    pygame.draw.rect(screen, RED, [425, 50, 150, 50])
    pygame.draw.rect(screen, RED, [625, 50, 150, 50])
    pygame.draw.rect(screen, RED, [825, 50, 150, 50])

    font = pygame.font.SysFont('', 24)
    img = font.render('Merge Sort', True, WHITE)
    img2 = font.render('Quick Sort', True, WHITE)
    img3 = font.render('Heap Sort', True, WHITE)
    img4 = font.render('Bubble Sort', True, WHITE)
    img5 = font.render('Insertion Sort', True, WHITE)
    screen.blit(img, (55, 68))
    screen.blit(img2, (255, 68))
    screen.blit(img3, (455, 68))
    screen.blit(img4, (655, 68))
    screen.blit(img5, (850, 68))
    # pygame.draw.rect(screen, BLUEISH, [25, 125, 150, 50])


def sortSelect(pos_x, pos_y):
    if 25 <= pos_x <= 175 and 50 <= pos_y <= 100:
        mergeSort(sortList)
        mergeDraw(sortList)
    if 225 <= pos_x <= 375 and 50 <= pos_y <= 100:
        print('Quick Sort')
    if 425 <= pos_x <= 575 and 50 <= pos_y <= 100:
        print('Heap Sort')
    if 625 <= pos_x <= 775 and 50 <= pos_y <= 100:
        print('Bubble Sort')
    if 825 <= pos_x <= 975 and 50 <= pos_y <= 100:
        print('Insertion Sort')


for i in range(50):
    rect_height = random.randint(10, 500)
    sortList.append(rect_height)
    pygame.draw.rect(screen, WHITE, [19.9 * i + 1, HEIGHT - rect_height, 15, rect_height])


def mergeSort(array):
    if len(array) > 1:
        midP = len(array)//2

        left = array[:midP]
        right = array[midP:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def mergeDraw(array):
    for i in range(len(array)):
       pygame.draw.rect(screen, RED, [19.9 * i + 1, HEIGHT - array[i], 15, array[i]])
    print()


def quickSort():
    pass


def heapSort():
    pass


def bubbleSort():
    pass


def insertionSort():
    pass


selection()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            sortSelect(pos[0], pos[1])
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
