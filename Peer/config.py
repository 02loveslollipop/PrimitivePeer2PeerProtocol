import yaml

class config:
    def __init__(self) -> None:
        with open('config.yaml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
            self.master_ip = config['control']['ip']
            self.seed = config['control']['seed']
            self.control_port = config['control']['port']
            self.data_port = config['data']['port']
            self.data_path = config['self']['path']
            
            
@staticmethod
        