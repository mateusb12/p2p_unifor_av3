from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import graphene
from graphql import graphql
import uvicorn

from technologies.mock_data import users


# Define GraphQL types
class UserType(graphene.ObjectType):
    name = graphene.String()
    email = graphene.String()
    friends = graphene.List(graphene.String)
    posts = graphene.List(graphene.String)
    activity = graphene.JSONString()

    def resolve_friends(self, info):
        return self.friends

    def resolve_posts(self, info):
        return self.posts

    def resolve_activity(self, info):
        return self.activity


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.String(required=True))

    async def resolve_user(self, info, id):
        return users.get(id)


schema = graphene.Schema(query=Query)
app = FastAPI()


@app.post("/graphql")
async def graphql_server(request: Request):
    data = await request.json()
    query = data.get("query")
    variables = data.get("variables")
    context = {"request": request}
    result = await graphql(schema.graphql_schema, query, context_value=context, variable_values=variables)
    if result.errors:
        return JSONResponse({"errors": [str(error) for error in result.errors]})
    return JSONResponse({"data": result.data})


# To run the server: uvicorn your_script_name:app --reload
if __name__ == "__main__":
    uvicorn.run("technologies.graph_ql:app", host="127.0.0.1", port=8000, reload=True)
