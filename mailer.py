import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

# Función para generar el contenido HTML
def generar_html(nombre, correo):
    html_body = f"""
    <html>
        <body style="font-family: Arial, sans-serif; background-color: #f2f2f7; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 10px rgba(0,0,0,0.1);">
                <header style="text-align: right;">
                    <img src="https://20candy.github.io/SenasChapinasWeb/assets/img/logo_largo.png" alt="Señas Chapinas Logo" style="height: 40px;">
                </header>
                <section>
                    <p style="font-size: 16px; color: #29235C;">Hola {nombre},</p>
                    <p style="font-size: 16px; color: #29235C;">
                        Estas realizando un cambio de contraseña para tu correo <a href="mailto:{correo}" style="color: #1E88E5;">{correo}</a>.
                    </p>
                    <div style="text-align: center; margin: 40px 0 40px 0;">
                        <a href="https://20candy.github.io/SenasChapinasWeb/change_password?email={correo}" style="background-color: #00973A; color: white; padding: 15px 25px; text-decoration: none; border-radius: 100px; font-size: 16px;">
                            Cambiar Contraseña
                        </a>
                    </div>
                    <p style="font-size: 12px; color: #29235C;">
                        Si tienes problemas para utilizar el botón de arriba, también puedes cambiar tu contraseña copiando la dirección de abajo en tu navegador de preferencia en tu dispositivo móvil:
                    </p>
                    <p style="font-size: 12px; color: #1E88E5;">
                        https://20candy.github.io/SenasChapinasWeb/change_password?email={correo}
                    </p>
                    <p style="font-size: 16px; color: #29235C; margin-top: 30px;">
                            Saludos,
                    </p>
                    <p style="font-size: 16px; color: #29235C; margin-top: 5px;">
                            Equipo Señas Chapinas
                    </p>
                    <footer style="margin-top: 40px; font-size: 12px; color: #60618C;">
                        <p>Si no solicitaste un cambio de contraseña, ignora este correo.</p>
                    </footer>
                </section>
            </div>
        </body>
    </html>
    """
    return html_body

# Configuración del servidor SMTP de Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Puerto SMTP de Gmail para conexión TLS
sender_email = "senas.chapinas@gmail.com"  # Tu correo de Gmail
password = "qmcn gmjl zjsu utva"  # Tu contraseña de aplicación generada en Gmail

# Obtener el correo del destinatario desde la terminal
if len(sys.argv) < 2:
    print("Por favor, proporciona un correo de destinatario.")
    sys.exit(1)

recipient_email = sys.argv[1]

# Obtener el nombre usando la parte antes de la arroba
nombre = recipient_email.split("@")[0]

# Generar el contenido HTML usando el nombre y el correo
html_content = generar_html(nombre, recipient_email)

# Configuración del mensaje
subject = "Cambia tu Contraseña"

# Crear el mensaje
message = MIMEMultipart("alternative")  # Usamos "alternative" para soportar texto y HTML
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject

# Crear el contenido HTML
html_part = MIMEText(html_content, "html")

# Adjuntar el contenido HTML al mensaje
message.attach(html_part)

# Enviar el correo usando el servidor SMTP de Gmail
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Iniciar la conexión TLS segura
    server.login(sender_email, password)  # Iniciar sesión en Gmail con la contraseña de aplicación
    server.sendmail(sender_email, recipient_email, message.as_string())  # Enviar el correo
    server.quit()  # Cerrar la conexión con el servidor SMTP
    print(f"Correo enviado con éxito a {recipient_email}.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
