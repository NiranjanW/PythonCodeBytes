
from http import HTTPStatus
from flask import Blueprint, Flask
from flask_restx import Api , Resource , Model, fields , marshal_with
from typing import TypedDict

blueprint = Blueprint("api",__name__,url_prefix="/api/v1")

api = Api (blueprint, version="1.0",title="Mini REST API",description="A Mini Rest Api")
ns = api.namespace("items" , description="Item Operations")
api.add_namespace(ns)


detail_model = api.model("Detail", {"id": fields.Integer, "name": fields.String})
item_model = api.model(
    "Item",
    {
        "id": fields.Integer,
        "name": fields.String,
        "details": fields.List(fields.Nested(detail_model)),
    },
)

item_parser = api.parser()
item_parser.add_argument("id", type=int, location="form")
item_parser.add_argument("name", type=str, location="form")

detail_parser = api.parser()
detail_parser.add_argument("id", type=int, location="form")
detail_parser.add_argument("name", type=str, location="form")

# Types
class ItemDetails(TypedDict):
    """
    TypedDict for item details
    """

    id: int
    name: str


class Item(TypedDict):
    """
    TypedDict for item
    """

    id: int
    name: str
    details: list[ItemDetails]


# Memory "Database"
memory_object: list[Item] = [
    {
        "id": 1,
        "name": "Item 2",
        "details": [
            {"id": 1, "name": "Detail 1"},
            {"id": 2, "name": "Detail 2"},
        ],
    }
]


class ItemApi(Resource):
    @api.response(HTTPStatus.OK.value , "Get Item")
    @api.marshal_list_with(item_model)
    def get(self) -> list[Item]:
        """
        Returns the memory object
        """
        return memory_object

    @api.response(HTTPStatus.OK.value, "Object added")
    @api.expect(item_parser)
    def post(self) -> None:
        """
        Simple append something to the memory object
        """
        args = item_parser.parse_args()
        memory_object.append(args)


app = Flask(__name__)  # This line already exists
app.register_blueprint(blueprint)

app.run()