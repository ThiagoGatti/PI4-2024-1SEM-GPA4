from flask import Blueprint, render_template

educador_blueprint = Blueprint('educador', __name__)

@educador_blueprint.route('/home')
def home():
    return render_template('home.html')

@educador_blueprint.route('/EducadorCondTrab')
def EducadorCondTrab():
    return render_template('formsProfessoresCondicaoTrab.html')

@educador_blueprint.route('/EducadorEnsino')
def EducadorEnsino():
    return render_template('formsProfessoresQualidadeEdu.html')

@educador_blueprint.route('/EducadorClima')
def EducadorClima():
    return render_template('formsProfessoresClimaEscolar.html')

@educador_blueprint.route('/EducadorInfra')
def EducadorInfra():
    return render_template('formsEducadoresInfra.html')

@educador_blueprint.route('/EducadorGestao')
def EducadorGestao():
    return render_template('formsEducadorGestao.html')

@educador_blueprint.route('/EducadorParticipacao')
def EducadorParticipacao():
    return render_template('formsProfessoresParticipacao.html')

@educador_blueprint.route('/FrequenciaVisualizar')
def FrequenciaVisualizar():
    return render_template('notasFrequenciaVisualizar.html')