from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from models.item_models import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
         type=float,
         required=True,
         help="This field cannot be left blank"
        )
    parser.add_argument('store_id',
         type=int,
         required=True,
         help="Every item must have a store ID"
        )

    @jwt_required()
    def get(self,name):
        # for item in items:
        #     if item['name']==name:
        #         return item
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item does not exist'}, 404

        # item = next(filter(lambda x: x['name']==name, items), None)
        # return {'item': item}, 200 if item else 404

    # @classmethod
    # def find_by_name(cls,name):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "SELECT * from items where name=?"
    #     result = cursor.execute(query, (name,))
    #     row = result.fetchone()        
    #     connection.close()

    #     if row:
    #         return {'item' : {'name': row[0], 'price':row[1]}}

    def post(self,name):       
        if ItemModel.find_by_name(name):
            return {'message': "Item with name '{}' already present.".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'],data['store_id'])
       
        try:
            item.save_to_db()
        except:
            return {'message': 'An Error Occurred while inserting'}, 500
        
        return item.json(), 201
        # if next(filter(lambda x: x['name']==name, items), None) is not None:
        #     return {'message': "Item with name '{}' already present.".format(name)}, 400

        # data = Item.parser.parse_args()

        # item = {'name' : name, 'price': data['price']}
        # items.append(item)
        # return item, 201

    # @classmethod
    # def insert(cls,item):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "INSERT INTO items VALUES (?,?)"
    #     cursor.execute(query, (item['name'], item['price']))

    #     connection.commit()
    #     connection.close()

    # DELETE an ITEM from the Table Items
    def delete(self,name):
        item = ItemModel.find_by_name(name) 
       
        #     return {'message': "Item with name '{}' is not present. Cannot Delete non-existing item".format(name)}, 400
        if item:
            item.delete_from_db()
        # # items = list(filter(lambda x: x['name'] != name, items))
        return {'message': "Item Deleted"}

    def put(self,name):        
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
       
#        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])        
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        
        item.save_to_db()
            
        return item.json()

    # @classmethod
    # def update(cls, item):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cursor.execute(query, (item['price'],item['name']))

    #     connection.commit()
    #     connection.close()

# Resource to get the details of all the Items together
class ItemList(Resource):
    @jwt_required()
    def get(self):
        
        return {'items' : [item.json() for item in ItemModel.query.all()]}

        # 'item' : list(map(lambda x: x.json(), ItemModel.query.all())) Alternative method

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name': row[0], 'price': row[1]})


        # connection.close()
        
        #return {'items': items}

        # for item in items:
        #     return {'Items' : items}
        # return {'Items' : None}, 404
        