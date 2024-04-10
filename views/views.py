from flask import request, request
from datetime import datetime
from flask_restful import Resource
from ..models import db, Blacklist, BlackListSchema

blacklist_schema = BlackListSchema()

token_valido = 'Bearer 456889'

class BlackListView(Resource):

   def post(self):
      email = request.json["email"]
      app_uuid = request.json["app_uuid"]
      blocked_reason = request.json["blocked_reason"]
      ip = request.environ['REMOTE_ADDR']
      createdAt=datetime.now()
      token = request.headers.get("Authorization", "")      
      if token == token_valido:
         blacklist = Blacklist( email = email, app_uuid = app_uuid, blocked_reason = blocked_reason, ip = ip, createdAt = createdAt )
         db.session.add(blacklist)
         db.session.commit()
         return {'mensaje':'Email ' + email + " almacenado para App con UUID " + app_uuid + " por la razon " + blocked_reason + " enviado desde la IP " + ip + " el dia " + str(createdAt)}, 200
      else:
         return {'mensaje': 'Token no autorizado'}, 401

          
   
   
   def get(self):
      email = request.args.get('email')
      blacklist_entry = Blacklist.query.filter_by(email=email).first()
      
      if blacklist_entry:
         # Email encontrado en la lista negra
         return {'en_lista_negra': True, 'razon': blacklist_entry.blocked_reason}, 200
      else:
         # Email no está en la lista negra
         return {'en_lista_negra': False, 'razon': 'N/A'}, 200
      
