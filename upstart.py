# Define app instance 

from app import app, db
from app.models import Organization, Category

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': Organization, 'Category': Category}