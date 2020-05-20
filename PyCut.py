#!/usr/bin/python
import pygame
from game import PyCutGame as PyCut
import cProfile
import gi
from gi.repository import Gdk

def main():
    pygame.init()
    pygame.display.set_mode((Gdk.Screen.width(), Gdk.Screen.height()), pygame.RESIZABLE)
    game_instance = PyCut()
    game_instance.run()

if __name__ == '__main__':
    main()
