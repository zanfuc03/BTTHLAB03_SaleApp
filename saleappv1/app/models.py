from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)
class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
if __name__ =='__main__':
    with app.app_context():
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        p1 = Product(name='Iphone 13', category_id=1, price=20000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        p2 = Product(name='Xiaomi', category_id=1, price=1000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        p3 = Product(name='IPad Pro Max', category_id=2, price=32000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        p4 = Product(name='Laptop J9', category_id=2, price=235000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        p5 = Product(name='NguyenA', category_id=1, price=25000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
        db.session.add_all([p1, p2, p3, p3, p4, p5])
        db.session.commit()


        # db.create_all()