from mycroft import MycroftSkill, intent_file_handler


class Introduction(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('introduction.intent')
    def handle_introduction(self, message):
        self.speak_dialog('introduction')


def create_skill():
    return Introduction()

