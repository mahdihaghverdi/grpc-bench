import asyncio

import grpc

from config import sample_pb2_grpc, sample_pb2


class GitHubServicer(sample_pb2_grpc.GitHubServiceServicer):
    async def GetRepository(self, request, context):
        owner = request.owner
        name = request.name
        # Perform GitHub API request or any desired logic
        description = f"Description of {owner}/{name}"
        return sample_pb2.RepositoryResponse(name=name, description=description)


async def serve():
    server = grpc.aio.server()
    sample_pb2_grpc.add_GitHubServiceServicer_to_server(GitHubServicer(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
