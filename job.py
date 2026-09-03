# job.py
import os

def main():
    token = os.environ.get("SECRET_API_TOKEN")

    if not token:
        raise ValueError("SECRET_API_TOKEN n'est pas défini dans l'environnement")

    print(f"Token récupéré, longueur : {len(token)} caractères")
    # Ici tu utiliserais le token pour t'authentifier auprès de ton API
    # ex: requests.get(url, headers={"Authorization": f"Bearer {token}"})

if __name__ == "__main__":
    main()