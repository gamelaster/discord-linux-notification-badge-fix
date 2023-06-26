 # Discord Linux notification badge fix

 ![Example on KDE](example-on-kde.png)

 When I moved from Windows to Linux, I really missed the notification badge, which contains how many new messages you have.\
 Of course, I installed `libunity`, but nothing worked. I tested both Discord Stable and Canary, but on both it did not worked.

 So I took a look on DBUS events, and find out, instead of using `application://discord-canary.desktop`, it uses just `application://discord.desktop`.
 (NOTE: I use only `discord-canary`, I don't know what issue is with Discord Stable). This Python script listens for those signals, and if any `discord.desktop` signal is received,
 it creates same signal but with `discord-canary.desktop` app id.

# Installation

Requirements:

- libunity (`libunity` on AUR, `libunity-dev` on Debian/Ubuntu)
- Python3

Run:

```bash
python3 discord-linux-notification-badge-fix.py
```

# Service

To be done...
