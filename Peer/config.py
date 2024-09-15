import yaml

class config:
    def __init__(self,path: str = None) -> None:
        if path is None:
            path = 'config.yaml'
        with open(path) as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
            self.token = config['auth']['token']
            self.control_port = config['control']['port']
            self.dataPort = config['peer']['port']
            self.ip = config['control']['ip']
            self.path = config['peer']['path']
