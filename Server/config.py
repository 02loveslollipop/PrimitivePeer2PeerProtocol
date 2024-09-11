import yaml

class config:
    def __init__(self) -> None:
        with open('config.yaml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
            self.masterIp = config['control']['ip']
            self.seed = config['control']['seed']
            self.control_port = config['control']['port']
            self.dataPort = config['data']['port']
            self.dataPath = config['self']['path']
            self.ttl = config['self']['ttl']            
