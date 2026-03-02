# 贪吃蛇

基于 Python + Pygame 的贪吃蛇游戏，模块化架构，便于扩展。

## 项目结构

```
snake/
├── main.py          # 入口
├── config.py        # 配置（窗口、网格、难度、主题）
├── assets.py        # 资源（字体）
├── entities.py      # 实体（Snake、Food）
├── game.py          # 游戏主循环与状态机
└── screens/         # 界面
    ├── base.py      # 屏幕基类
    ├── menu.py      # 主菜单
    ├── gameplay.py  # 游戏进行中
    └── game_over.py # 结束界面
```

## 运行方式

```bash
pip install -r requirements.txt
python main.py
```

## 操作说明

- **开始页面**：选择难度后点击「开始游戏」
- **方向键**：控制蛇的移动方向
- **空格键**：游戏结束后重新开始

## 扩展指南

- **新难度**：在 `config.py` 的 `DIFFICULTIES` 中添加
- **新主题**：在 `config.py` 中定义新 `ThemeConfig`，传入各 Screen
- **新实体**：在 `entities.py` 中新增类（如障碍物、道具）
- **新界面**：继承 `screens.base.Screen` 实现新屏幕
