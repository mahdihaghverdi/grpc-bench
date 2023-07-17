import asyncio

import grpc
from config import sample_pb2_grpc, sample_pb2


async def run_async(how_much: int):
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = sample_pb2_grpc.GitHubServiceStub(channel)

        tasks = [
            stub.GetRepository(
                sample_pb2.RepositoryRequest(owner="openai", name="ChatGPT")
            )
            for _ in range(how_much)
        ]
        await asyncio.gather(*tasks, return_exceptions=True)
