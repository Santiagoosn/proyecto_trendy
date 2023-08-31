class Config:
        
    #definir la cadena de conexion ("conectionstring")
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/proyecto_trendy'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False 
    SECRET_KEY = 'SanSte'