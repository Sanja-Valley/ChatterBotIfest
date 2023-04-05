from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Creating the Inserttable for inserting data into the database

#ToDo: Remover comentários para associar ao banco de dados Postgres quando for criado

# class Inserttable(db.Model):
#     '''Data for ON/OFF should be dumped in this table.'''

#     __tablename__ = 'produto'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column(db.String(100), primary_key=False)

#     # method used to represent a class's objects as a string
#     def __repr__(self):
#         return '<produtoid %r>' % self.produtoid