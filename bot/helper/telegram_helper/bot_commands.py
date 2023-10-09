from bot import CMD_SUFFIX

class _BotCommands:
    def __init__(self):
        self.YtdlCommand = [f'ytdl{CMD_SUFFIX}', f'y{CMD_SUFFIX}']
        self.LeechCommand = [f'leech{CMD_SUFFIX}', f'l{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech{CMD_SUFFIX}', f'yl{CMD_SUFFIX}']        
        self.StopAllCommand = [f'stopall{CMD_SUFFIX}', 'stopallbot']        
        self.RestartCommand = [f'restart{CMD_SUFFIX}', 'restartall']        
        self.BotSetCommand = f'bsetting{CMD_SUFFIX}'
        self.UserSetCommand = [f'usetting{CMD_SUFFIX}', f'us{CMD_SUFFIX}']        
        self.SpeedCommand = f'speedtest{CMD_SUFFIX}'        
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.MediaInfoCommand = f'mediainfo{CMD_SUFFIX}'       

BotCommands = _BotCommands()
