from pathlib import Path

from PIL import Image, ImageDraw


def build_icon() -> None:
    root = Path(__file__).resolve().parents[1]
    assets_dir = root / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    size = 256
    image = Image.new("RGBA", (size, size), (20, 20, 30, 255))
    draw = ImageDraw.Draw(image)

    # Grid-like background lines.
    for step in range(0, size, 32):
        draw.line((step, 0, step, size), fill=(45, 45, 60, 255), width=1)
        draw.line((0, step, size, step), fill=(45, 45, 60, 255), width=1)

    # Snake body.
    blocks = [(56, 128), (92, 128), (128, 128), (164, 128)]
    for x, y in blocks:
        draw.rounded_rectangle((x, y, x + 28, y + 28), radius=6, fill=(30, 220, 90, 255))

    # Snake eye.
    draw.ellipse((176, 136, 184, 144), fill=(8, 8, 8, 255))

    # Food.
    draw.ellipse((190, 92, 224, 126), fill=(235, 54, 54, 255))

    png_path = assets_dir / "icon.png"
    ico_path = assets_dir / "icon.ico"
    image.save(png_path, format="PNG")
    image.save(ico_path, format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])


if __name__ == "__main__":
    build_icon()
