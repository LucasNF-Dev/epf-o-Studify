from bottle import get, post, template, request, redirect
from services.calendario_service import CalendarioService

@get("/calendario")
def calendario_view():
    cal = CalendarioService.load()
    return template ("calendario", calendario=cal)

@get("/calendario/prova/nova")
def form_prova():
    return template("calendario_prova_form")

@post("/calendario/prova/nova")
def salvar_prova():
    data = request.froms.get("data")
    materia = request.forms.get("materia")

    cal = CalendarioService.load()
    cal.add_prova(data, materia)
    CalendarioService.save(cal)

    redirect("/calendario")


@get("/calendario/evento/novo")
def form_evento():
    return template("calendario_evento_form")

@post("/calendario/evento/novo")
def salvar_evento():
    data = request.forms.get("data")
    titulo = request.forms.get("titulo")
    descricao = request.forms.get("descricao")

    cal = CalendarioService.load()
    cal.add_evento(data, titulo, descricao)
    CalendarioService.save(cal)

    redirect ("/calendario")