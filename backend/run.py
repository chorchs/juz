from app import create_app, db
from app.models import User, Causa, Victima, Agresor, Pericia, CamaraGesell

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Causa': Causa, 'Victima': Victima,
            'Agresor': Agresor, 'Pericia': Pericia, 'CamaraGesell': CamaraGesell}
