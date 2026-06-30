# Demo

一个 Python 小工具合集，包含简单计算器和截图工具。

## 功能

### 🧮 计算器 (`calculator.py`)

支持基础运算的命令行计算器：

| 运算符 | 说明   |
| ------ | ------ |
| `+`    | 加法   |
| `-`    | 减法   |
| `*`    | 乘法   |
| `/`    | 除法   |
| `**`   | 幂运算 |
| `%`    | 取余   |

**特色功能：**
- 保存上次计算结果，可用 `+5`、`*2` 等快捷方式继续运算
- 输入 `q` 退出，输入 `c` 清屏

```bash
python calculator.py
```

### 📸 截图工具 (`screenshot.py`)

支持全屏截图，支持延迟截图（3/5 秒）。

```bash
python screenshot.py
```

截图自动保存到 `screenshots/` 目录，文件名包含时间戳。

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/tuzehui6-a11y/demo.git
cd demo

# 运行计算器
python calculator.py

# 运行截图工具（首次会自动安装 Pillow）
python screenshot.py
```

## 环境要求

- Python 3.6+
- Pillow（截图工具依赖，首次运行自动安装）
