"""
屏幕基类 - 定义统一接口，便于扩展新界面
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Optional

import pygame


@dataclass
class ScreenResult:
    """屏幕返回结果，用于状态流转"""
    next_state: Optional[str] = None
    data: Optional[Dict[str, Any]] = None


class Screen(ABC):
    """屏幕抽象基类"""

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> Optional[ScreenResult]:
        """处理事件，返回 None 表示无状态切换"""
        pass

    @abstractmethod
    def update(self, dt: float) -> Optional[ScreenResult]:
        """更新逻辑"""
        pass

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        """绘制界面"""
        pass
