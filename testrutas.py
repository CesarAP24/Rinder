
# SIN MODELO CHAT 
@app.route('/mensajes/list', methods=['POST'])
def obtener_ultimos_mensajes():
    id_usuario = request.get['id_usuario']
    mensajes = db.session.query(Mensaje.id_usario_remitente, Mensaje.id_usario_destinatario).filter_by(id_usuario).distinct().order_by(id_mensaje.fecha.desc()).limit(10).all()


#SIN MODELO CHAT MEJORADO

@app.route('/mensajes/list2', methods=['GET'])
def obtener_ultimos_chats():
    id_usuario = request.json.get('id_usuario')

    subquery = db.session.query(
        Mensaje.id_usuarioremitente,
        Mensaje.id_usuariodestinatario,
        db.func.max(Mensaje.fecha).label('max_fecha')
    ).group_by(Mensaje.id_usuarioremitente, Mensaje.id_usuariodestinatario).subquery()

    mensajes = db.session.query(
        Mensaje.id_usuarioremitente,
        Mensaje.id_usuariodestinatario,
        Mensaje.id_mensaje
    ).join(
        subquery,
        db.and_(
            Mensaje.id_usuarioremitente == subquery.c.id_usuarioremitente,
            Mensaje.id_usuariodestinatario == subquery.c.id_usuariodestinatario,
            Mensaje.fecha == subquery.c.max_fecha
        )
    ).filter(
        db.or_(
            Mensaje.id_usuarioremitente == id_usuario,
            Mensaje.id_usuariodestinatario == id_usuario
        )
    ).order_by(Mensaje.fecha.desc()).limit(10).all()

    ultimos_chats = []
    for mensaje in mensajes:
        if mensaje.id_usuarioremitente != id_usuario:
            id_chat = mensaje.id_usuarioremitente
        else:
            id_chat = mensaje.id_usuariodestinatario
        ultimos_chats.append({'id_chat': id_chat, 'id_ultimo_mensaje': mensaje.id_mensaje})

    return jsonify(ultimos_chats)


#CON MODELO CHAT MEJORADO

@app.route('/chats/list', methods=['GET'])
def obtener_ultimos_chats():
    chats = Chat.query.order_by(Chat.fecha.desc()).all()
    ultimos_chats = []
    for chat in chats:
        ultimo_mensaje = Mensaje.query.filter_by(id_mensaje=chat.id_mensaje).first()
        if ultimo_mensaje:
            ultimos_chats.append({'id_chat': chat.id_chat, 'id_ultimo_mensaje': ultimo_mensaje.id_mensaje})

    return jsonify(ultimos_chats)