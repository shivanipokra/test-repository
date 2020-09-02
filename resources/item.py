import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import JWT,jwt_required
from models.item import ItemModel


class Item(Resource):
    print("hello")
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True)
    parser.add_argument('store_id', type=int, required=True)

    # data = parser.parse_args()

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'},404



    def post(self,name):
        if ItemModel.find_by_name(name):
        # if next(filter(lambda x: x['name']== name,items),None) is not None:
            return {'message': "An item with name '{}' already exists".format(name)}, 400         #400 is bad request

        data = Item.parser.parse_args()

        # item = ItemModel(name, data['price'],data['store_id'])
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {'message':"An error occurred inserting the item"},500   #internal server error

        return item.json(), 201         #201 means object is created


    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'item deleted'}

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "DELETE FROM items WHERE name =?"
        # cursor.execute(query,(name,))
        # connection.commit()
        # connection.close()
        #
        # return {'message':'item deleted'}

    def put(self,name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name,data['price'])

        if item is None:
            item = ItemModel(name,data['price'],data['store_id'])
            # try:
            #     updated_item.insert()
            # except:
            #     return {'message': 'An error occurred inserting the item'},500
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()
            # try:
            #     updated_item.update()
            # except:
            #     return {'message': 'An error occurred inserting the item'}, 500

        # return updated_item.json()


class ItemList(Resource):
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all()]}
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []
        #
        # for row in result:
        #     items.append({'name':row[0],'price':row[1]})
        #
        # connection.close()
        #
        # return {'items':items}