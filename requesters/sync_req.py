import grpc
from config import sample_pb2_grpc, sample_pb2


def run_sync(how_much: int):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = sample_pb2_grpc.GitHubServiceStub(channel)

        for _ in range(how_much):
            stub.GetRepository(
                sample_pb2.RepositoryRequest(owner="openai", name="ChatGPT")
            )
