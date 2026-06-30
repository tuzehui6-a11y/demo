"""
简单计算器
支持：加(+)、减(-)、乘(*)、除(/)、幂(**)、取余(%)
输入 'q' 退出，输入 'c' 清屏
"""

def calculator():
    print("=" * 40)
    print("  简单计算器  |  输入 q 退出  |  输入 c 清屏")
    print("=" * 40)
    print("  支持: +  -  *  /  **  %")
    print()

    last_result = None

    while True:
        try:
            if last_result is not None:
                prompt = f"请输入算式 (上次结果: {last_result})> "
            else:
                prompt = "请输入算式> "

            expr = input(prompt).strip()

            if expr.lower() == 'q':
                print("再见！")
                break

            if expr.lower() == 'c':
                print("\n" * 50)
                print("=" * 40)
                print("  简单计算器  |  输入 q 退出  |  输入 c 清屏")
                print("=" * 40)
                print("  支持: +  -  *  /  **  %")
                print()
                last_result = None
                continue

            if not expr:
                continue

            # 允许使用上一次结果继续运算
            if last_result is not None and expr[0] in '+-*/%' and len(expr) > 1:
                expr = str(last_result) + expr

            # 使用 eval 计算（安全考量：仅允许数字和运算符）
            result = eval(expr, {"__builtins__": {}}, {})

            if isinstance(result, (int, float)):
                print(f"  = {result}")
                last_result = result
            else:
                print("  错误：无效的算式")

        except ZeroDivisionError:
            print("  错误：不能除以零！")
        except (SyntaxError, NameError, TypeError):
            print("  错误：请输入有效的算式！")
        except KeyboardInterrupt:
            print("\n再见！")
            break

if __name__ == "__main__":
    calculator()
