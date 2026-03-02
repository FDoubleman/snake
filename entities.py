"""
游戏实体模块 - Snake、Food 等，便于扩展新实体（障碍物、道具等）
"""
import random
from typing import List, Tuple

import pygame

from config import GridConfig, WindowConfig


# 方向向量
DIR_UP = (0, -1)
DIR_DOWN = (0, 1)
DIR_LEFT = (-1, 0)
DIR_RIGHT = (1, 0)
DIRECTIONS = (DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT)


class Snake:
    """蛇实体 - 封装移动、生长、碰撞检测"""

    def __init__(self, grid: GridConfig) -> None:
        self._grid = grid
        self._body: List[Tuple[int, int]] = []
        self._direction = DIR_RIGHT
        self.reset()

    def reset(self) -> None:
        """重置蛇到初始状态"""
        cx, cy = self._grid.cols // 2, self._grid.rows // 2
        self._body = [(cx, cy), (cx - 1, cy), (cx - 2, cy)]
        self._direction = DIR_RIGHT

    @property
    def head(self) -> Tuple[int, int]:
        return self._body[0]

    @property
    def body(self) -> List[Tuple[int, int]]:
        return self._body.copy()

    @property
    def length(self) -> int:
        return len(self._body)

    @property
    def initial_length(self) -> int:
        return 3  # 初始长度

    def set_direction(self, new_dir: Tuple[int, int]) -> None:
        """设置方向（防止反向）"""
        if (new_dir[0] + self._direction[0], new_dir[1] + self._direction[1]) != (0, 0):
            self._direction = new_dir

    def move(self, grow: bool = False) -> None:
        """移动一步，grow=True 时不移除尾部（吃食物后）"""
        hx, hy = self._body[0]
        dx, dy = self._direction
        new_head = (hx + dx, hy + dy)
        self._body.insert(0, new_head)
        if not grow:
            self._body.pop()

    def collides_with_self(self) -> bool:
        """是否撞到自己"""
        return self.head in self._body[1:]

    def collides_with_wall(self) -> bool:
        """是否撞墙"""
        x, y = self.head
        return x < 0 or x >= self._grid.cols or y < 0 or y >= self._grid.rows

    def contains(self, pos: Tuple[int, int]) -> bool:
        """某位置是否在蛇身上"""
        return pos in self._body

    def draw(self, surface: pygame.Surface, color: Tuple[int, int, int], cell_size: int) -> None:
        """绘制蛇身"""
        for seg in self._body:
            rect = pygame.Rect(seg[0] * cell_size, seg[1] * cell_size, cell_size - 1, cell_size - 1)
            pygame.draw.rect(surface, color, rect)


class Food:
    """食物实体 - 封装生成与绘制"""

    def __init__(self, grid: GridConfig) -> None:
        self._grid = grid
        self._pos: Tuple[int, int] = (0, 0)

    def spawn(self, occupied: List[Tuple[int, int]]) -> None:
        """在非占用位置随机生成"""
        while True:
            x = random.randint(0, self._grid.cols - 1)
            y = random.randint(0, self._grid.rows - 1)
            if (x, y) not in occupied:
                self._pos = (x, y)
                return

    @property
    def pos(self) -> Tuple[int, int]:
        return self._pos

    def draw(self, surface: pygame.Surface, color: Tuple[int, int, int], cell_size: int) -> None:
        """绘制食物"""
        rect = pygame.Rect(
            self._pos[0] * cell_size, self._pos[1] * cell_size,
            cell_size - 1, cell_size - 1
        )
        pygame.draw.rect(surface, color, rect)
