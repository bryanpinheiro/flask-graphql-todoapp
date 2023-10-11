# main.py

from flask import Flask
from flask_graphql import GraphQLView
from graphql_schema import schema

# Create a Flask app
app = Flask(__name__)
app.debug = True

# Bind the GraphQL view to a URL endpoint
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
