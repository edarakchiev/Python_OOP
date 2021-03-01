from player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.list_players = []

    def assign_player(self, player: Player):
        if not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        self.list_players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        filtered_names = [p.name for p in self.list_players]
        if player_name not in filtered_names:
            return f"Player {player_name} is not in the guild."
        else:
            del self.list_players[player_name.index(player_name)]
            #player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for el in self.list_players:
            result += el.player_info()
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
guild.kick_player("George")
print(guild.guild_info())
