from requests import Session

class DiscordUser:
	def __init__(self) -> None:
		self.api = "https://discord.com/api/v9"
		self.session = Session()
		self.session.headers = {
			"Content-Type": "application/json",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"
		}

	def _post(self, endpoint: str, data: dict = None) -> dict:
		return self.session.post(f"{self.api}{endpoint}", json=data).json()

	def _get(self, endpoint: str, params: dict = None) -> dict:
		return self.session.get(f"{self.api}{endpoint}", params=params).json()

	def _patch(self, endpoint: str, data: dict = None) -> dict:
		return self.session.patch(f"{self.api}{endpoint}", json=data).json()

	def _delete(self, endpoint: str) -> dict:
		return self.session.delete(f"{self.api}{endpoint}").json()

	def _put(self, endpoint: str, data: dict = None) -> dict:
		return self.session.put(f"{self.api}{endpoint}", json=data).json()

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
		response = self._post("/auth/login", data)
		if "token" in response:
			self.token = response["token"]
			self.session.headers["Authorization"] = self.token
		return response

	def affinities_users(self) -> dict:
		return self._get("/users/@me/affinities/users")

	def get_guilds(self) -> dict:
		return self._get("/users/@me/guilds")

	def get_guild_info(self, guild_id: int) -> dict:
		return self._get(f"/guilds/{guild_id}")

	def get_guild_channels(self, guild_id: int) -> dict:
		return self._get(f"/guilds/{guild_id}/channels")

	def get_account_channels(self) -> dict:
		return self._get("/users/@me/channels")

	def leave_guild(self, guild_id: int) -> dict:
		return self._delete(f"/users/@me/guilds/{guild_id}")

	def leave_channel(self, channel_id: int) -> dict:
		return self._delete(f"/users/@me/channels/{channel_id}")

	def discoverable_guilds(
			self,
			offset: int = 0,
			limit: int = 24) -> dict:
		params = {
			"offset": offset,
			"limit": limit
		}
		return self._get("/discoverable-guilds", params)

	def get_relationships(self) -> dict:
		return self._get("/users/@me/relationships")

	def get_user_info(self, user_id: int) -> dict:
		return self._get(f"/users/{user_id}/profile")

	def delete_friend(self, user_id: int) -> dict:
		return self._delete(f"/users/@me/relationships/{user_id}")

	def typing_active(self, channel_id: int) -> dict:
		return self._post(f"/channels/{channel_id}/typing")

	def change_username(
			self,
			password: str,
			username: str) -> dict:
		data = {
			"password": password,
			"username": username
		}
		return self._patch("/users/@me", data)

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
		return self._patch("/users/@me/settings", data)

	def send_message(
			self,
			content: str,
			channel_id: int) -> dict:
		data = {
			"content": content
		}
		return self._post(
            f"/channels/{channel_id}/messages", data)

	def delete_message(
			self,
			message_id: int,
			channel_id: int) -> dict:
		return self._delete(
			f"/channels/{channel_id}/messages/{message_id}")

	def get_channel_messages(
			self,
			channel_id: int,
			limit: int = 100) -> dict:
		params = {
			"limit": limit
		}
		return self._get(
			f"/channels/{channel_id}/messages", params)

	def get_voice_regions(self) -> dict:
		return self._get("/voice/regions")

	def get_guild_bans(self, guild_id: int) -> dict:
		return self._get(f"/guilds/{guild_id}/bans")

	def get_guild_users(self, guild_id: int) -> dict:
		return self._get(f"/guilds/{guild_id}/members")

	def delete_channel(self, channel_id: int) -> dict:
		return self._delete(f"/channels/{channel_id}")

	def edit_message(
			self,
			channel_id: int,
			message_id: int,
			content: str) -> dict:
		data = {
			"content": content
		}
		return self._patch(
			f"/channels/{channel_id}/messages/{message_id}", data)

	def ban_user_from_guild(
			self,
			guild_id: int,
			user_id: int) -> dict:
		return self._put(f"/guilds/{guild_id}/bans/{user_id}")

	def kick_user_from_guild(
			self,
			guild_id: int,
			user_id: int) -> dict:
		return self._delete(f"/guilds/{guild_id}/members/{user_id}")

	def create_role(
			self,
			name: str,
			guild_id: int,
			role_type: int = 0) -> dict:
		data = {
			"name": name,
			"type": role_type
		}
		return self._post(f"/guilds/{guild_id}/roles", data)

	def join_guild(self, invite: str) -> dict:
		return self._post(f"/invites/{invite}")

	def get_guild_invites(self, guild_id: int) -> dict:
		return self._get(f"/guilds/{guild_id}/invites")

	def get_guild_roles(self, guild_id: int) -> dict:
		return self._get(f"/guilds/{guild_id}/roles")

	def change_avatar(self, avatar_id: str) -> dict:
		data = {
			"avatar": avatar_id
		}
		return self._patch(f"/users/@me", data)

	def change_password(
			self,
			old_password: str,
			new_password: str) -> dict:
		data = {
			"password": old_password,
			"new_password": new_password
		}
		return self._patch(f"/users/@me", data)
