# SPDX-License-Identifier: GPL-3.0-only
# Copyright 2023 Marek Kraus <gamelaster@outlook.com>

from gi.repository import GLib, Gio

bus = Gio.bus_get_sync(Gio.BusType.SESSION, None)


def emit_launcher_entry_update_signal(params):
    bus.emit_signal(
        None,  # sender
        "/",  # object path
        "com.canonical.Unity.LauncherEntry",  # interface name
        "Update",  # signal name
        params,  # parameters
    )


def on_launcher_entry_update_signal_handler(*args):
    unpacked = args[5].unpack()
    app_uri = unpacked[0]

    if app_uri == "application://discord.desktop":
        params = GLib.Variant.parse(
            None,
            args[5]
            .print_(True)
            .replace(
                "application://discord.desktop", "application://discord-canary.desktop"
            ),
        )
        emit_launcher_entry_update_signal(params)


bus.signal_subscribe(
    None,
    "com.canonical.Unity.LauncherEntry",
    None,
    None,
    None,
    Gio.DBusSignalFlags.NONE,
    on_launcher_entry_update_signal_handler,
)

mainloop = GLib.MainLoop()
mainloop.run()
