from mcdreforged.api.all import *

def executeCommand(server: PluginServerInterface, command: str):
    is_rcon_running = server.is_rcon_running()
    if is_rcon_running:
        rcon_info = server.rcon_query(command)
        if rcon_info:
            server.logger.info(f"Command: {command} executed, result: {rcon_info}")
        else:
            server.logger.info(f"Command: {command} executed, result: None")
    else:
        server.execute_command(command)

def on_load(server: PluginServerInterface, prev):
    # !!pickaxe 命令，获取331钻石镐
    def pickaxe(src, ctx):
        # If is console, send a message to the console
        if not src.is_player:
            server.logger.info("[pickaxe] You must be a player to use this command")
        else:
            command = "give {player} diamond_pickaxe{{display:{{Name:'{{\"text\":\"331钻石镐子\", \"color\":\"aqua\"}}'}}, Enchantments:[{{id:\"minecraft:efficiency\",lvl:3}}, {{id:\"minecraft:unbreaking\",lvl:3}}, {{id:\"minecraft:mending\",lvl:1}}]}} 1".format(player=src.player)
            executeCommand(server, command)

    # Register help message for !!pickaxe command
    server.register_help_message('!!pickaxe', '获取331钻石镐')
    # Register !!pickaxe command
    server.register_command(
        # Set command
        Literal('!!pickaxe').runs(pickaxe)
    )
