import flet as ft

def main(page: ft.Page):
    page.title = "Выбор параметров"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 500
    page.window_resizable = False
    page.padding = 20
    
    # Глобальные переменные для хранения выбранных значений
    selected_time = None
    selected_amount = None
    
    # Функция для открытия окна с выбором времени
    def open_time_window(e):
        def time_window_handler(time_page: ft.Page):
            time_page.title = "Выбор времени суток"
            time_page.window_width = 300
            time_page.window_height = 250
            time_page.window_resizable = False
            time_page.padding = 20
            
            time_result = ft.Text("", size=16)
            
            def select_day(e):
                nonlocal selected_time
                selected_time = "День"
                time_result.value = f"Выбрано: День"
                time_result.color = ft.colors.GREEN
                time_page.update()
            
            def select_night(e):
                nonlocal selected_time
                selected_time = "Ночь"
                time_result.value = f"Выбрано: Ночь"
                time_result.color = ft.colors.GREEN
                time_page.update()
            
            def close_window(e):
                time_page.window_close()
            
            time_page.add(
                ft.Column([
                    ft.Text("Выберите время суток:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Row([
                        ft.ElevatedButton("День", on_click=select_day, width=100),
                        ft.ElevatedButton("Ночь", on_click=select_night, width=100),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    time_result,
                    ft.Divider(height=20),
                    ft.ElevatedButton("Закрыть окно", on_click=close_window),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )
        
        ft.app(target=time_window_handler, view=ft.WEB_BROWSER)
    
    # Функция для открытия окна с выбором суммы
    def open_amount_window(e):
        def amount_window_handler(amount_page: ft.Page):
            amount_page.title = "Выбор суммы выручки"
            amount_page.window_width = 350
            amount_page.window_height = 400
            amount_page.window_resizable = False
            amount_page.padding = 20
            
            amount_result = ft.Text("", size=16)
            
            def select_amount(amount):
                def inner(e):
                    nonlocal selected_amount
                    selected_amount = amount
                    amount_result.value = f"Выбрано: {amount:,} ₽".replace(",", " ")
                    amount_result.color = ft.colors.GREEN
                    amount_page.update()
                return inner
            
            def close_window(e):
                amount_page.window_close()
            
            # Кнопки с суммами
            amounts = [10000, 12000, 15000, 17000, 19000, 21000, 23000]
            amount_buttons = []
            
            for amount in amounts:
                amount_buttons.append(
                    ft.ElevatedButton(
                        f"{amount:,} ₽".replace(",", " "),
                        on_click=select_amount(amount),
                        width=120,
                    )
                )
            
            amount_page.add(
                ft.Column([
                    ft.Text("Выберите сумму выручки:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Column(amount_buttons, spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Divider(height=20),
                    amount_result,
                    ft.Divider(height=10),
                    ft.ElevatedButton("Закрыть окно", on_click=close_window),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)
            )
        
        ft.app(target=amount_window_handler, view=ft.WEB_BROWSER)
    
    # Функция для отображения результатов
    def show_results(e):
        if selected_time is None or selected_amount is None:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Пожалуйста, выберите время суток и сумму выручки!"),
                bgcolor=ft.colors.RED_400
            )
            page.snack_bar.open = True
            page.update()
            return
        
        # Показываем результаты на главной странице
        result_text.value = f"Выбрано: {selected_time}, {selected_amount:,} ₽".replace(",", " ")
        result_text.color = ft.colors.GREEN
        page.update()
    
    # Элементы главной страницы
    result_text = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
    
    # Добавляем элементы на главную страницу
    page.add(
        ft.Column([
            ft.Text("Приложение для выбора параметров", 
                   size=22, 
                   weight=ft.FontWeight.BOLD,
                   text_align=ft.TextAlign.CENTER),
            ft.Divider(height=30),
            
            ft.Text("Шаг 1: Выберите время суток", size=16),
            ft.ElevatedButton(
                "Открыть окно выбора времени",
                on_click=open_time_window,
                icon=ft.icons.ACCESS_TIME,
                width=250,
            ),
            
            ft.Divider(height=20),
            
            ft.Text("Шаг 2: Выберите сумму выручки", size=16),
            ft.ElevatedButton(
                "Открыть окно выбора суммы",
                on_click=open_amount_window,
                icon=ft.icons.ATTACH_MONEY,
                width=250,
            ),
            
            ft.Divider(height=30),
            
            ft.ElevatedButton(
                "ОТПРАВИТЬ",
                on_click=show_results,
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.BLUE_400,
                    color=ft.colors.WHITE,
                ),
                width=200,
                height=50,
            ),
            
            ft.Divider(height=20),
            result_text,
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)