"""
游戏配置模块 - 集中管理所有可调参数，便于扩展与调优
"""
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass(frozen=True)
class WindowConfig:
    """窗口配置"""
    width: int = 800
    height: int = 600
    title: str = "贪吃蛇"
    fps: int = 60


@dataclass(frozen=True)
class GridConfig:
    """网格配置"""
    cell_size: int = 20

    @property
    def cols(self) -> int:
        return WindowConfig.width // self.cell_size

    @property
    def rows(self) -> int:
        return WindowConfig.height // self.cell_size


@dataclass(frozen=True)
class DifficultyConfig:
    """难度配置"""
    name: str
    speed: int  # 每秒移动次数（帧数）


# 难度预设，便于扩展新难度
DIFFICULTIES: Tuple[DifficultyConfig, ...] = (
    DifficultyConfig("简单", 6),
    DifficultyConfig("普通", 10),
    DifficultyConfig("困难", 14),
    DifficultyConfig("极难", 18),
)


@dataclass
class ThemeConfig:
    """主题/颜色配置，便于后期换肤"""
    background: Tuple[int, int, int] = (0, 0, 0)
    grid: Tuple[int, int, int] = (40, 40, 40)
    snake: Tuple[int, int, int] = (0, 200, 0)
    food: Tuple[int, int, int] = (255, 0, 0)
    text: Tuple[int, int, int] = (255, 255, 255)
    button: Tuple[int, int, int] = (0, 150, 0)
    button_hover: Tuple[int, int, int] = (0, 180, 0)
    button_inactive: Tuple[int, int, int] = (60, 60, 60)


# 默认主题，可扩展更多主题
DEFAULT_THEME = ThemeConfig()
