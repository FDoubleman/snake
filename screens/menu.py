"""主菜单屏幕"""
from typing import Optional

import pygame

from assets import get_font
from config import DEFAULT_THEME, DIFFICULTIES, ThemeConfig, WindowConfig
from screens.base import Screen, ScreenResult


class MenuScreen(Screen):
    """开始菜单 - 难度选择 + 开始按钮"""

    def __init__(self, theme: ThemeConfig = None) -> None:
        self._theme = theme or DEFAULT_THEME
        self._selected = 1  # 默认普通
        self._font = get_font(36)
        self._font_title = get_font(48)

    def _get_button_rects(self) -> tuple:
        """获取按钮矩形（用于点击检测）"""
        bw, bh = 100, 40
        by = 270
        start_x = WindowConfig.width // 2 - (len(DIFFICULTIES) * (bw + 15) - 15) // 2

        diff_rects = []
        for i in range(len(DIFFICULTIES)):
            x = start_x + i * (bw + 15)
            diff_rects.append((pygame.Rect(x, by, bw, bh), i))

        start_rect = pygame.Rect(WindowConfig.width // 2 - 80, 380, 160, 50)
        return diff_rects, start_rect

    def handle_event(self, event: pygame.event.Event) -> Optional[ScreenResult]:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            diff_rects, start_rect = self._get_button_rects()
            pos = event.pos
            if start_rect.collidepoint(pos):
                return ScreenResult(next_state="playing", data={"difficulty": self._selected})
            for rect, idx in diff_rects:
                if rect.collidepoint(pos):
                    self._selected = idx
                    break
        return None

    def update(self, dt: float) -> Optional[ScreenResult]:
        return None

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(self._theme.background)

        # 标题
        title = self._font_title.render("贪吃蛇", True, self._theme.text)
        tr = title.get_rect(center=(WindowConfig.width // 2, 120))
        surface.blit(title, tr)

        # 难度标签
        label = self._font.render("游戏难度", True, self._theme.text)
        lr = label.get_rect(center=(WindowConfig.width // 2, 220))
        surface.blit(label, lr)

        diff_rects, start_rect = self._get_button_rects()

        # 难度按钮
        for rect, idx in diff_rects:
            color = self._theme.button if idx == self._selected else self._theme.button_inactive
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, self._theme.text, rect, 2)
            text = self._font.render(DIFFICULTIES[idx].name, True, self._theme.text)
            surface.blit(text, text.get_rect(center=rect.center))

        # 开始按钮
        pygame.draw.rect(surface, self._theme.button_hover, start_rect)
        pygame.draw.rect(surface, self._theme.text, start_rect, 2)
        st = self._font.render("开始游戏", True, self._theme.text)
        surface.blit(st, st.get_rect(center=start_rect.center))
