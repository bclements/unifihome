from dataclasses import dataclass
import datetime


@dataclass
class SystemInfo:
    """
    This class is used to store the system information of the controller.
    """
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

    def __post_init__(self):        
        for (name, field_type) in self.__annotations__items():
            if not isinstance(self.__dict__[name], field_type):
                given_type = type(self.__dict__[name])
                raise TypeError(
                    f"The field `{name}` must be `{field_type}` (found `{given_type}`)."
                )


    @classmethod
    def from_api(cls, payload):
        """
        Creates a SystemInfo object from the API payload.
        :param payload: The API payload.
        :return: A SystemInfo object.
        """
        autobackup = payload[0]["autobackup"]
        build = payload[0]["build"]
        console_display_version = payload[0]["console_display_version"]
        data_retention_days = payload[0]["data_retention_days"]
        data_retention_time_in_hours_for_5minutes_scale = payload[0]["data_retention_time_in_hours_for_5minutes_scale"]
        data_retention_time_in_hours_for_daily_scale = payload[0]["data_retention_time_in_hours_for_daily_scale"]
        data_retention_time_in_hours_for_hourly_scale = payload[0]["data_retention_time_in_hours_for_hourly_scale"]
        data_retention_time_in_hours_for_monthly_scale = payload[0]["data_retention_time_in_hours_for_monthly_scale"]
        data_retention_time_in_hours_for_others = payload[0]["data_retention_time_in_hours_for_others"]
        debug_device = payload[0]["debug_device"]
        debug_mgmt = payload[0]["debug_mgmt"]
        debug_sdn = payload[0]["debug_sdn"]
        debug_setting_preference = payload[0]["debug_setting_preference"]
        debug_system = payload[0]["debug_system"]
        default_site_device_auth_password_alert = payload[0]["default_site_device_auth_password_alert"]
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
