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
            
    # !!haste 命令，获取急迫2效果
    def haste(src, ctx):
        if not src.is_player:
            server.logger.info("[haste] You must be a player to use this command")
        else:
            command = "effect give {player} haste 1000000 1".format(player=src.player)
            executeCommand(server, command)
            
    # !!food 命令，获取食物
    def food(src, ctx):
        if not src.is_player:
            server.logger.info("[food] You must be a player to use this command")
        else:
            command = "give {player} cooked_beef 128".format(player=src.player)
            executeCommand(server, command)
            
    # !!transport 命令，获取鞘翅和烟花
    def transport(src, ctx):
        if not src.is_player:
            server.logger.info("[transport] You must be a player to use this command")
        else:
            command = "give {player} elytra{{Enchantments:[{{id:\"minecraft:unbreaking\",lvl:3}}, {{id:\"minecraft:mending\",lvl:1}}]}} 1".format(player=src.player)
            executeCommand(server, command)
            command = "give {player} firework_rocket 384".format(player=src.player)
            executeCommand(server, command)

    # Register help message for !!pickaxe command
    server.register_help_message('!!pickaxe', '获取331钻石镐')
    server.register_help_message('!!haste', '获取急迫2效果')
    server.register_help_message('!!food', '获取食物')
    server.register_help_message('!!transport', '获取鞘翅和烟花')
    # Register !!pickaxe command
    server.register_command(
        # Set command
        Literal('!!pickaxe').runs(pickaxe)
    )
    server.register_command(
        Literal('!!haste').runs(haste)
    )
    server.register_command(
        Literal('!!food').runs(food)
    )
    server.register_command(
        Literal('!!transport').runs(transport)
    )
