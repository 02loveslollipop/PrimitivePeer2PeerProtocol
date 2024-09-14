import yaml

class config:
    def __init__(self) -> None:
        with open('config.yaml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
            self.token = config['auth']['token']
            self.control_port = config['control']['port']
            self.dataPort = config['peer']['port']         
