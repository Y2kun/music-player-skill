from mycroft import MycroftSkill, intent_file_handler


class MusicPlayer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('player.music.intent')
    def handle_player_music(self, message):
        self.speak_dialog('player.music')


def create_skill():
    return MusicPlayer()

