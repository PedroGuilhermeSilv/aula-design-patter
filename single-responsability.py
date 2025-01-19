
## Exemplo ruim
class UserManager:
    def create_user(self, name, email):
        # Cria um novo usuário
        pass

    def send_email(self, email, subject, body):
        # Envia um email
        pass



## Exemplo  Bom
class UserManager:
    def create_user(self, dados):
        ...

class EmailService:
    def send_email(self,email):
        ...
