from rich.console import RenderableType
from rich.panel import Panel
from textual._context import active_app
from textual.widget import Widget


class BackupInfoWidget(Widget):
    """
    This is a widget that displays the retention details of the backups.
    :return: A panel containing the details.
    """

    def __init__(self, *args, data, **kwargs) -> None:
        self.data = data
        super().__init__(*args, **kwargs)

    def render(self) -> RenderableType:
        content = (
            f"[b]Configured Days of Retention:[/b] {self.data.data_retention_days}\n"
            f"[b]Currently storing {len(active_app.get().unifi_controller.get_backups())} backups"
        )
        return Panel(
            content, title="Retention Details", title_align="left", border_style="blue"
        )
