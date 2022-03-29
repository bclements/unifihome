from rich.console import RenderableType
from rich.panel import Panel
from textual.widget import Widget


class BuildInfoWidget(Widget):
    """
    This is a widget that displays the build information of the system.
    :param data: The data that is to be displayed.
    :return: A panel containing the data.
    """

    def __init__(self, *args, data, **kwargs) -> None:
        self.data = data
        super().__init__(*args, **kwargs)

    def render(self) -> RenderableType:
        content = (
            f"[b]System Name[/b]: {self.data.name}\n"
            f"[b]Version[/b]: {self.data.version}\n"
            f"[b]Build[/b]: {self.data.build}\n"
            f"[b]UDM Version[/b]: {self.data.udm_version}\n"
            f"[b]Update Available?[/b] {self.data.update_available}\n"
            f"[b]Device:[/b] {self.data.ubnt_device_type}"
        )
        return Panel(
            content,
            title="Buid Information",
            title_align="left",
            border_style="bold blue",
        )
