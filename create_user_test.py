import sender_stand_request
import data

# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

def test_create_user_success():
    body = get_user_body("Naru")
    resp = sender_stand_request.post_user_path(body)
    assert resp.status_code == 201
    assert resp.json()["authToken"] != ""

def test_create_user_failure_spe_chart():
    body = get_user_body("N@ru")
    resp = sender_stand_request.post_user_path(body)
    assert resp.status_code == 400

