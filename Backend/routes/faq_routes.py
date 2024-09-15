from flask import request, jsonify
from bson import ObjectId
from flask_cors import CORS
from models.faq import FAQ 

def faq_routes(app, mongo):
    CORS(app)

    faq_model = FAQ(mongo)

    # Create a new FAQ
    @app.route('/faqs', methods=['POST'])
    def create_faq():
        data = request.get_json()

        if 'question' not in data or 'answer' not in data:
            return jsonify({'message': 'Question and answer are required'}), 400

        try:
            faq_id = faq_model.create_faq(data)
            return jsonify({'message': 'FAQ created successfully', 'id': str(faq_id)}), 201
        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to create FAQ'}), 500

    # Get a single FAQ by ID
    @app.route('/faqs/<faq_id>', methods=['GET'])
    def get_faq(faq_id):
        if not ObjectId.is_valid(faq_id):
            return jsonify({'message': 'Invalid FAQ ID'}), 400

        faq = faq_model.get_faq(faq_id)
        if faq:
            faq['_id'] = str(faq['_id'])
            return jsonify(faq), 200
        return jsonify({'message': 'FAQ not found'}), 404

    # Update a FAQ by ID
    @app.route('/faqs/<faq_id>', methods=['PUT'])
    def update_faq(faq_id):
        if not ObjectId.is_valid(faq_id):
            return jsonify({'message': 'Invalid FAQ ID'}), 400

        data = request.get_json()

        if not data:
            return jsonify({'message': 'No data provided to update'}), 400

        try:
            result = faq_model.update_faq(faq_id, data)
            if result:
                return jsonify({'message': 'FAQ updated successfully'}), 200
            return jsonify({'message': 'FAQ not found'}), 404
        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to update FAQ'}), 500

    # Delete a FAQ by ID
    @app.route('/faqs/<faq_id>', methods=['DELETE'])
    def delete_faq(faq_id):
        if not ObjectId.is_valid(faq_id):
            return jsonify({'message': 'Invalid FAQ ID'}), 400

        try:
            result = faq_model.delete_faq(faq_id)
            if result:
                return jsonify({'message': 'FAQ deleted successfully'}), 200
            return jsonify({'message': 'FAQ not found'}), 404
        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to delete FAQ'}), 500

    # Get all FAQs
    @app.route('/faqs', methods=['GET'])
    def get_all_faqs():
        try:
            faqs = faq_model.get_all_faqs()
            for faq in faqs:
                faq['_id'] = str(faq['_id'])
            return jsonify(faqs), 200
        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to retrieve FAQs'}), 500
