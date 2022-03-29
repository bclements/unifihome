from rich.console import RenderableType
from rich.panel import Panel
from textual.widget import Widget


class NetworkInfoWidget(Widget):
    def __init__(self, *args, data, **kwargs) -> None:
        self.data = data
        super().__init__(*args, **kwargs)

    def render(self) -> RenderableType:
        content = f"[b]Hostname[/b]: {self.data.hostname}\n" f"[b]IP Address(es)[/b]:\n"
        for ip in self.data.ip_addrs:
            content = content + f"\t{ip}\n"
        content_1 = (
            f"\n[b]HTTP Port[/b]: {self.data.https_port}\n"
            f"[b]Inform Port:[/b] {self.data.inform_port}"
        )
        content = content + content_1
        return Panel(
            content,
            title="Network Information",
            title_align="left",
            border_style="blue",
        )
