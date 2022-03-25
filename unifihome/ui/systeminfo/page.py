from rich.console import Group, RenderableType
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from textual._context import active_app
from textual.widget import Widget

#from ...model.systeminfo import SystemInfo
#from ..systeminfo.backup import BackupInfoWidget
#from ..systeminfo.build import BuildInfoWidget
#from ..systeminfo.misc import MiscInfoWidget
#from ..systeminfo.network import NetworkInfoWidget


#class PageWidget(Widget):
#    def render(self) -> RenderableType:
#        systeminfo = SystemInfo.from_api(
#            active_app.get().unifi_controller.get_sysinfo()
#        )
#        networkWidget = NetworkInfoWidget(data=systeminfo)
#        buildWidget = BuildInfoWidget(data=systeminfo)
#        backupWidget = BackupInfoWidget(data=systeminfo)
#        miscWidget = MiscInfoWidget(data=systeminfo)

#        self.table = Table(expand=True, show_header=False, padding=0, box=None)
#        self.table.add_column(no_wrap=True, ratio=1)
#        self.table.add_column(no_wrap=True)
#        self.table.add_column(no_wrap=True)
#        self.table.add_row(buildWidget, backupWidget, "")
#        self.table.add_row(networkWidget, miscWidget, "")
#        self.group = Group(self.table, "")
#        return Padding(
#            Panel(self.group, title="Unifi System Information"), (1, 0, 0, 0)
#        )
