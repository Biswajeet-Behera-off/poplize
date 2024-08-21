import flet as ft

# Function to create the Home page content
def home_page(go_back):
    return ft.Column(
        controls=[
            # Header Section
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text("Hamster Kombat", color=ft.colors.WHITE, size=20, weight="bold"),
                        ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    height=50
                ),
                bgcolor=ft.colors.BLACK
            ),
            # Profile Section
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.CircleAvatar(radius=20, bgcolor=ft.colors.BLUE),
                        ft.Column(
                            controls=[
                                ft.Text("Biswajeet Behera (CEO)", color=ft.colors.WHITE),
                                ft.Text("Grandmaster • 9/11", color=ft.colors.GREEN, size=10),
                            ],
                            spacing=5
                        )
                    ],
                    spacing=10,
                    # padding=ft.Padding(top=10, right=10, bottom=10, left=10)
                ),
                bgcolor=ft.colors.BLACK
            ),
            # Card Section
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text("Daily reward", color=ft.colors.WHITE),
                        bgcolor=ft.colors.BLUE_GREY, width=80, height=100, 
                    ),
                    ft.Container(
                        content=ft.Text("Daily cipher", color=ft.colors.WHITE),
                        bgcolor=ft.colors.RED, width=80, height=100, 
                    ),
                    ft.Container(
                        content=ft.Text("Daily combo", color=ft.colors.WHITE),
                        bgcolor=ft.colors.PURPLE, width=80, height=100, 
                    ),
                    ft.Container(
                        content=ft.Text("Mini game", color=ft.colors.WHITE),
                        bgcolor=ft.colors.GREEN, width=80, height=100, 
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                # padding=ft.Padding(10)
            ),
            # Coin Section
            ft.Container(
                content=ft.Text("599,438,529", color=ft.colors.YELLOW, size=30, weight="bold"),
                alignment=ft.alignment.center,
                # padding=ft.Padding(10)
            ),
        ],
        expand=True,
    )

# Function to create the Game page content
def game_page(go_back):
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.ARROW_BACK, icon_color=ft.colors.WHITE, on_click=lambda e: go_back()),
                        ft.Text("Game Page", color=ft.colors.WHITE, size=20, weight="bold"),
                        ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    height=50
                ),
                bgcolor=ft.colors.BLACK
            ),
            ft.Text("Game Page", color=ft.colors.GREY, size=30, weight="bold"),
            # Add more content for Game page here
        ],
        expand=True
    )

# Function to create the Friend page content
def friend_page(go_back):
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.ARROW_BACK, icon_color=ft.colors.WHITE, on_click=lambda e: go_back()),
                        ft.Text("Friend Page", color=ft.colors.WHITE, size=20, weight="bold"),
                        ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    height=50
                ),
                bgcolor=ft.colors.BLACK
            ),
            ft.Text("Friend Page", color=ft.colors.GREY, size=30, weight="bold"),
            # Add more content for Friend page here
        ],
        expand=True
    )

# Function to create the Earn page content
def earn_page(go_back):
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.ARROW_BACK, icon_color=ft.colors.WHITE, on_click=lambda e: go_back()),
                        ft.Text("Earning Page", color=ft.colors.WHITE, size=20, weight="bold"),
                        ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    height=50
                ),
                bgcolor=ft.colors.BLACK
            ),
            ft.Text("Earn Page", color=ft.colors.GREY, size=30, weight="bold"),
            # Add more content for Earn page here
        ],
        expand=True
    )

# Function to create the Save page content
def save_page(go_back):
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.ARROW_BACK, icon_color=ft.colors.WHITE, on_click=lambda e: go_back()),
                        ft.Text("Save Money", color=ft.colors.WHITE, size=20, weight="bold"),
                        ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    height=50
                ),
                bgcolor=ft.colors.BLACK
            ),
            ft.Text("Save Page", color=ft.colors.GREY, size=30, weight="bold"),
            # Add more content for Save page here
        ],
        expand=True
    )

# Main function to build the app
def main(page: ft.Page):
    # Initial setup for the page
    page.title = "Hamster Kombat"
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Create a dictionary to map page names to their content
    def get_page(page_name):
        pages = {
            "home": home_page(go_back),
            "game": game_page(go_back),
            "friend": friend_page(go_back),
            "earn": earn_page(go_back),
            "save": save_page(go_back)
        }
        return pages[page_name]

    # This will store the currently visible page
    current_page = ft.Ref[ft.Column]()

    # This list will keep track of the navigation history
    history = ["home"]

    # Function to switch pages
    def switch_page(page_name):
        # If we're switching to a new page, add the current page to the history
        if page_name != history[-1]:
            history.append(page_name)
        current_page.current.controls = [get_page(page_name)]
        page.update()

    # Function to go back to the previous page
    def go_back():
        if len(history) > 1:
            history.pop()  # Remove the current page from history
            previous_page = history[-1]  # Get the previous page
            current_page.current.controls = [get_page(previous_page)]
            page.update()

    # Define the navigation bar
    nav_bar = ft.Row(
        controls=[
            ft.IconButton(icon=ft.icons.HOME_FILLED, tooltip="Home", icon_color=ft.colors.GREY, selected_icon_color=ft.colors.YELLOW, on_click=lambda e: switch_page("home")),
            ft.IconButton(icon=ft.icons.GAMEPAD, tooltip="Game", icon_color=ft.colors.GREY,selected_icon_color=ft.colors.YELLOW, on_click=lambda e: switch_page("game")),
            ft.IconButton(icon=ft.icons.PEOPLE, tooltip="Friend", icon_color=ft.colors.GREY,selected_icon_color=ft.colors.YELLOW, on_click=lambda e: switch_page("friend")),
            ft.IconButton(icon=ft.icons.CURRENCY_EXCHANGE, tooltip="Earn", icon_color=ft.colors.GREY,selected_icon_color=ft.colors.YELLOW, on_click=lambda e: switch_page("earn")),
            ft.IconButton(icon=ft.icons.SAVINGS, tooltip="Save", icon_color=ft.colors.GREY,selected_icon_color=ft.colors.YELLOW, on_click=lambda e: switch_page("save")),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        height=50,
    )
    def on_change(e):
        page.session.set("current_page", e.control.selected_index)
        current_page.current = e.control.selected_index

    navigation = ft.NavigationBar(
                selected_index=current_page.current,
                destinations=[
                    ft.IconButton(icon=ft.icons.HOME_FILLED, tooltip="Home", icon_color=ft.colors.GREY, selected_icon_color=ft.colors.YELLOW, on_click=lambda e: switch_page("home")),
                    ft.IconButton(icon=ft.icons.GAMEPAD, tooltip="Game", icon_color=ft.colors.GREY,selected_icon_color=ft.colors.YELLOW, on_click=lambda e: switch_page("game")),
                    ft.IconButton(icon=ft.icons.PEOPLE, tooltip="Friend", icon_color=ft.colors.GREY,selected_icon_color=ft.colors.YELLOW, on_click=lambda e: switch_page("friend")),
                    ft.IconButton(icon=ft.icons.CURRENCY_EXCHANGE, tooltip="Earn", icon_color=ft.colors.GREY,selected_icon_color=ft.colors.YELLOW, on_click=lambda e: switch_page("earn")),
                    ft.IconButton(icon=ft.icons.SAVINGS, tooltip="Save", icon_color=ft.colors.GREY,selected_icon_color=ft.colors.YELLOW, on_click=lambda e: switch_page("save")),
                ],
                on_change=on_change,
                height=50,
            )
    

    # Initialize with the Home page
    current_page.current = get_page("home")

    # Add the current page and the navigation bar to the page
    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=current_page.current,
                    expand=True,
                ),
                nav_bar
            ],
            expand=True,
        )
    )

# Run the app
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
