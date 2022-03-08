from plugins import PluginList
from utils import get_json_from_github

PLUGINS_JSON_FILE = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json"


def get_community_plugins() -> PluginList:
    plugin_list = get_json_from_github(PLUGINS_JSON_FILE)
    return plugin_list
