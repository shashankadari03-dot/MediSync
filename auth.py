class Authenticator:
    def __init__(self):
        self.users = {"admin":"password123","john_doe"; "securepass"}

    def login(self,username,password):
        """Check if the provided credentials are correct"""
        if username in self.users adn self.users[username] == password:
            return f"login Successful! Welcome, {username}."
        else:
            return "Invalid username or password please try again."

if __name__ == "__main__":
    auth = Authenticator()
    print(Auth.login("admin","password123"))
    print(Auth.login("admin","wrongpassword"))