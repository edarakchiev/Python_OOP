class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = ""
        for doc in self.documents:
            result += f"{doc}\n"
        return result

    @staticmethod
    def get_category_by_id(category_list, category_id):
        return [category for category in category_list if category.id == category_id][0]

    @staticmethod
    def get_topic_by_id(topic_list, topic_id):
        return [topic for topic in topic_list if topic.id == topic_id][0]

    @staticmethod
    def get_doc_by_id(doc_list, doc_id):
        return [doc for doc in doc_list if doc.id == doc_id][0]

    @staticmethod
    def get_category_by_id(cat_list, cat_id):
        return [cat for cat in cat_list if cat.id == cat_id][0]

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.get_category_by_id(self.categories, category_id)
        if category:
            category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.get_topic_by_id(self.topics, topic_id)
        if topic:
            topic.storage_folder = new_storage_folder
            topic.topic = new_topic

    def edit_document(self, document_id, new_file_name):
        document = self.get_doc_by_id(self.documents, document_id)
        if document:
            document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.get_category_by_id(self.categories, category_id)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.get_topic_by_id(self.topics, topic_id)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.get_doc_by_id(self.documents, document_id)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        document = self.get_doc_by_id(self.documents, document_id)
        if document:
            return document
