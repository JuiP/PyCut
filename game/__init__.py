import pygame
import traceback
import os

from . import scenes, events, objects

class PyCutGame():
    """docstring for PyCutGame"""
    def __init__(self, poll_cb=None):
        self.dev = True
        self.data = None
        self.basePath = os.path.dirname(__file__)
        ##pre-inits for pygame?
        #pygame.mixer.pre_init(44100, -16, 1, 512*2)
        #pygame.display.init()
        #pygame.font.init()
        #pygame.mixer.init(44100)
        ########################
        self.width = 1200
        self.height = 900
        self.fps = 15
        self.title = "PyCut"
        self.quit_attempt = False
        self.level = 1
        self.total_good_pizza = 0
        self.poll_cb = poll_cb

    def scaling_constants(self, screen):
        self.width, self.height = screen.get_width(), screen.get_height()
        scale_x = self.width / 1200.0
        scale_y = self.height / 900.0
        return scale_x, scale_y

    def load_assets(self):
        self.game_icon = self.load_image("PyCut_icon.png")
        self.game_icon = pygame.transform.scale(self.game_icon,
                                                (int(55 * SCALE_X),int(55 * SCALE_Y)))
        self.font_path  = os.path.join(self.basePath, "assets/font/Roboto-Thin.ttf")
        self.bold_font_path  = os.path.join(self.basePath, "assets/font/Roboto-Regular.ttf")
        self.shop_background = self.load_image("Background.png")
        self.shop_background = pygame.transform.scale(self.shop_background,
                                                (int(1200 * SCALE_X),int(900 * SCALE_Y)))
        self.counter_top = self.load_image("Countertop.png")
        self.counter_top = pygame.transform.scale(self.counter_top,
                                                (int(1200 * SCALE_X),int(900 * SCALE_Y)))
        self.help_img = self.load_image("help.png")
        self.help_img = pygame.transform.scale(self.help_img,
                                                (int(1000 * SCALE_X),int(561 * SCALE_Y)))
        self.plain_pizza = self.load_image("blank_pizza.png")
        self.plain_pizza = pygame.transform.scale(self.plain_pizza,
                                                (int(520 * SCALE_X),int(520 * SCALE_Y)))
        self.button_bg = self.load_image("red_button01.png")
        self.button_bg = pygame.transform.scale(self.button_bg,
                                                (int(190 * SCALE_X),int(49 * SCALE_Y)))
        self.button_bg_active = self.load_image("red_button02.png")
        self.button_bg_active = pygame.transform.scale(self.button_bg_active,
                                                (int(190 * SCALE_X),int(49 * SCALE_Y)))
        self.message_bubble_img = self.load_image("message_bubble.png")
        self.message_bubble_img = pygame.transform.scale(self.message_bubble_img,
                                                (int(850 * SCALE_X),int(151 * SCALE_Y)))
        self.cheese_img = self.load_image("cheese.png")
        self.cheese_img = pygame.transform.scale(self.cheese_img,
                                                (int(325 * SCALE_X),int(225 * SCALE_Y)))
        self.mushroom_img = self.load_image("mushroom.png")
        self.mushroom_img = pygame.transform.scale(self.mushroom_img,
                                                (int(280 * SCALE_X),int(280 * SCALE_Y)))
        self.pepperoni_img = self.load_image("pepperoni.png")
        self.pepperoni_img = pygame.transform.scale(self.pepperoni_img,
                                                (int(210 * SCALE_X),int(210 * SCALE_Y)))
        self.pineapple_img = self.load_image("pineapple.png")
        self.pineapple_img = pygame.transform.scale(self.pineapple_img,
                                                (int(280 * SCALE_X),int(280 * SCALE_Y)))
        self.trash_can_img = self.load_image("trash_can.png")
        self.trash_can_img = pygame.transform.scale(self.trash_can_img,
                                                (int(245 * SCALE_X),int(299 * SCALE_Y)))
        self.trash_can_front_img = self.load_image("trash_can_front.png")
        self.trash_can_front_img = pygame.transform.scale(self.trash_can_front_img,
                                                (int(245 * SCALE_X),int(299 * SCALE_Y)))
        self.trash_can_back_img = self.load_image("trash_can_back.png")
        self.trash_can_back_img = pygame.transform.scale(self.trash_can_back_img,
                                                (int(245 * SCALE_X),int(299 * SCALE_Y)))
        self.character_1 = self.load_image("Character1.png")
        self.character_1 = pygame.transform.scale(self.character_1,
                                                (int(232 * SCALE_X),int(348 * SCALE_Y)))
        self.character_2 = self.load_image("Character2.png")
        self.character_2 = pygame.transform.scale(self.character_2,
                                                (int(236 * SCALE_X),int(345 * SCALE_Y)))
        self.character_3 = self.load_image("Character3.png")
        self.character_3 = pygame.transform.scale(self.character_3,
                                                (int(235 * SCALE_X),int(349 * SCALE_Y)))
        self.character_4 = self.load_image("Character4.png")
        self.character_4 = pygame.transform.scale(self.character_4,
                                                (int(232 * SCALE_X),int(354 * SCALE_Y)))
        self.game_characters = [self.character_1, self.character_2,
                                self.character_3, self.character_4]
        self.game_toppings = [self.cheese_img, self.mushroom_img,
                                self.pepperoni_img, self.pineapple_img]

    def game_loop(self):
        self.screen = pygame.display.get_surface()
        global SCALE_X, SCALE_Y
        SCALE_X, SCALE_Y = self.scaling_constants(self.screen)
        self.clock = pygame.time.Clock()
        self.load_assets()
        self.font_large = pygame.font.Font(self.font_path, int(72 * SCALE_X))
        self.font = pygame.font.Font(self.font_path, int(24 * SCALE_X))
        self.font_small = pygame.font.Font(self.font_path, int(14 * SCALE_X))
        self.bold_font_large = pygame.font.Font(self.bold_font_path, int(72 * SCALE_X))
        self.bold_font = pygame.font.Font(self.bold_font_path, int(24 * SCALE_X))
        self.bold_font_small = pygame.font.Font(self.bold_font_path, int(14 * SCALE_X))
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.game_icon)
        self.difficulty = "Easy"
        self.starting_scene = scenes.TitleScene
        self.active_scene = self.starting_scene(self)

        while self.active_scene != None:
            if self.poll_cb:
                self.poll_cb()
            pressed_keys = pygame.key.get_pressed()
            # Event filtering
            filtered_events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_attempt = True
                elif event.type == pygame.KEYDOWN:
                    alt_pressed = pressed_keys[pygame.K_LALT] or \
                                  pressed_keys[pygame.K_RALT]
                    if event.key == pygame.K_ESCAPE:
                        self.quit_attempt = True
                    elif event.key == pygame.K_F4 and alt_pressed:
                        self.quit_attempt = True

                if self.quit_attempt:
                    self.active_scene.Terminate()
                else:
                    filtered_events.append(event)

            self.active_scene.ProcessInput(filtered_events, pressed_keys)
            self.active_scene.Update()
            self.active_scene.Render()

            if not self.active_scene.override_render:
                pygame.display.flip()
            self.active_scene = self.active_scene.next
            self.clock.tick(self.fps)

    def run(self):
        self.game_loop()

    def quit(self):
        self.quit_attempt = True

    def load_image(self, img):
        """Load image from file path

        img: The name of the image to load
        """
        img_path = os.path.join(self.basePath, "assets/img/" + img)
        return pygame.image.load(img_path)

    def write_file(self, file_path):
        # Ignoring file_path because it seems to be useless when this actually gets called
        # I also don't know what was calling this, nor what message to store
        # So I am just dumping a stack trace at the time of call
        log = open("log.txt","a")
        log.write("\n")
        log.write("Begin Log \n")
        log.write(''.join(traceback.format_stack()))
        log.write("End Log")
        log.close()
