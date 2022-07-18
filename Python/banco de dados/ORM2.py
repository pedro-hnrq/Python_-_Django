from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from ORM import Pessoa

def RetornaSession():
    USUARIO="root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "pythonfull"
    PORT ="3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()
session = RetornaSession()
# ##DELETE##
# x = session.query(Pessoa).filter(Pessoa.id == 5).one()
# session.delete(x)
# session.commit()


# ##UPDATE##
# x = session.query(Pessoa).filter(Pessoa.id == 4).all()
# x[0].nome += ' Feitosa'
# session.commit()

##OR##
# x = session.query(Pessoa).filter(or_(Pessoa.nome == 'Pedro', Pessoa.usuario == 'pedro'))
# for i in x:
#     print(i.senha)

##SELECT##
# x = session.query(Pessoa).all()
# x = session.query(Pessoa).filter(Pessoa.nome == 'Henrique')
# for i in x:
#     print(i.id)

# x = Pessoa(nome = 'Soares', 
#            usuario = 'pedro',
#            senha = '98746' )
# y = Pessoa(nome = 'Feitosa', 
#            usuario = 'henri',
#            senha = '98745' )
# session.add_all([x,y])
# # session.rollback()
# session.commit()