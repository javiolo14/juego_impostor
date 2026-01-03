import streamlit as st
import random
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Impostor Sincronizado", page_icon="🕵️")
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
@st.cache_resource
def estado_servidor():
    return {
        'activo': False,
        'fase': 'espera',
        'jugadores': [],
        'impostores': [],
        'palabra': "",
        'pista': "",
        'vistos': [],
        'start_time': None
    }

server = estado_servidor()

# --- PANEL LATERAL (HOST) ---
with st.sidebar:
    st.header("👑 Panel de Control")
    soy_host = st.checkbox("Activar modo Host")
    if soy_host:
        if st.button("🔴 REINICIAR JUEGO (Para todos)"):
            server.update({'activo': False, 'fase': 'espera', 'vistos': [], 'jugadores': []})
            st.rerun()

st.title("🕵️ ¿Quién es el Impostor?")

# --- FLUJO DEL JUEGO ---

# 1. PANTALLA DE ESPERA O CONFIGURACIÓN
if not server['activo']:
    if soy_host:
        st.subheader("Configura la partida para tus amigos")
        nombres_input = st.text_area("Nombres de participantes (separados por coma):", "Juan, Maria, Pedro")
        num_imp = st.slider("Número de impostores", 1, 3, 1)
        
        if st.button("🚀 LANZAR PARTIDA"):
            lista_nombres = [n.strip() for n in nombres_input.split(",") if n.strip()]
            if len(lista_nombres) < 3:
                st.error("Se necesitan al menos 3 jugadores.")
            else:
                seleccion = random.choice(DATABASE)
                server.update({
                    'activo': True,
                    'fase': 'revelar',
                    'jugadores': lista_nombres,
                    'impostores': random.sample(lista_nombres, num_imp),
                    'palabra': seleccion['palabra'],
                    'pista': seleccion['pista'],
                    'vistos': []
                })
                st.rerun()
    else:
        st.info("⌛ Esperando a que el Host inicie la partida...")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ3bmZ3bmZ3bmZ3JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZNoAZW9mJmN0PWc/uIJBFZoOaifHf52MER/giphy.gif")
        time.sleep(3) # Auto-actualiza para ver si el host ya inició
        st.rerun()

# 2. PANTALLA DE REVELAR ROL (PARA TODOS)
elif server['fase'] == 'revelar':
    st.header("🔑 Revela tu identidad")
    st.write("Escribe tu nombre para ver tu palabra. ¡No se puede repetir!")
    
    nombre_usuario = st.text_input("Tu nombre exacto:").strip()
    
    if st.button("Ver mi rol"):
        if nombre_usuario not in server['jugadores']:
            st.warning("No estás en la lista de esta partida.")
        elif nombre_usuario in server['vistos']:
            st.error(f"⚠️ {nombre_usuario}, ¡Ya viste tu rol! No puedes volver a entrar.")
        else:
            if nombre_usuario in server['impostores']:
                st.error(f"ERES EL IMPOSTOR 😈. Pista: {server['pista']}")
            else:
                st.success(f"ERES CIVIL 😊. Palabra: {server['palabra']}")
            
            server['vistos'].append(nombre_usuario)
            st.info("Memoriza tu información. Faltan otros por ver.")

    st.write(f"Jugadores listos: **{len(server['vistos'])} / {len(server['jugadores'])}**")
    
    # Solo el Host puede pasar a la siguiente fase
    if soy_host and len(server['vistos']) >= len(server['jugadores']):
        if st.button("Pasar a Votación 🗳️"):
            server['fase'] = 'votacion'
            server['start_time'] = time.time()
            st.rerun()
    elif len(server['vistos']) < len(server['jugadores']):
        st.caption("Esperando a que todos vean su rol...")
        time.sleep(2)
        st.rerun()

# 3. PANTALLA DE VOTACIÓN
elif server['fase'] == 'votacion':
    st.header("🗳️ Tiempo de Votación")
    
    # Temporizador Sincronizado
    limite = 5 * 60
    restante = int(limite - (time.time() - server['start_time']))
    
    if restante > 0:
        mins, secs = divmod(restante, 60)
        st.metric("Reloj de debate", f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        st.rerun()
    else:
        st.error("🚨 ¡TIEMPO AGOTADO! ¡VOTEN AHORA!")

    if soy_host:
        if st.button("Revelar Impostores al grupo"):
            st.subheader(f"Los impostores eran: {', '.join(server['impostores'])}")
            st.write(f"La palabra secreta era: **{server['palabra']}**")