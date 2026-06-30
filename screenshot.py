"""
简单截图工具
支持：全屏截图、延迟截图、自定义保存路径
"""

import os
import sys
from datetime import datetime


def ensure_pillow():
    """检查并提示安装 Pillow"""
    try:
        from PIL import ImageGrab
        return True
    except ImportError:
        print("正在安装依赖库 Pillow...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "-q"])
        print("安装完成！\n")
        return True


def take_screenshot(save_dir=None, delay=0):
    """截图并保存"""
    from PIL import ImageGrab

    # 默认保存到脚本所在目录的 screenshots 文件夹
    if save_dir is None:
        save_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
    os.makedirs(save_dir, exist_ok=True)

    # 生成文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(save_dir, f"screenshot_{timestamp}.png")

    if delay > 0:
        print(f"将在 {delay} 秒后截图...")
        import time
        for i in range(delay, 0, -1):
            print(f"  {i}...")
            time.sleep(1)

    print("正在截图...", end=" ")
    screenshot = ImageGrab.grab(all_screens=True)
    screenshot.save(filepath, "PNG")
    print(f"完成！")

    return filepath


def main():
    ensure_pillow()

    print("=" * 45)
    print("  简单截图工具")
    print("=" * 45)
    print()

    while True:
        print("选项：")
        print("  1. 立即全屏截图")
        print("  2. 延迟截图（3秒）")
        print("  3. 延迟截图（5秒）")
        print("  q. 退出")
        print()

        choice = input("请选择> ").strip()

        if choice.lower() == 'q':
            print("再见！")
            break
        elif choice == '1':
            path = take_screenshot()
            print(f"已保存至: {path}\n")
        elif choice == '2':
            path = take_screenshot(delay=3)
            print(f"已保存至: {path}\n")
        elif choice == '3':
            path = take_screenshot(delay=5)
            print(f"已保存至: {path}\n")
        else:
            print("无效选项，请重新选择\n")


if __name__ == "__main__":
    main()
