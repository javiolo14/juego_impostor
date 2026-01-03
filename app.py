import streamlit as st
import random

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

# --- ESTADO GLOBAL DEL JUEGO ---
if 'juego' not in st.session_state:
    st.session_state.juego = {
        'fase': 'config',
        'jugadores': [],
        'impostores': [],
        'palabra': "",
        'pista': "",
        'turno_inicial': ""
    }

# --- FUNCIONES ---
def iniciar_partida(nombres_str, n_impostores):
    lista = [n.strip() for n in nombres_str.split(",") if n.strip()]
    if len(lista) < 3:
        st.error("Mínimo 3 jugadores")
        return
    
    seleccion = random.choice(DATABASE)
    imps = random.sample(lista, n_impostores)
    
    st.session_state.juego.update({
        'fase': 'jugando',
        'jugadores': lista,
        'impostores': imps,
        'palabra': seleccion['palabra'],
        'pista': seleccion['pista'],
        'turno_inicial': random.choice(lista)
    })

# --- INTERFAZ ---
st.set_page_config(page_title="Impostor Game", page_icon="🕵️")

if st.session_state.juego['fase'] == 'config':
    st.header("⚙️ Configuración")
    nombres = st.text_area("Nombres (separados por coma):", "Alex, Juan, Sofia, Maria")
    num_imp = st.number_input("Número de Impostores", 1, 5, 1)
    
    if st.button("Generar Roles"):
        iniciar_partida(nombres, num_imp)
        st.rerun()

elif st.session_state.juego['fase'] == 'jugando':
    st.header("🎮 Partida en curso")
    st.info(f"Empieza hablando: **{st.session_state.juego['turno_inicial']}**")
    
    # Revelar información
    nombre_sel = st.selectbox("Busca tu nombre:", ["---"] + st.session_state.juego['jugadores'])
    
    if nombre_sel != "---":
        with st.expander("Pulsa para ver tu palabra/pista"):
            if nombre_sel in st.session_state.juego['impostores']:
                st.error(f"ERES EL IMPOSTOR 😈")
                st.write(f"Pista del tema: **{st.session_state.juego['pista']}**")
            else:
                st.success(f"ERES CIVIL 😊")
                st.write(f"Palabra secreta: **{st.session_state.juego['palabra']}**")
    
    st.divider()
    if st.button("Fase de Votación 🗳️"):
        st.session_state.juego['fase'] = 'votacion'
        st.rerun()

elif st.session_state.juego['fase'] == 'votacion':
    st.header("🗳️ Votación")
    
    # Temporizador visual (Streamlit no tiene uno nativo dinámico fácil, usamos un placeholder)
    st.warning("Tienen 5 minutos para debatir.")
    
    if st.button("Revelar Identidades"):
        st.write("### Los Impostores eran:")
        for imp in st.session_state.juego['impostores']:
            st.write(f"- **{imp}**")
        st.write(f"La palabra era: **{st.session_state.juego['palabra']}**")
        
        if st.button("Jugar otra vez"):
            st.session_state.juego['fase'] = 'config'
            st.rerun()