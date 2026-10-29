@app.route('/dashboard')
def carregar_dashboard():
# Extração via API 
    res =supabase.table('pacientes')\
.select('*').execute() 
    return render_template(
'dash.html', dados=res.data
)