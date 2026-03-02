"""游戏主界面"""
from typing import Optional

import pygame

from assets import get_font
from config import DEFAULT_THEME, GridConfig, ThemeConfig, WindowConfig
from entities import Food, Snake, DIR_DOWN, DIR_LEFT, DIR_RIGHT, DIR_UP
from screens.base import Screen, ScreenResult


class GameplayScreen(Screen):
    """游戏进行中界面"""

    def __init__(
        self,
        snake: Snake,
        food: Food,
        difficulty_index: int,
        theme: ThemeConfig = None,
    ) -> None:
        self._snake = snake
        self._food = food
        self._difficulty_index = difficulty_index
        self._theme = theme or DEFAULT_THEME
        self._grid = GridConfig()
        self._font = get_font(36)

    def handle_event(self, event: pygame.event.Event) -> Optional[ScreenResult]:
        if event.type == pygame.KEYDOWN:
            key_map = {
                pygame.K_UP: DIR_UP,
                pygame.K_DOWN: DIR_DOWN,
                pygame.K_LEFT: DIR_LEFT,
                pygame.K_RIGHT: DIR_RIGHT,
            }
            if event.key in key_map:
                self._snake.set_direction(key_map[event.key])
        return None

    def update(self, dt: float) -> Optional[ScreenResult]:
        # 移动蛇
        ate_food = self._snake.head == self._food.pos
        self._snake.move(grow=ate_food)

        if ate_food:
            self._food.spawn(self._snake.body)

        # 碰撞检测
        if self._snake.collides_with_wall() or self._snake.collides_with_self():
            score = self._snake.length - self._snake.initial_length
            return ScreenResult(next_state="game_over", data={"score": score})

        return None

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(self._theme.background)

        # 网格
        cs = self._grid.cell_size
        for x in range(0, WindowConfig.width, cs):
            pygame.draw.line(surface, self._theme.grid, (x, 0), (x, WindowConfig.height))
        for y in range(0, WindowConfig.height, cs):
            pygame.draw.line(surface, self._theme.grid, (0, y), (WindowConfig.width, y))

        # 蛇与食物
        self._snake.draw(surface, self._theme.snake, cs)
        self._food.draw(surface, self._theme.food, cs)

        # 分数
        score = self._snake.length - self._snake.initial_length
        text = self._font.render(f"分数: {score}", True, self._theme.text)
        surface.blit(text, (10, 10))
