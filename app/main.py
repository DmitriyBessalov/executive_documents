import strawberry
import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from settings import Graphql
from graphql_app.mutation import Mutation
from graphql_app.query import Query

app = FastAPI()


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)


graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host=Graphql.host,
        port=Graphql.port,
        reload=Graphql.debug,
        use_colors=Graphql.debug,
    )
