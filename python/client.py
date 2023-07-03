import grpc
import user_pb2
import user_pb2_grpc

def main():
    print("Python GRPC client started")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        user = user_pb2.User(first_name="Max", last_name="Mustermann", email="max.mustermann@example.com")

        # Erstellen eines Benutzers
        response = stub.CreateUser(user_pb2.CreateUserRequest(user=user))
        print("User created, ID received: ", response.id)

        # Abrufen eines Benutzers
        response = stub.GetUser(user_pb2.GetUserRequest(id=1))
        print("User fetched: ", response.user)

        # Aktualisieren eines Benutzers
        user = user_pb2.User(id=1, first_name="Max", last_name="Mustermann", email="max.updated@example.com")
        response = stub.UpdateUser(user_pb2.UpdateUserRequest(user=user))
        print("User updated.")

        # Löschen eines Benutzers
        response = stub.DeleteUser(user_pb2.DeleteUserRequest(id=1))
        print("User deleted.")

if __name__ == '__main__':
    main()

