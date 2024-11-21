# 菜单
menu = {
    1: {"name": "汉堡", "price": 15},
    2: {"name": "薯条", "price": 10},
    3: {"name": "炸鸡", "price": 20},
    4: {"name": "可乐", "price": 8},
    5: {"name": "冰淇淋", "price": 12}
}

# 订单存储
order = []

# 打印菜单
def show_menu():
    print("\n===== 菜单 =====")
    for item_id, details in menu.items():
        print(f"{item_id}. {details['name']} - {details['price']} 元")
    print("=================")

# 添加餐品到订单
def add_to_order():
    try:
        item_id = int(input("\n请输入餐品编号添加到订单（0 返回主菜单）："))
        if item_id == 0:
            return
        if item_id in menu:
            quantity = int(input(f"您选择了 {menu[item_id]['name']}，请输入数量："))
            if quantity > 0:
                order.append({"name": menu[item_id]["name"], "price": menu[item_id]["price"], "quantity": quantity})
                print(f"{menu[item_id]['name']} x{quantity} 已添加到订单！")
            else:
                print("数量必须大于 0，请重新输入。")
        else:
            print("无效的餐品编号，请重新选择！")
    except ValueError:
        print("输入无效，请输入数字！")

# 查看订单
def show_order():
    if not order:
        print("\n您的订单为空！")
    else:
        print("\n===== 当前订单 =====")
        total_price = 0
        for item in order:
            item_total = item["price"] * item["quantity"]
            total_price += item_total
            print(f"{item['name']} x{item['quantity']} - {item_total} 元")
        print(f"总金额：{total_price} 元")
        print("===================")

# 结算订单
def checkout():
    if not order:
        print("\n您的订单为空，无法结算！")
    else:
        show_order()
        confirm = input("确认结算吗？（y/n）：").strip().lower()
        if confirm == "y":
            print("订单已结算，谢谢光临！")
            order.clear()
        else:
            print("订单未结算，返回主菜单。")

# 主程序
def main():
    while True:
        print("\n===== 点餐系统 =====")
        print("1. 查看菜单")
        print("2. 添加餐品")
        print("3. 查看订单")
        print("4. 结算订单")
        print("0. 退出系统")
        print("===================")

        try:
            choice = int(input("请输入您的选择："))
            if choice == 1:
                show_menu()
            elif choice == 2:
                show_menu()
                add_to_order()
            elif choice == 3:
                show_order()
            elif choice == 4:
                checkout()
            elif choice == 0:
                print("谢谢使用，再见！")
                break
            else:
                print("无效的选项，请重新选择！")
        except ValueError:
            print("输入无效，请输入数字！")

# 启动程序
if __name__ == "__main__":
    main()

    main()