import click
from pyunifi.controller import Controller
from textual import events
from textual.app import App

import constants
from ui.footer import Footer
from ui.main import Main
from ui.title import Title


class UnifiHome(App):
    def __init__(self, *args, credentials, refresh_rate, **kwargs):
        self.credentials = credentials
        self.refresh_rate = refresh_rate
        self.unifi_controller = Controller(
            self.credentials["host"],
            self.credentials["username"],
            self.credentials["password"],
        )
        self.pending_event = None
        super().__init__(*args, **kwargs)

    async def on_load(self, event: events.Load) -> None:
        await self.bind("i", "get_system_info", "Unifi System Info")
        await self.bind("c", "clear", "Clear Screen")
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
@click.option("-h", required=True, envvar="UNIFI_HOSTNAME")
@click.option("-u", required=True, envvar="UNIFI_USERNAME")
@click.option("-p", required=True, envvar="UNIFI_PASSWORD")
@click.option(
    "-s",
    default="default",
    required=False,
    envvar="UNIFI_SITE",
    help="Unifi Site name [Default: default]",
)
@click.option(
    "-r",
    default=30,
    required=False,
    envvar="UNIFI_REFRESH",
    help="Refresh rate in seconds [Default: 30 seconds]",
)
def main(h, u, p, r):
    credentials = {"host": h, "username": u, "password": p}
    print("Unifi Home is starting")
    UnifiHome.run(
        title=f"Unifi Home v{constants.VERSION}-b{constants.BUILD}",
        log="textual.log",
        credentials=credentials,
        refresh_rate=r,
    )


if __name__ == "__main__":
    main()
