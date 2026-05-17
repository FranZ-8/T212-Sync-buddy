import os
import sys
import requests

def upload():
    csv_file = sys.argv[1]
    account_id = sys.argv[2]
    
    url = os.environ.get("GHOSTFOLIO_URL")
    secret = os.environ.get("GHOSTFOLIO_SECRET")
    
    if not url or not secret:
        print("❌ Erro: GHOSTFOLIO_URL ou GHOSTFOLIO_SECRET não configurados nas variáveis.")
        sys.exit(1)
        
    endpoint = f"{url.rstrip('/')}/api/v1/import"
    headers = {"Authorization": f"Bearer {secret}"}
    
    print(f"🚀 A enviar {csv_file} diretamente para a API do Ghostfolio...")
    
    with open(csv_file, 'rb') as f:
        files = {'file': (os.path.basename(csv_file), f, 'text/csv')}
        data = {'accountId': account_id}
        
        response = requests.post(endpoint, headers=headers, files=files, data=data)
        
    if response.status_code in [200, 201]:
        print("✅ Envio efetuado com sucesso total!")
    else:
        print(f"❌ Falha no envio da API. Status: {response.status_code}")
        print(response.text)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python upload_to_gf.py <caminho_csv> <account_id>")
        sys.exit(1)
    upload()
