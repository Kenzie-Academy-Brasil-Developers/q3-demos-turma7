import pymongo
from bson.objectid import ObjectId


# Database URI
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["turma7"]


class Dev:
    def __init__(self, *args, **kwargs) -> None:
        self.nome = kwargs["nome"]
        self.email = kwargs["email"]

    def post_dev(self):
        db.devs.insert_one(self.__dict__)

    @staticmethod
    def delete_dev(dev_id):
        deleted_dev = db.devs.find_one_and_delete({"_id": ObjectId(dev_id)})
        # print("DELETED DEV -> ", deleted_dev)
        # print("TYPE DELETED DEV -> ", type(deleted_dev))
        return deleted_dev

    @staticmethod
    def serialize_dev(data):
        if type(data) is list:
            for dev in data:
                dev.update({"_id": str(dev["_id"])})
        elif type(data) is Dev:
            data._id = str(data._id)
        elif type(data) is dict:
            # data['_id'] = str(data[_id])
            data.update({"_id": str(data["_id"])})

    @staticmethod
    def get_all():
        # devs_list = db.get_collection('devs').find()

        devs_list = db.devs.find()

        return devs_list
