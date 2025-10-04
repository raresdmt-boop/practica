# CRUD, mai am update si delete si listare detaliata (adica fix cartea pe care o vreau in fucntie de parametri)

# adaugam si tabelul de autori, legam tabela de autori cu tabela de carti
# creeaza o metoda care sa ne aduca toate cartile unui autor

# creeaza cont de github

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///practica_sqlAlchemy2.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Autor(Base):
    __tablename__ = 'autori'

    id = Column(Integer, primary_key=True)
    nume = Column(String, nullable = False)

    carti = relationship('Carte', back_populates='autor')

    def __str__(self):
        return f'Autor: {self.nume}'

autori_data = [
    
            {"nume": "Guido van Rossum"},
            {"nume": "Alan Beaulieu"},
            {"nume": "Miguel Grinberg"},
            {"nume": "Robert Martin"},
            {"nume": "Andy Hunt"}
            
]


class Carte(Base):
    __tablename__ = 'carti'

    id = Column(Integer, primary_key=True)
    titlu = Column(String(50), nullable=False, unique=True)
    pagini = Column(Integer, default=0)
    anul_publicarii = Column(Integer, nullable=False)

    autor_id = Column(Integer, ForeignKey('autori.id'))

    autor = relationship('Autor', back_populates='carti')

    def __repr__(self):
        return f'Cartea {self.titlu}, scrisa de {self.autor}, in anul {self.anul_publicarii} are {self.pagini} (de) pagini.' 

Base.metadata.create_all(engine)

carti_data = [
            {"titlu": "The Python Tutorial", "autor": "Guido van Rossum", "pagini": 150, "anul_publicarii": 2020},
            {"titlu": "Learning SQL", "autor": "Alan Beaulieu", "pagini": 338, "anul_publicarii": 2009},
            {"titlu": "Flask Web Development", "autor": "Miguel Grinberg", "pagini": 316, "anul_publicarii": 2018},
            {"titlu": "Clean Code", "autor": "Robert Martin", "pagini": 464, "anul_publicarii": 2008},
            {"titlu": "The Pragmatic Programmer", "autor": "Andy Hunt", "pagini": 352, "anul_publicarii": 1999}
            ]





def insert_autori():
    for autor in autori_data:
        autor_exista = session.query(Autor).filter_by(nume=autor.get('nume')).first()
        if not autor_exista:
            temp_autor = Autor(**autor)
            session.add(temp_autor)
            session.commit()

insert_autori()




# def insert_carti():
#     for carte in carti_data:
#         carte_exista = session.query(Carte).filter_by(titlu=carte.get('titlu')).first()
#         if not carte_exista:
#             temp_carte = Carte(**carte)
#             session.add(temp_carte)
#             session.commit()

# insert_carti()

# def cauta_carti_nr_pagini(nr_pag):
#     carti_care_exista = session.query(Carte).filter(Carte.pagini >= nr_pag).all()
#     lista_carti = [carte.titlu for carte in carti_care_exista]
#     return lista_carti
    

# # print(cauta_carti_nr_pagini(400))

# def da_update_la_carte(titlul_cartii, nr_pag):
#     cartea_updatata = session.query(Carte).filter_by(titlu=titlul_cartii).first()
#     cartea_updatata.pagini = nr_pag
#     session.commit()
#     return f'Cartea a fost updatata cu nr de pagini {nr_pag}'

# # print(da_update_la_carte('The Pragmatic Programmer', 352))

# def sterge_cartea(titlul_cartii):
#     cartea_de_sters = session.query(Carte).filter_by(titlu=titlul_cartii).first()
#     session.delete(cartea_de_sters)
#     session.commit()
#     return f'Cartea {titlul_cartii} a fost stearsa din database.'

# def cauta_cartea(**kwargs):
#     cartea = session.query(Carte).filter_by(**kwargs).first()
#     return cartea

# # print(cauta_cartea(titlu = 'Flask Web Development'))

