import os

MAP_SAVE_PATH = os.path.join(os.path.dirname(__file__), "generated_maps")
MAP_NAME = "%s_%s_map.png"
MAP_MAX_SIZE = 200
MAP_SIZE = 100

HASS_ALLOWED_DEVICES = [
    "light.light",
    "sensor.hl_4150cdn_page_counter",
    "media_player.spotify_fluffy_bean",
    "sensor.pihole_ads_blocked_today",
    "sensor.pihole_ads_percentage_today",
]
