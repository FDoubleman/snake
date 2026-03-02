"""
游戏主循环与状态机 - 协调各屏幕切换与游戏节奏
"""
import pygame

from config import DIFFICULTIES, DEFAULT_THEME, GridConfig, WindowConfig
from entities import Food, Snake
from screens.base import Screen
from screens import GameOverScreen, GameplayScreen, MenuScreen


class Game:
    """游戏主控制器"""

    def __init__(self) -> None:
        pygame.init()
        self._screen = pygame.display.set_mode((WindowConfig.width, WindowConfig.height))
        pygame.display.set_caption(WindowConfig.title)

        self._clock = pygame.time.Clock()
        self._theme = DEFAULT_THEME
        self._grid = GridConfig()

        self._state = "menu"
        self._current_screen: Screen = None
        self._difficulty_index = 1

        # 游戏实体（playing / game_over 时使用）
        self._snake: Snake = None
        self._food: Food = None

        self._enter_menu()

    def _enter_menu(self) -> None:
        self._state = "menu"
        self._current_screen = MenuScreen(self._theme)

    def _enter_playing(self, difficulty_index: int = None) -> None:
        if difficulty_index is not None:
            self._difficulty_index = difficulty_index

        self._snake = Snake(self._grid)
        self._food = Food(self._grid)
        self._food.spawn(self._snake.body)

        self._state = "playing"
        self._current_screen = GameplayScreen(
            self._snake, self._food, self._difficulty_index, self._theme
        )

    def _enter_game_over(self, score: int) -> None:
        self._state = "game_over"
        self._current_screen = GameOverScreen(
            self._snake, self._food, score, self._theme
        )

    def _get_tick_rate(self) -> int:
        """当前状态下的帧率"""
        if self._state == "playing":
            return DIFFICULTIES[self._difficulty_index].speed
        return WindowConfig.fps

    def run(self) -> None:
        """主循环"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

                result = self._current_screen.handle_event(event)
                if result and result.next_state:
                    self._apply_transition(result)

            if not running:
                break

            result = self._current_screen.update(1.0 / self._get_tick_rate())
            if result and result.next_state:
                self._apply_transition(result)

            self._current_screen.draw(self._screen)
            pygame.display.flip()
            self._clock.tick(self._get_tick_rate())

        pygame.quit()

    def _apply_transition(self, result) -> None:
        """根据 ScreenResult 切换状态"""
        state = result.next_state
        data = result.data or {}

        if state == "playing":
            diff = data.get("difficulty", self._difficulty_index)
            self._enter_playing(diff)
        elif state == "game_over":
            score = data.get("score", 0)
            self._enter_game_over(score)
