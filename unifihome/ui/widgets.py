import datetime
from dataclasses import dataclass

from rich.console import Group, RenderableType
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from textual._context import active_app
from textual.widget import Widget
import logging
from pprint import pformat

logging.basicConfig(filename="unifihome.log", filemode="a", level=logging.DEBUG)

"""
Dataclasses to use in widgets # Refactor this to be in it's own model class file
"""


@dataclass
class SystemInfo:
    autobackup: str
    build: str
    console_display_version: str
    data_retention_days: int
    data_retention_time_in_hours_for_5minutes_scale: int
    data_retention_time_in_hours_for_daily_scale: int
    data_retention_time_in_hours_for_hourly_scale: int
    data_retention_time_in_hours_for_monthly_scale: int
    data_retention_time_in_hours_for_others: int
    debug_device: str
    debug_mgmt: str
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

    @classmethod
    def from_api(cls, payload):
        autobackup = payload[0]["autobackup"]
        build = payload[0]["build"]
        console_display_version = payload[0]["console_display_version"]
        data_retention_days = payload[0]["data_retention_days"]
        data_retention_time_in_hours_for_5minutes_scale = payload[0][
            "data_retention_time_in_hours_for_5minutes_scale"
        ]
        data_retention_time_in_hours_for_daily_scale = payload[0][
            "data_retention_time_in_hours_for_daily_scale"
        ]
        data_retention_time_in_hours_for_hourly_scale = payload[0][
            "data_retention_time_in_hours_for_hourly_scale"
        ]
        data_retention_time_in_hours_for_monthly_scale = payload[0][
            "data_retention_time_in_hours_for_monthly_scale"
        ]
        data_retention_time_in_hours_for_others = payload[0][
            "data_retention_time_in_hours_for_others"
        ]
        debug_device = payload[0]["debug_device"]
        debug_mgmt = payload[0]["debug_mgmt"]
        debug_sdn = payload[0]["debug_sdn"]
        debug_setting_preference = payload[0]["debug_setting_preference"]
        debug_system = payload[0]["debug_system"]
        default_site_device_auth_password_alert = payload[0][
            "default_site_device_auth_password_alert"
        ]
        facebook_wifi_registered = payload[0]["facebook_wifi_registered"]
        has_webrtc_support = payload[0]["has_webrtc_support"]
        hostname = payload[0]["hostname"]
        https_port = payload[0]["https_port"]
        image_maps_use_google_engine = payload[0]["image_maps_use_google_engine"]
        inform_port = payload[0]["inform_port"]
        ip_addrs = payload[0]["ip_addrs"]
        is_cloud_console = payload[0]["is_cloud_console"]
        live_chat = payload[0]["live_chat"]
        name = payload[0]["name"]
        override_inform_host = payload[0]["override_inform_host"]
        previous_version = payload[0]["previous_version"]
        radius_disconnect_running = payload[0]["radius_disconnect_running"]
        sso_app_id = payload[0]["sso_app_id"]
        sso_app_sec = payload[0]["sso_app_sec"]
        store_enabled = payload[0]["store_enabled"]
        timezone = payload[0]["timezone"]
        ubnt_device_type = payload[0]["ubnt_device_type"]
        udm_version = payload[0]["udm_version"]
        unifi_go_enabled = payload[0]["unifi_go_enabled"]
        unsupported_device_count = payload[0]["unsupported_device_count"]
        unsupported_device_list = payload[0]["unsupported_device_list"]
        update_available = "Yes" if payload[0]["update_available"] else "No"
        update_downloaded = "Yes" if payload[0]["update_downloaded"] else "No"
        uptime = str(datetime.timedelta(seconds=payload[0]["uptime"]))
        version = payload[0]["version"]

        return cls(
            autobackup=autobackup,
            build=build,
            console_display_version=console_display_version,
            data_retention_days=data_retention_days,
            data_retention_time_in_hours_for_5minutes_scale=data_retention_time_in_hours_for_5minutes_scale,
            data_retention_time_in_hours_for_daily_scale=data_retention_time_in_hours_for_daily_scale,
            data_retention_time_in_hours_for_hourly_scale=data_retention_time_in_hours_for_hourly_scale,
            data_retention_time_in_hours_for_monthly_scale=data_retention_time_in_hours_for_monthly_scale,
            data_retention_time_in_hours_for_others=data_retention_time_in_hours_for_others,
            debug_device=debug_device,
            debug_mgmt=debug_mgmt,
            debug_sdn=debug_sdn,
            debug_setting_preference=debug_setting_preference,
            debug_system=debug_system,
            default_site_device_auth_password_alert=default_site_device_auth_password_alert,
            facebook_wifi_registered=facebook_wifi_registered,
            has_webrtc_support=has_webrtc_support,
            hostname=hostname,
            https_port=https_port,
            image_maps_use_google_engine=image_maps_use_google_engine,
            inform_port=inform_port,
            ip_addrs=ip_addrs,
            is_cloud_console=is_cloud_console,
            live_chat=live_chat,
            name=name,
            override_inform_host=override_inform_host,
            previous_version=previous_version,
            radius_disconnect_running=radius_disconnect_running,
            sso_app_id=sso_app_id,
            sso_app_sec=sso_app_sec,
            store_enabled=store_enabled,
            timezone=timezone,
            ubnt_device_type=ubnt_device_type,
            udm_version=udm_version,
            unifi_go_enabled=unifi_go_enabled,
            unsupported_device_count=unsupported_device_count,
            unsupported_device_list=unsupported_device_list,
            update_available=update_available,
            update_downloaded=update_downloaded,
            uptime=uptime,
            version=version,
        )


class UnifiSystemInfo(Widget):
    def render(self) -> RenderableType:
        si = SystemInfo.from_api(active_app.get().unifi_controller.get_sysinfo())
        self.table = Table(expand=True, show_header=False, padding=0, box=None)
        self.table.add_column("1", no_wrap=True, ratio=1)
        self.table.add_column("2", no_wrap=True)
        self.table.add_column("3", no_wrap=True)
        self.table.add_row(
            self.render_buildinfo(si),
            Group(self.render_miscinfo(si), self.render_retentioninfo(si)),
            "",
        )
        self.table.add_row(
            self.render_networkinfo(si),
            "" "",
        )
        self.group = Group(self.table, "")
        return Padding(
            Panel(self.group, title="Unifi System Information"), (1, 0, 0, 0)
        )

    def render_networkinfo(self, si):
        content = f"[b]Hostname[/b]: {si.hostname}\n" f"[b]IP Address(es)[/b]:\n"
        for ip in si.ip_addrs:
            content = content + f"\t{ip}\n"
        content_1 = (
            f"\n[b]HTTP Port[/b]: {si.https_port}\n"
            f"[b]Inform Port:[/b] {si.inform_port}"
        )
        content = content + content_1
        return Panel(
            content,
            title="Network Information",
            title_align="left",
            border_style="blue",
        )

    def render_buildinfo(self, si):
        content = (
            f"[b]System Name[/b]: {si.name}\n"
            f"[b]Version[/b]: {si.version}\n"
            f"[b]Build[/b]: {si.build}\n"
            f"[b]UDM Version[/b]: {si.udm_version}\n"
            f"[b]Update Available?[/b] {si.update_available}\n"
            f"[b]Device:[/b] {si.ubnt_device_type}"
        )
        return Panel(
            content,
            title="Buid Information",
            title_align="left",
            border_style="bold blue",
        )

    def render_retentioninfo(self, si):
        content = (
            f"[b]Configured Days of Retention:[/b] {si.data_retention_days}\n"
            f"[b]Currently storing {len(active_app.get().unifi_controller.get_backups())} backups"
        )
        return Panel(
            content, title="Retention Details", title_align="left", border_style="blue"
        )

    def render_miscinfo(self, si):
        content = f"[b]Timezone:[/b] {si.timezone}\n"
        content = content + f"[b]Uptime:[/b] {si.uptime}"
        return Panel(
            content, title="Misc. Information", title_align="left", border_style="blue"
        )
