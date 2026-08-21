import os
import openpyxl  # Nouvelle bibliothèque pour lire le Excel directement
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
service_role_key = os.getenv('SERVICE_ROLE_KEY')

print("SUPABASE_URL présente :", bool(url))
print("SUPABASE_KEY présente :", bool(key))
print("SERVICE_ROLE_KEY présente :", bool(service_role_key))

supabase_client = create_client(url, key)
supabase_admin = create_client(url, service_role_key)




