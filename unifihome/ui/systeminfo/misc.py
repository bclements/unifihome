from rich.console import RenderableType
from rich.panel import Panel
from textual.widget import Widget


class MiscInfoWidget(Widget):
    """
    This is a widget that displays miscellaneous information about the bot.
    :return: A panel containing the miscellaneous information.
    """

    def __init__(self, *args, data, refresh_rate, **kwargs) -> None:
        self.data = data
        super().__init__(*args, **kwargs)

    def render(self) -> RenderableType:
        content = f"[b]Timezone:[/b] {self.data.timezone}\n"
        content = content + f"[b]Uptime:[/b] {self.data.uptime}"
        return Panel(
            content, title="Misc. Information", title_align="left", border_style="blue"
        )
