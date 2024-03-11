data = {
    "items": [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"}
    ]
}

def get_items():
    return data

def add_item(item):
    data['items'].append(item)
    return item

def get_item_by_id(item_id):
    items = data['items']
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return item, 200
    return {'message': 'Item not found'}, 404
