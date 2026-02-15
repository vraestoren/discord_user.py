import requests
from time import time

class DiscordUser:
    def __init__(self) -> None:
        self.api = "https://discord.com/api/v9"
        self.session = requests.Session()
        self.session.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"
        }
        
    def login(
            self,
            login: str,
            password: str,
            login_source: str = None,
            gift_code_sku_id: str = None) -> dict:
        data = {
            "login": login,
            "password": password,
            "undelete": False,
            "captcha_key": None,
            "login_source": login_source,
            "gift_code_sku_id": gift_code_sku_id
        }
        response = self.session.post(
            f"{self.api}/auth/login", json=data).json()
        if "token" in response:
            self.token = response["token"]
            self.session.headers["Authorization"] = self.token
        return response

    def affinities_users(self) -> dict:
        return self.session.get(
            f"{self.api}/users/@me/affinities/users").json()

    def get_guilds(self) -> dict:
        return self.session.get(
            f"{self.api}/users/@me/guilds").json()

    def get_guild_info(self, guild_id: int) -> dict:
        return self.session.get(
            f"{self.api}/guilds/{guild_id}").json()

    def get_guild_channels(self, guild_id: int) -> dict:
        return self.session.get(
            f"{self.api}/guilds/{guild_id}/channels").json()
    
    def get_account_channels(self) -> dict:
        return self.session.get(
            f"{self.api}/users/@me/channels").json()

    def leave_guild(self, guild_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/users/@me/guilds/{guild_id}").json()

    def leave_channel(self, channel_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/users/@me/channels/{channel_id}").json()

    def discoverable_guilds(
            self,
            offset: int = 0,
            limit: int = 24) -> dict:
        return self.session.get(
            f"{self.api}/discoverable-guilds?offset={offset}&limit={limit}").json()

    def get_relationships(self) -> dict:
        return self.session.get(
            f"{self.api}/users/@me/relationships").json()

    def get_user_info(self, user_id: int) -> dict:
        return self.session.get(
            f"{self.api}/users/{user_id}/profile").json()

    def delete_friend(self, user_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/users/@me/relationships/{user_id}").json()

    def typing_active(self, channel_id: int) -> dict:
        return self.session.get(
            f"{self.api}/channels/{channel_id}/typing").json()

    def change_username(
            self,
            password: str,
            username: str) -> dict:
        data = {
            "password": password,
            "username": username
        }
        return self.session.patch(
            f"{self.api}/users/@me", json=data).json()

    def change_status(
            self,
            emoji_name: str = None,
            text: str = None) -> dict:
        data = {
            "custom_status": {
                "emoji_name": emoji_name,
                "text": text
            }
        }
        return self.session.patch(
            f"{self.api}/users/@me/settings", json=data).json()

    def send_message(
            self,
            content: str,
            channel_id: int) -> dict:
        data = {
            "content": content
        }
        return self.session.post(
            f"{self.api}/channels/{channel_id}/messages",
            json=data).json()

    def delete_message(
            self,
            message_id: int,
            channel_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/channels/{channel_id}/messages/{message_id}").json()

    def get_channel_messages(
            self,
            channel_id: int,
            limit: int = 100) -> dict:
        return self.session.get(
            f"{self.api}/channels/{channel_id}/messages?limit={limit}").json()

    def get_voice_regions(self) -> dict:
        return self.session.get(
            f"{self.api}/voice/regions").text

    def get_guild_bans(self, guild_id: int) -> dict:
        return self.session.get(
            f"{self.api}/guilds/{guild_id}/bans").json()

    def get_guild_users(self, guild_id: int) -> dict:
        return self.session.get(
            f"{self.api}/guilds/{guild_id}/members").json()

    def delete_channel(self, channel_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/channels/{channel_id}").json()
    
    def edit_message(
            self,
            channel_id: int,
            message_id: int,
            content: str) -> dict:
        data = {
            "content": content
        }
        return self.session.patch(
            f"{self.api}/channels/{channel_id}/messages/{message_id}",
            json=data).json()

    def ban_user_from_guild(
            self,
            guild_id: int,
            user_id: int) -> dict:
        return requests.put(
            f"{self.api}/guilds/{guild_id}/bans/{user_id}").json()

    def kick_user_from_guild(
            self,
            guild_id: int,
            user_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/guilds/{guild_id}/members/{user_id}").json()

    def create_role(
            self,
            name: str,
            guild_id: int,
            type: int = 0) -> dict:
        data = {
            "name": name,
            "type": type
        }
        return self.session.post(
            f"{self.api}/guilds/{guild_id}/roles",
            json=data).json()

    def join_guild(self, invite: str) -> dict:
        return self.session.post(
            f"{self.api}/invites/{invite}").json()

    def get_guild_invites(self, guild_id: int) -> dict:
        return self.session.get(
            f"{self.api}/guilds/{guild_id}/invites").json()

    def get_guild_roles(self, guild_id: int) -> dict:
        return self.session.get(
            f"{self.api}/guilds/{guild_id}/roles").json()

    def change_avatar(self, avatar_id: str) -> dict:
        data = {
            "avatar": avatar_id
        }
        return self.session.patch(
            f"{self.api}/users/@me", json=data).json()

    def change_password(
            self,
            old_password: str,
            new_password: str) -> dict:
        data = {
            "new_password": new_password,
            "password": old_password
        }
        return self.session.patch(
            f"{self.api}/users/@me", json=data).json()
