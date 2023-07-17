from concurrent import futures

import grpc

from config import sample_pb2_grpc, sample_pb2


class GitHubServicer(sample_pb2_grpc.GitHubServiceServicer):
    def GetRepository(self, request, context):
        owner = request.owner
        name = request.name
        # Perform GitHub API request or any desired logic
        description = f"Description of {owner}/{name}"
        return sample_pb2.RepositoryResponse(name=name, description=description)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_GitHubServiceServicer_to_server(GitHubServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
