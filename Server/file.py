class File:
    def __init__(self, filename:str, Peer: 'Peer') -> None: # type: ignore
        self.filename = filename
        self.Peer = Peer
    
    def __str__(self) -> str:
        return self.filename