from flask_restplus import fields
from server.instance import server


item = server.api.model('Item',
        {
       'name': fields.String(required=True, min_length=1, max_length=200, description='Item name'),
       'price': fields.Float(description='Price')
        }
)