<div align="center">
  <img src="https://discord.com/assets/847541504914fd33810e70a0ea73177e.ico" height="60">
  <h1>discord_user.py</h1>


> Web-API for the [Discord](https://discord.com) user API (v9)

---

## Usage

```python
from discord_user import DiscordUser

client = DiscordUser()
client.login("email@example.com", "password")
```

---

## Methods

### Auth

| Method | Description |
|--------|-------------|
| `login(login, password, login_source, gift_code_sku_id)` | Log in and set session token |

---

### Account

| Method | Description |
|--------|-------------|
| `change_username(password, username)` | Change account username |
| `change_password(old_password, new_password)` | Change account password |
| `change_avatar(avatar_id)` | Change account avatar |
| `change_status(emoji_name, text)` | Set a custom status |
| `affinities_users()` | Get user affinities |
| `get_relationships()` | Get friends/relationships |
| `delete_friend(user_id)` | Remove a friend |
| `get_user_info(user_id)` | Get a user's profile |

---

### Guilds

| Method | Description |
|--------|-------------|
| `get_guilds()` | List all joined guilds |
| `get_guild_info(guild_id)` | Get info about a guild |
| `get_guild_channels(guild_id)` | List channels in a guild |
| `get_guild_users(guild_id)` | List members in a guild |
| `get_guild_roles(guild_id)` | List roles in a guild |
| `get_guild_bans(guild_id)` | List bans in a guild |
| `get_guild_invites(guild_id)` | List invites in a guild |
| `join_guild(invite)` | Join a guild by invite code |
| `leave_guild(guild_id)` | Leave a guild |
| `ban_user_from_guild(guild_id, user_id)` | Ban a user from a guild |
| `kick_user_from_guild(guild_id, user_id)` | Kick a user from a guild |
| `create_role(name, guild_id, role_type)` | Create a role in a guild |
| `discoverable_guilds(offset, limit)` | Browse public/discoverable guilds |

---

### Channels & Messages

| Method | Description |
|--------|-------------|
| `get_account_channels()` | List all DM channels |
| `leave_channel(channel_id)` | Leave / close a channel |
| `delete_channel(channel_id)` | Delete a channel |
| `send_message(content, channel_id)` | Send a message |
| `edit_message(channel_id, message_id, content)` | Edit a message |
| `delete_message(message_id, channel_id)` | Delete a message |
| `get_channel_messages(channel_id, limit)` | Fetch messages from a channel |
| `typing_active(channel_id)` | Trigger the typing indicator |

---

### Voice

| Method | Description |
|--------|-------------|
| `get_voice_regions()` | List available voice regions |

---

## Example

```python
from discord_user import DiscordUser

client = DiscordUser()
client.login("email@example.com", "password")

# Send a message
client.send_message("Hello!", channel_id=1234567890)

# Change status
client.change_status(emoji_name="🔥", text="coding")

# Get all guilds
guilds = client.get_guilds()
print(guilds)
```
</div>
