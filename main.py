from wad_data import WADData
from settings import *
import pygame as pg
import sys
from map_renderer import MapRenderer
from player import Player
from bsp import BSP
from seg_handler import SegHandler
from view_renderer import ViewRenderer


class DoomEngine:
    def __init__(self, wad_path='wad/DOOM1.WAD'):
        self.wad_path = wad_path
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.running = True
        self.dt = 1 / 60
        self.on_init()
    
    def on_init(self):
        self.wad_data = WADData(self, map_name='E1M1')
        self.map_renderer = MapRenderer(self)
        self.player = Player(self)
        self.bsp = BSP(self)
        self.seg_handler = SegHandler(self)
        self.view_renderer = ViewRenderer(self)
    
    def update(self):
        self.player.update()
        self.seg_handler.update()
        self.bsp.update()
        self.dt = self.clock.tick()
        pg.display.set_caption(f'{self.clock.get_fps()} FPS')
    
    def draw(self):
        pg.display.flip()
        self.screen.fill('black')
        self.map_renderer.draw()
        # pg.display.flip()
    
    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                self.running = False
    
    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    doom = DoomEngine()
    doom.run()
