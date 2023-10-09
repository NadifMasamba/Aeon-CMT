from bot import CMD_SUFFIX

class _BotCommands:
    def __init__(self):
        self.StartCommand = '123'
        self.MirrorCommand = [f'12{CMD_SUFFIX}', f'm{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl{CMD_SUFFIX}', f'y{CMD_SUFFIX}']
        self.LeechCommand = [f'leech{CMD_SUFFIX}', f'l{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech{CMD_SUFFIX}', f'yl{CMD_SUFFIX}']
        self.CloneCommand = [f'1234{CMD_SUFFIX}', f'c{CMD_SUFFIX}']
        self.CountCommand = f'321{CMD_SUFFIX}'
        self.DeleteCommand = f'322{CMD_SUFFIX}'
        self.StopAllCommand = [f'stopall{CMD_SUFFIX}', 'stopallbot']
        self.ListCommand = f'534{CMD_SUFFIX}'
        self.SearchCommand = f'765{CMD_SUFFIX}'
        self.StatusCommand = [f'21312{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'398u8{CMD_SUFFIX}'
        self.AuthorizeCommand = f's54{CMD_SUFFIX}'
        self.UnAuthorizeCommand = f'a544{CMD_SUFFIX}'
        self.AddSudoCommand = f'fg45{CMD_SUFFIX}'
        self.RmSudoCommand = f'fdfd56{CMD_SUFFIX}'
        self.PingCommand = [f'ffs65{CMD_SUFFIX}', 'pingall']
        self.RestartCommand = [f'restart{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'afada54{CMD_SUFFIX}', 'statsall']
        self.HelpCommand = f'cadf4231{CMD_SUFFIX}'
        self.LogCommand = f'fdafaf455{CMD_SUFFIX}'
        self.ShellCommand = f'hvih546{CMD_SUFFIX}'
        self.EvalCommand = f'fadfdf34{CMD_SUFFIX}'
        self.ExecCommand = f'fsaf98{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'fsaff8867{CMD_SUFFIX}'
        self.BotSetCommand = f'bsetting{CMD_SUFFIX}'
        self.UserSetCommand = [f'usetting{CMD_SUFFIX}', f'us{CMD_SUFFIX}']
        self.BtSelectCommand = f'safafaa43231{CMD_SUFFIX}'
        self.SpeedCommand = f'speedtest{CMD_SUFFIX}'
        self.RssCommand = f'fsafa7575{CMD_SUFFIX}'
        self.AddImageCommand = f'jhgjgh667{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.MediaInfoCommand = f'mediainfo{CMD_SUFFIX}'
        self.BroadcastCommand = [f'broadcast{CMD_SUFFIX}', 'broadcastall']

BotCommands = _BotCommands()
