class Youtube:
    def __init__(self, channel_id, channel_name, channel_description):
        self.channel_id = 123
        self.channel_name = "panavesity"
        self.channel_description = "This is a channel about panavesity"

    def get_channel_info(self):
        return f"Channel ID: {self.channel_id}, Channel Name: {self.channel_name}, Channel Description: {self.channel_description}"
