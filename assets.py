"""
资源管理模块 - 字体、主题等，便于扩展多语言与换肤
"""
import os
from typing import Dict, Optional

import pygame

from config import DEFAULT_THEME, ThemeConfig


def _find_chinese_font_path() -> Optional[str]:
    """查找支持中文的系统字体"""
    font_names = ["msyh.ttf", "simhei.ttf", "simsun.ttc"]
    fonts_dir = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts")
    for name in font_names:
        path = os.path.join(fonts_dir, name)
        if os.path.exists(path):
            return path
    return None


class FontManager:
    """字体管理器，统一管理各类字号"""

    def __init__(self) -> None:
        self._fonts: Dict[int, pygame.font.Font] = {}
        self._base_path = _find_chinese_font_path()

    def get(self, size: int) -> pygame.font.Font:
        """获取指定大小的字体"""
        if size not in self._fonts:
            if self._base_path:
                self._fonts[size] = pygame.font.Font(self._base_path, size)
            else:
                self._fonts[size] = pygame.font.Font(None, size)
        return self._fonts[size]


# 全局字体实例
fonts = FontManager()


def get_font(size: int) -> pygame.font.Font:
    """便捷获取字体"""
    return fonts.get(size)
