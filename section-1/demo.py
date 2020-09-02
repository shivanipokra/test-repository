# from flask import Flask,jsonify,request,render_template             #jsonify coverts data into json format
#
# app = Flask(__name__)       #creating object of flask using unique name
#
# stores =[
#     {
#         'name':'My Wonderful Store',
#         'items':[
#             {
#                 'name':'My Item',
#                 'price': 200
#             }
#         ]
#     }
# ]
#
#
# @app.route('/')
# def home():
#     render_template('index.html')
#
#
# @app.route('/store/<string:name>')
# def get_store(name):
#     # iterate over store
#     for store in stores:
#         # if the store name matches, return it
#         if store['name'] == name:
#             return jsonify(store)
#         # if none match,return an error msg
#     return jsonify({'message':'store not found'})
#
#
# # @app.route('/store')
# # def get_store():
# #     return jsonify({'stores':stores})
#
#
# @app.route('/store',methods=['POST'])
# def create_store():
#     request_data = request.get_json()
#     new_store = {
#         'name': request_data['name'],
#         'items': []
#     }
#     stores.append(new_store)
#     return jsonify(new_store)
#
# @app.route('/store/<string:name>/item')
# def get_item_in_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify({'items':store['items']})
#     return jsonify({'message':'store not found'})
#
#
# @app.route('/store/<string:name>/item',methods=['POST'])
# def create_item_in_store(name):
#     request_data = request.get_json()
#     for store in stores:
#         if store['name'] == name:
#             new_item = {
#                 'name': request_data['name'],
#                 'price': request_data['price']
#             }
#             store['items'].append(new_item)
#             return jsonify(new_item)
#     return jsonify({'message':'store not found'})
#
# app.run(port=5000,debug=True)




from flask import Flask,jsonify,request,render_template         #jsonify coverts data into json format

app = Flask(__name__)           #creating object of flask using unique name

stores = [{
    'name': 'My Store',
    'items': [{
        'name':'my item',
        'price': 15.99
    }]
}]

@app.route('/')
def home():
  return render_template('index.html')

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)
  #pass

#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
    # iterate over store
  for store in stores:
      # if the store name matches, return it
    if store['name'] == name:
          return jsonify(store)
      # if none match,return an error msg
  return jsonify ({'message': 'store not found'})
  #pass

#get /store
@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})
  #pass

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})
  #pass

#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message':'store not found'})

  #pass

app.run(debug=True,port=5000)