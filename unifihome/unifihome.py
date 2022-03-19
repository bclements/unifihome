import click
from pyunifi.controller import Controller
from textual import events
from textual.app import App
from textual.widgets import ScrollView
import constants
from ui.footer import Footer
from ui.main import Main
from ui.title import Title
from rich.table import Table
from rich.console import Console


class UnifiHome(App):
    def __init__(self, *args, credentials, **kwargs):
        self.credentials = credentials
        self.unifi_controller = Controller(
            "192.168.1.1", self.credentials["username"], self.credentials["password"]
        )
        self.pending_event = None
        super().__init__(*args, **kwargs)

    async def on_load(self, event: events.Load) -> None:
        await self.bind("i", "get_system_info", "Unifi System Info")        
        await self.bind("c", "clear","Clear Screen")
        await self.bind("q", "quit", "Quit")
        await self.bind("h", "display_help", "Help")
        
    async def on_mount(self, event: events.Mount) -> None:
        self.header = Title()
        self.main = Main()
        self.footer = Footer()
        await self.view.dock(self.header, edge="top")
        await self.view.dock(self.footer, edge="bottom")
        await self.view.dock(self.main, name="main")

    def show_info(self) -> None:           
        self.main.get_sys_info()


    def action_get_system_info(self) -> None:
        self.show_info()

    def action_clear(self) -> None:
        self.main.clear()

@click.command()
@click.option("--username", required=True)
@click.option("--password", required=True)
def UnifiHomeStart(username, password):
    creds = {"username": username, "password": password}
    print("Unifi Home is starting")
    UnifiHome.run(title=f"Unifi Home v{constants.VERSION}-b{constants.BUILD}", log="textual.log", credentials=creds)


if __name__ == "__main__":
    UnifiHomeStart()
