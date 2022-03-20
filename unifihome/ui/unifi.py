from rich.console import RenderableType
from rich.panel import Panel
from rich.table import Table
from textual._context import active_app
from textual.widget import Widget
from rich.padding import Padding

"""
Various Unifi Home Widgets
"""


class UnifiSystemInfo(Widget):
    def render(self) -> RenderableType:
        c = active_app.get().unifi_controller
        systeminfo = c.get_sysinfo()
        table = Table(expand=True, show_header=False, show_lines=False, show_edge=False)
        table.add_column(width=1)
        table.add_column(width=1)
        table.add_column(width=1)
        table.add_row(
            self.render_buildinfo(systeminfo[0]),
            self.render_networkinfo(systeminfo[0]),
            "",
        )
        return Padding(Panel(table, title="Unifi System Information"), (1, 0, 0, 0))

    def render_networkinfo(self, si):
        content = (
            f'[b]Hostname[/b]: {si["hostname"]}\n[b]IP Address[/b]: {si["ip_addrs"][0]}'
        )
        return Panel(content, title="Network Information")

    def render_buildinfo(self, si):
        updateAvailable = f"Yes" if si["update_available"] else f"No"
        content = f'[b]Version[/b]: {si["version"]}\n[b]Build[/b]: {si["build"]}\n[b]Update Available? {updateAvailable}'
        return Panel(content, title="Build")
