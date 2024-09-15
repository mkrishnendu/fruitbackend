from bson.objectid import ObjectId

class FAQ:
    def __init__(self, mongo):
        self.collection = mongo.db.faqs

    def create_faq(self, data):
        return self.collection.insert_one(data)

    def get_faq(self, faq_id):
        return self.collection.find_one({'_id': ObjectId(faq_id)})

    def update_faq(self, faq_id, data):
        return self.collection.update_one({'_id': ObjectId(faq_id)}, {'$set': data})

    def delete_faq(self, faq_id):
        return self.collection.delete_one({'_id': ObjectId(faq_id)})

    def get_all_faqs(self):
        return list(self.collection.find())
