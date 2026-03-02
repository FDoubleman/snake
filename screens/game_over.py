"""游戏结束界面"""
from typing import Optional

import pygame

from assets import get_font
from config import DEFAULT_THEME, GridConfig, ThemeConfig, WindowConfig
from entities import Food, Snake
from screens.base import Screen, ScreenResult


class GameOverScreen(Screen):
    """Game Over 界面 - 绘制冻结的游戏画面 + 结束提示"""

    def __init__(
        self,
        snake: Snake,
        food: Food,
        score: int,
        theme: ThemeConfig = None,
    ) -> None:
        self._snake = snake
        self._food = food
        self._score = score
        self._theme = theme or DEFAULT_THEME
        self._grid = GridConfig()
        self._font = get_font(36)
        self._font_large = get_font(72)

    def handle_event(self, event: pygame.event.Event) -> Optional[ScreenResult]:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return ScreenResult(next_state="playing")
        return None

    def update(self, dt: float) -> Optional[ScreenResult]:
        return None

    def draw(self, surface: pygame.Surface) -> None:
        # 绘制冻结的游戏画面
        surface.fill(self._theme.background)
        cs = self._grid.cell_size
        for x in range(0, WindowConfig.width, cs):
            pygame.draw.line(surface, self._theme.grid, (x, 0), (x, WindowConfig.height))
        for y in range(0, WindowConfig.height, cs):
            pygame.draw.line(surface, self._theme.grid, (0, y), (WindowConfig.width, y))
        self._snake.draw(surface, self._theme.snake, cs)
        self._food.draw(surface, self._theme.food, cs)
        score_text = self._font.render(f"分数: {self._score}", True, self._theme.text)
        surface.blit(score_text, (10, 10))

        # 结束提示
        text = self._font_large.render("Game Over", True, self._theme.text)
        tr = text.get_rect(center=(WindowConfig.width // 2, WindowConfig.height // 2 - 30))
        surface.blit(text, tr)

        hint = self._font.render("按空格键重新开始", True, self._theme.text)
        hr = hint.get_rect(center=(WindowConfig.width // 2, WindowConfig.height // 2 + 20))
        surface.blit(hint, hr)
