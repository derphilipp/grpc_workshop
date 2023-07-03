from concurrent import futures
import grpc
import user_pb2
import user_pb2_grpc

class UserService(user_pb2_grpc.UserServiceServicer):

    def CreateUser(self, request, context):
        return user_pb2.CreateUserResponse(id=1)

    def GetUser(self, request, context):
        return user_pb2.GetUserResponse(user=user_pb2.User(id=1, first_name="Max", last_name="Mustermann", email="max.mustermann@example.com"))

    def UpdateUser(self, request, context):
        return user_pb2.UpdateUserResponse()

    def DeleteUser(self, request, context):
        return user_pb2.DeleteUserResponse()

def serve():
    print("Starting GRPC Python server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
