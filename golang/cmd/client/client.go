package main

import (
    "context"
    "log"
    "time"

    pb "github.com/derphilipp/grpc_workshop/user"

    "google.golang.org/grpc"
)

func main() {
    log.Printf("Starting grpc client")
    conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure(), grpc.WithBlock())
    if err != nil {
        log.Fatalf("did not connect: %v", err)
    }
    defer conn.Close()

    c := pb.NewUserServiceClient(conn)
    log.Printf("Connection to server started")

    ctx, cancel := context.WithTimeout(context.Background(), time.Second)
    defer cancel()

    createUserResponse, err := c.CreateUser(ctx, &pb.CreateUserRequest{User: &pb.User{FirstName: "Max", LastName: "Mustermann", Email: "max.mustermann@example.com"}})
    if err != nil {
        log.Fatalf("could not create user: %v", err)
    }
    log.Printf("User created, ID received: %d", createUserResponse.Id)

    getUserResponse, err := c.GetUser(ctx, &pb.GetUserRequest{Id: createUserResponse.Id})
    if err != nil {
        log.Fatalf("could not fetch user: %v", err)
    }
    log.Printf("User fetched: %v", getUserResponse.User)

    _, err = c.UpdateUser(ctx, &pb.UpdateUserRequest{User: &pb.User{Id: createUserResponse.Id, FirstName: "Max", LastName: "Mustermann", Email: "max.updated@example.com"}})
    if err != nil {
        log.Fatalf("could not update user: %v", err)
    }
    log.Printf("User updated")

    _, err = c.DeleteUser(ctx, &pb.DeleteUserRequest{Id: createUserResponse.Id})
    if err != nil {
        log.Fatalf("could not delete user: %v", err)
    }
    log.Printf("User deleted")
}

