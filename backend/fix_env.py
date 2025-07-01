with open('.env', 'wb') as f:
    f.write(b'API_KEY=your-secret-key\n')
print('Successfully wrote .env file in binary mode (no BOM).') 