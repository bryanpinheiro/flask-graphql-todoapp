# graphql_schema.py

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Todo as TodoModel
from todo_dao import TodoDAO
from todo_dto import TodoDTO


class Todo(SQLAlchemyObjectType):
    class Meta:
        model = TodoModel


class TodoInput(graphene.InputObjectType):
    title = graphene.String(required=True)


class Query(graphene.ObjectType):
    todos = graphene.List(Todo)
    todo = graphene.Field(Todo, todo_id=graphene.Int(required=True))

    @staticmethod
    def resolve_todos(self, info):
        todo_dao = TodoDAO()
        todos = todo_dao.get_all_todos()
        return todos

    @staticmethod
    def resolve_todo(self, info, todo_id):
        todo_dao = TodoDAO()
        todo = todo_dao.get_todo_by_id(todo_id=todo_id)
        return todo


class CreateTodoMutation(graphene.Mutation):
    class Arguments:
        todo_input = TodoInput(required=True)

    todo = graphene.Field(Todo)

    @staticmethod
    def mutate(self, info, todo_input):
        todo_dao = TodoDAO()
        todo_dao.create_todo(title=todo_input.title)
        return None


class UpdateTodoMutation(graphene.Mutation):
    class Arguments:
        todo_id = graphene.Int(required=True)
        todo_input = TodoInput(required=True)

    todo = graphene.Field(Todo)

    @staticmethod
    def mutate(self, info, todo_id, todo_input):
        todo_dao = TodoDAO()
        todo_dao.update_todo(todo_id=todo_id, data=todo_input)
        return None


class DeleteTodoMutation(graphene.Mutation):
    class Arguments:
        todo_id = graphene.Int(required=True)

    todo = graphene.Field(Todo)

    @staticmethod
    def mutate(self, info, todo_id):
        todo_dao = TodoDAO()
        todo_dao.delete_todo(todo_id=todo_id)
        return None


class Mutation(graphene.ObjectType):
    create_todo = CreateTodoMutation.Field()
    update_todo = UpdateTodoMutation.Field()
    delete_todo = DeleteTodoMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
