import datetime
import json
from dataclasses import dataclass

from rich.console import Group, RenderableType
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from textual._context import active_app
from textual.widget import Widget

"""
Dataclasses to use in widgets # Refactor this to be in it's own model class file
"""

@dataclass
class SystemInfo:
    console_display_version: str
    debug_sdn: str
    debug_setting_preference: str
    debug_system: str
    default_site_device_auth_password_alert: bool
    facebook_wifi_registered: bool
    has_webrtc_support: bool
    hostname: str
    https_port: str
    image_maps_use_google_engine: bool
    inform_port: str
    ip_addrs: list
    is_cloud_console: bool
    live_chat: str
    name: str
    override_inform_host: bool
    previous_version: str
    radius_disconnect_running: bool
    sso_app_id: str
    sso_app_sec: str
    store_enabled: str
    timezone: str
    ubnt_device_type: str
    udm_version: str
    unifi_go_enabled: bool
    unsupported_device_count: int
    unsupported_device_list: list
    update_available: str
    update_downloaded: str
    uptime: int
    version: str  
    

class UnifiSystemInfo(Widget):
    def render(self) -> RenderableType:
        systeminfo = active_app.get().unifi_controller.get_sysinfo()
        self.table = Table(expand=True, show_header=False, padding=0, box=None)
        self.table.add_column("1", no_wrap=True, ratio=1)
        self.table.add_column("2", no_wrap=True)
        self.table.add_column("3", no_wrap=True)
        self.table.add_row(
            self.render_buildinfo(systeminfo[0]),
            self.render_miscinfo(systeminfo[0]),
            "",
        )
        self.table.add_row(self.render_networkinfo(systeminfo[0]), "", "")
        self.group = Group(self.table, "")
        return Padding(
            Panel(self.group, title="Unifi System Information"), (1, 0, 0, 0)
        )

    def render_networkinfo(self, si):
        content = f'[b]Hostname[/b]: {si["hostname"]}\n' f"[b]IP Address(es)[/b]:\n"
        for ip in si["ip_addrs"]:
            content = content + f"\t{ip}\n"
        content_1 = (
            f'\n[b]HTTP Port[/b]: {si["https_port"]}\n'
            f'[b]Inform Port:[/b] {si["inform_port"]}'
        )
        content = content + content_1
        return Panel(
            content,
            title="Network Information",
            title_align="left",
            border_style="blue",
        )

    def render_buildinfo(self, si):
        updateAvailable = f"Yes" if si["update_available"] else f" No"
        content = (
            f'[b]Version[/b]: {si["version"]}\n'
            f'[b]Build[/b]: {si["build"]}\n'
            f"[b]Update Available?[/b]{updateAvailable}\n"
            f'[b]Device:[/b] {si["ubnt_device_type"]}'
        )
        return Panel(
            content,
            title="Buid Information",
            title_align="left",
            border_style="bold blue",
        )

    def render_miscinfo(self, si):
        uptime = str(datetime.timedelta(seconds=si["uptime"]))
        content = f'[b]Timezone:[/b] {si["timezone"]}\n'
        content = content + f"[b]Uptime:[/b] {uptime}"
        return Panel(
            content, title="Misc. Information", title_align="left", border_style="blue"
        )
