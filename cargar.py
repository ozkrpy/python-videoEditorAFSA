from main import db
from models import db as dbmodel, Jugador,Videos
from datetime import datetime

dbmodel.create_all()

# j = Jugador(nombre='ANON', numero_camiseta='23', date=datetime.utcnow())
# dbmodel.session.add(j)
# j = Jugador(nombre='ANON', numero_camiseta='24', date=datetime.utcnow())
# dbmodel.session.add(j)
# j = Jugador(nombre='ANON', numero_camiseta='25', date=datetime.utcnow())
# dbmodel.session.add(j)
j = Jugador(nombre='ANON1', numero_camiseta='26', date=datetime.utcnow())
dbmodel.session.add(j)
dbmodel.session.commit()

j = Jugador(nombre='ANON2', numero_camiseta='27', date=datetime.utcnow())
dbmodel.session.add(j)
dbmodel.session.commit()


v = Videos(origen='a', inicio=1, duracion=4, date=datetime.utcnow())
dbmodel.session.add(v)
dbmodel.session.commit()

print(v.query.all())
print(Jugador.query.all())
