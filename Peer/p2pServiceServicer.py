import p2p_pb2_grpc
import p2p_pb2
import grpc
from config import config

class P2PServiceServicer(p2p_pb2_grpc.GreeterServicer):
    def getFile(self, request, context):
        '''
        # getFile(self, request, context) -> fileBytes
        Get the binary of the file requested if it exists else return an error
        ## Arguments
        request: fileRequest -> the request containing the file name
        context: grpc.ServicerContext -> the context of the request
        ## Returns
        fileBytes -> the binary of the file requested
        '''
        conf = config()
        absolute_path = conf.path + request.file_name
        try:
            with open(absolute_path, "rb") as file:
                return p2p_pb2.fileBytes(file_bytes=file.read())
        except FileNotFoundError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("File not found")
            return p2p_pb2.fileBytes(file_bytes=b"")