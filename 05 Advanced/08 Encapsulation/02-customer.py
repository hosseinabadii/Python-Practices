from dataclasses import dataclass


def send_email(to: str, subject: str, body: str) -> None:
    print(f"Sending email...")
    print(f" | to: {to}")
    print(f" | Subject: {subject}")
    print(f" | Body: {body}")


@dataclass
class Customer:
    id: str
    name: str
    email_address: str

    def __post_init__(self):
        self._send_welcome_email()

    def _send_welcome_email(self):
        subject = "Welcome to our platform!"
        body = (
            f"Hi, {self.name}, we're so glad you joined our platform."
        )
        send_email(self.email_address, subject, body)

def main():
    Customer("14785", "Reza", "Reza@14785gmail.com")

if __name__ == "__main__":
    main()