from rich.panel import Panel
from textual._context import active_app
from textual.reactive import Reactive
from textual.widget import Widget


class Main(Widget):

    value = Reactive("")

    def render(self) -> Panel:
        return Panel(str(self.value))

    def clear(self) -> None:
        self.value = ""

    def get_sys_info(self) -> None:
        c = active_app.get().unifi_controller
        systeminfo = c.get_sysinfo()
        from rich.console import Console

        console = Console()
        with console.capture() as capture:
            for i in systeminfo[0]:
                console.print(f"{i}", f"{systeminfo[0][i]}")

        self.value = capture.get()
