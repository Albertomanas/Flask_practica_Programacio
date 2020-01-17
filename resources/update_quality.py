from flask_restful import Resource, Api
from config import tienda
from services.service import Service


class Update_quality(Resource):

    def get(self):
        return Service.get_quality_updated(tienda)
    
    def post(self):
        pass
