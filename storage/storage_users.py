from storage import storage_set, storage_get

#cp docker-compose.yml and docker-compose up -d

storage_set('10.20.2.2:username')

print(storage_get('10.20.2.2:username'))
