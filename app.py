import streamlit as st
import random
import time

if 'juego' not in st.session_state:
    st.session_state.juego = {
        'fase': 'config',
        'jugadores': [],
        'impostores': [],
        'palabra': "",
        'pista': "",
        'vistos': set() # Aquí guardamos quién ya miró su rol
    }
# --- BASE DE DATOS DE EJEMPLO (ESTRUCTURA PARA 150 PALABRAS) ---
DATABASE = [
    # --- DEPORTES (30) ---
    {"palabra": "Fútbol", "pista": "Césped", "cat": "Deportes"},
    {"palabra": "Baloncesto", "pista": "Aro", "cat": "Deportes"},
    {"palabra": "Tenis", "pista": "Raqueta", "cat": "Deportes"},
    {"palabra": "Natación", "pista": "Cloro", "cat": "Deportes"},
    {"palabra": "Voleibol", "pista": "Red", "cat": "Deportes"},
    {"palabra": "Golf", "pista": "Hoyo", "cat": "Deportes"},
    {"palabra": "Boxeo", "pista": "Guantes", "cat": "Deportes"},
    {"palabra": "Ciclismo", "pista": "Ruta", "cat": "Deportes"},
    {"palabra": "Rugby", "pista": "Ovalada", "cat": "Deportes"},
    {"palabra": "Béisbol", "pista": "Bate", "cat": "Deportes"},
    {"palabra": "Esgrima", "pista": "Espada", "cat": "Deportes"},
    {"palabra": "Surf", "pista": "Ola", "cat": "Deportes"},
    {"palabra": "Ajedrez", "pista": "Tablero", "cat": "Deportes"},
    {"palabra": "Patinaje", "pista": "Hielo", "cat": "Deportes"},
    {"palabra": "Kárate", "pista": "Cinturón", "cat": "Deportes"},
    {"palabra": "Yoga", "pista": "Flexibilidad", "cat": "Deportes"},
    {"palabra": "Fórmula 1", "pista": "Motor", "cat": "Deportes"},
    {"palabra": "Atletismo", "pista": "Pista", "cat": "Deportes"},
    {"palabra": "Gimnasia", "pista": "Salto", "cat": "Deportes"},
    {"palabra": "Remo", "pista": "Agua", "cat": "Deportes"},
    {"palabra": "Ping Pong", "pista": "Mesa", "cat": "Deportes"},
    {"palabra": "Escalada", "pista": "Montaña", "cat": "Deportes"},
    {"palabra": "Búlder", "pista": "Roca", "cat": "Deportes"},
    {"palabra": "Esquí", "pista": "Nieve", "cat": "Deportes"},
    {"palabra": "Pádel", "pista": "Muro", "cat": "Deportes"},
    {"palabra": "Hockey", "pista": "Stick", "cat": "Deportes"},
    {"palabra": "Sumo", "pista": "Peso", "cat": "Deportes"},
    {"palabra": "Dardos", "pista": "Puntería", "cat": "Deportes"},
    {"palabra": "Bolos", "pista": "Pinos", "cat": "Deportes"},
    {"palabra": "Billar", "pista": "Taco", "cat": "Deportes"},

    # --- MARCAS (30) ---
    {"palabra": "BMW", "pista": "Aros", "cat": "Marcas"},
    {"palabra": "Apple", "pista": "Mordida", "cat": "Marcas"},
    {"palabra": "Coca Cola", "pista": "Gas", "cat": "Marcas"},
    {"palabra": "Nike", "pista": "Gancho", "cat": "Marcas"},
    {"palabra": "Adidas", "pista": "Rayas", "cat": "Marcas"},
    {"palabra": "McDonalds", "pista": "Arcos", "cat": "Marcas"},
    {"palabra": "Netflix", "pista": "Pantalla", "cat": "Marcas"},
    {"palabra": "Amazon", "pista": "Paquete", "cat": "Marcas"},
    {"palabra": "Google", "pista": "Buscador", "cat": "Marcas"},
    {"palabra": "Ferrari", "pista": "Caballo", "cat": "Marcas"},
    {"palabra": "Rolex", "pista": "Lujo", "cat": "Marcas"},
    {"palabra": "Disney", "pista": "Castillo", "cat": "Marcas"},
    {"palabra": "Starbucks", "pista": "Sirena", "cat": "Marcas"},
    {"palabra": "Toyota", "pista": "Japón", "cat": "Marcas"},
    {"palabra": "Samsung", "pista": "Corea", "cat": "Marcas"},
    {"palabra": "Lego", "pista": "Bloque", "cat": "Marcas"},
    {"palabra": "IKEA", "pista": "Mueble", "cat": "Marcas"},
    {"palabra": "Tesla", "pista": "Eléctrico", "cat": "Marcas"},
    {"palabra": "Zara", "pista": "Moda", "cat": "Marcas"},
    {"palabra": "Red Bull", "pista": "Alas", "cat": "Marcas"},
    {"palabra": "Pepsi", "pista": "Azul", "cat": "Marcas"},
    {"palabra": "Spotify", "pista": "Música", "cat": "Marcas"},
    {"palabra": "Facebook", "pista": "Red", "cat": "Marcas"},
    {"palabra": "Instagram", "pista": "Foto", "cat": "Marcas"},
    {"palabra": "WhatsApp", "pista": "Mensaje", "cat": "Marcas"},
    {"palabra": "YouTube", "pista": "Video", "cat": "Marcas"},
    {"palabra": "Mercedes", "pista": "Estrella", "cat": "Marcas"},
    {"palabra": "Audi", "pista": "Círculos", "cat": "Marcas"},
    {"palabra": "Puma", "pista": "Felino", "cat": "Marcas"},
    {"palabra": "Nintendo", "pista": "Consola", "cat": "Marcas"},

    # --- PERSONAJES DE FICCIÓN (30) ---
    {"palabra": "Tony Stark", "pista": "Millonario", "cat": "Ficción"},
    {"palabra": "Batman", "pista": "Murciélago", "cat": "Ficción"},
    {"palabra": "Spiderman", "pista": "Telaraña", "cat": "Ficción"},
    {"palabra": "Shrek", "pista": "Ogro", "cat": "Ficción"},
    {"palabra": "Hulk", "pista": "Verde", "cat": "Ficción"},
    {"palabra": "Harry Potter", "pista": "Cicatriz", "cat": "Ficción"},
    {"palabra": "Darth Vader", "pista": "Casco", "cat": "Ficción"},
    {"palabra": "Mickey Mouse", "pista": "Orejas", "cat": "Ficción"},
    {"palabra": "Sherlock Holmes", "pista": "Lupa", "cat": "Ficción"},
    {"palabra": "Joker", "pista": "Risa", "cat": "Ficción"},
    {"palabra": "Superman", "pista": "Capa", "cat": "Ficción"},
    {"palabra": "Wonder Woman", "pista": "Lazo", "cat": "Ficción"},
    {"palabra": "Mario", "pista": "Gorra", "cat": "Ficción"},
    {"palabra": "Pikachu", "pista": "Rayo", "cat": "Ficción"},
    {"palabra": "Elsa", "pista": "Hielo", "cat": "Ficción"},
    {"palabra": "Goku", "pista": "Pelo", "cat": "Ficción"},
    {"palabra": "SpongeBob", "pista": "Piña", "cat": "Ficción"},
    {"palabra": "Simba", "pista": "Rey", "cat": "Ficción"},
    {"palabra": "Woody", "pista": "Vaquero", "cat": "Ficción"},
    {"palabra": "James Bond", "pista": "Agente", "cat": "Ficción"},
    {"palabra": "Gandalf", "pista": "Mago", "cat": "Ficción"},
    {"palabra": "Frodo", "pista": "Anillo", "cat": "Ficción"},
    {"palabra": "Katniss Everdeen", "pista": "Arco", "cat": "Ficción"},
    {"palabra": "Indiana Jones", "pista": "Látigo", "cat": "Ficción"},
    {"palabra": "Lara Croft", "pista": "Tumbas", "cat": "Ficción"},
    {"palabra": "Cenicienta", "pista": "Zapatilla", "cat": "Ficción"},
    {"palabra": "Robin Hood", "pista": "Flecha", "cat": "Ficción"},
    {"palabra": "Pinocho", "pista": "Nariz", "cat": "Ficción"},
    {"palabra": "Tarzán", "pista": "Selva", "cat": "Ficción"},
    {"palabra": "Deadpool", "pista": "Máscara", "cat": "Ficción"},

    # --- FAMOSOS (30) ---
    {"palabra": "Messi", "pista": "Pulga", "cat": "Famosos"},
    {"palabra": "Cristiano Ronaldo", "pista": "Bicho", "cat": "Famosos"},
    {"palabra": "Elon Musk", "pista": "Cohete", "cat": "Famosos"},
    {"palabra": "Bill Gates", "pista": "Software", "cat": "Famosos"},
    {"palabra": "Michael Jackson", "pista": "Guante", "cat": "Famosos"},
    {"palabra": "Beyoncé", "pista": "Diva", "cat": "Famosos"},
    {"palabra": "Shakira", "pista": "Caderas", "cat": "Famosos"},
    {"palabra": "Albert Einstein", "pista": "Genio", "cat": "Famosos"},
    {"palabra": "Leonardo Da Vinci", "pista": "Pintor", "cat": "Famosos"},
    {"palabra": "Marilyn Monroe", "pista": "Rubia", "cat": "Famosos"},
    {"palabra": "Usain Bolt", "pista": "Veloz", "cat": "Famosos"},
    {"palabra": "Rafael Nadal", "pista": "Tierra", "cat": "Famosos"},
    {"palabra": "Stephen Hawking", "pista": "Silla", "cat": "Famosos"},
    {"palabra": "Taylor Swift", "pista": "Guitarra", "cat": "Famosos"},
    {"palabra": "Jeff Bezos", "pista": "Calvo", "cat": "Famosos"},
    {"palabra": "Dwayne Johnson", "pista": "Roca", "cat": "Famosos"},
    {"palabra": "Lady Gaga", "pista": "Monstruo", "cat": "Famosos"},
    {"palabra": "Will Smith", "pista": "Príncipe", "cat": "Famosos"},
    {"palabra": "Oprah Winfrey", "pista": "Sillón", "cat": "Famosos"},
    {"palabra": "Gordon Ramsay", "pista": "Cocina", "cat": "Famosos"},
    {"palabra": "Jackie Chan", "pista": "Artes", "cat": "Famosos"},
    {"palabra": "Madonna", "pista": "Pop", "cat": "Famosos"},
    {"palabra": "Eminem", "pista": "Rap", "cat": "Famosos"},
    {"palabra": "Dalí", "pista": "Bigote", "cat": "Famosos"},
    {"palabra": "Picasso", "pista": "Cubismo", "cat": "Famosos"},
    {"palabra": "Maluma", "pista": "Reggaetón", "cat": "Famosos"},
    {"palabra": "Zendaya", "pista": "Actriz", "cat": "Famosos"},
    {"palabra": "LeBron James", "pista": "Canasta", "cat": "Famosos"},
    {"palabra": "Tiger Woods", "pista": "Verde", "cat": "Famosos"},
    {"palabra": "Rihanna", "pista": "Paraguas", "cat": "Famosos"},

    # --- FIGURAS Y OBJETOS (30) ---
    {"palabra": "Triángulo", "pista": "Tres", "cat": "Figuras"},
    {"palabra": "Círculo", "pista": "Redondo", "cat": "Figuras"},
    {"palabra": "Cubo", "pista": "Dado", "cat": "Figuras"},
    {"palabra": "Pirámide", "pista": "Egipto", "cat": "Figuras"},
    {"palabra": "Esfera", "pista": "Balón", "cat": "Figuras"},
    {"palabra": "Cilindro", "pista": "Tubo", "cat": "Figuras"},
    {"palabra": "Estrella", "pista": "Cielo", "cat": "Figuras"},
    {"palabra": "Corazón", "pista": "Amor", "cat": "Figuras"},
    {"palabra": "Diamante", "pista": "Brillo", "cat": "Figuras"},
    {"palabra": "Rectángulo", "pista": "Puerta", "cat": "Figuras"},
    {"palabra": "Pentágono", "pista": "Cinco", "cat": "Figuras"},
    {"palabra": "Hexágono", "pista": "Panal", "cat": "Figuras"},
    {"palabra": "Óvalo", "pista": "Huevo", "cat": "Figuras"},
    {"palabra": "Rombo", "pista": "Cometa", "cat": "Figuras"},
    {"palabra": "Cruz", "pista": "Iglesia", "cat": "Figuras"},
    {"palabra": "Reloj", "pista": "Tiempo", "cat": "Objetos"},
    {"palabra": "Cámara", "pista": "Lente", "cat": "Objetos"},
    {"palabra": "Guitarra", "pista": "Cuerdas", "cat": "Objetos"},
    {"palabra": "Paraguas", "pista": "Lluvia", "cat": "Objetos"},
    {"palabra": "Gafas", "pista": "Ojos", "cat": "Objetos"},
    {"palabra": "Brújula", "pista": "Norte", "cat": "Objetos"},
    {"palabra": "Ancla", "pista": "Barco", "cat": "Objetos"},
    {"palabra": "Martillo", "pista": "Clavo", "cat": "Objetos"},
    {"palabra": "Espejo", "pista": "Reflejo", "cat": "Objetos"},
    {"palabra": "Lámpara", "pista": "Luz", "cat": "Objetos"},
    {"palabra": "Llave", "pista": "Candado", "cat": "Objetos"},
    {"palabra": "Tijeras", "pista": "Filo", "cat": "Objetos"},
    {"palabra": "Maleta", "pista": "Viaje", "cat": "Objetos"},
    {"palabra": "Libro", "pista": "Páginas", "cat": "Objetos"},
    {"palabra": "Escalera", "pista": "Peldaño", "cat": "Objetos"}
]

st.title("🕵️ Juego del Impostor")

# --- FASE 1: CONFIGURACIÓN ---
if st.session_state.juego['fase'] == 'config':
    nombres = st.text_area("Nombres de participantes (separados por coma):")
    num_imp = st.slider("Cantidad de impostores", 1, 3, 1)
    
    if st.button("Generar Partida"):
        lista = [n.strip() for n in nombres.split(",") if n.strip()]
        if len(lista) < 3:
            st.error("Mínimo 3 personas")
        else:
            item = random.choice(DATABASE)
            st.session_state.juego.update({
                'fase': 'revelar',
                'jugadores': lista,
                'impostores': random.sample(lista, num_imp),
                'palabra': item['palabra'],
                'pista': item['pista'],
                'vistos': set()
            })
            st.rerun()

# --- FASE 2: REVELAR ROL (CON BLOQUEO) ---
elif st.session_state.juego['fase'] == 'revelar':
    st.header("🔑 Revelar Identidad")
    st.write("Cada uno debe poner su nombre para ver su palabra. ¡Solo puedes hacerlo una vez!")
    
    nombre_input = st.text_input("Escribe tu nombre exactamente como se anotó:").strip()
    
    if st.button("Ver mi rol"):
        if nombre_input not in st.session_state.juego['jugadores']:
            st.warning("Ese nombre no está en la lista de participantes.")
        elif nombre_input in st.session_state.juego['vistos']:
            st.error(f"⚠️ ¡Trampa detectada! {nombre_input}, ya viste tu rol y no puedes volver a verlo.")
        else:
            # Mostrar info y marcar como visto
            if nombre_input in st.session_state.juego['impostores']:
                st.error(f"ERES EL IMPOSTOR 😈. Pista: {st.session_state.juego['pista']}")
            else:
                st.success(f"ERES CIVIL 😊. Palabra: {st.session_state.juego['palabra']}")
            
            st.session_state.juego['vistos'].add(nombre_input)
            st.info("Memoriza tu palabra y cierra esta pestaña o dale el móvil al siguiente.")

    # Mostrar cuánta gente falta por ver
    faltan = len(st.session_state.juego['jugadores']) - len(st.session_state.juego['vistos'])
    st.write(f"Faltan **{faltan}** jugadores por ver su rol.")
    
    if faltan == 0:
        if st.button("Todos listos - Ir a Votación 🗳️"):
            st.session_state.start_time = time.time()
            st.session_state.juego['fase'] = 'votacion'
            st.rerun()

# --- FASE 3: VOTACIÓN ---
elif st.session_state.juego['fase'] == 'votacion':
    st.header("🗳️ Fase de Votación")
    # Lógica del reloj de 5 min (como ya la teníamos)
    limite = 5 * 60
    ahora = time.time()
    restante = int(limite - (ahora - st.session_state.start_time))
    
    if restante > 0:
        m, s = divmod(restante, 60)
        st.metric("Tiempo de debate", f"{m:02d}:{s:02d}")
        if st.button("Actualizar tiempo"): st.rerun()
    else:
        st.error("¡TIEMPO AGOTADO!")

    if st.button("Revelar quiénes eran"):
        st.write(f"Impostores: {st.session_state.juego['impostores']}")
        if st.button("Nueva partida"):
            st.session_state.juego['fase'] = 'config'
            st.rerun()