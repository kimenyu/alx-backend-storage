import redis

# Connect to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Function to set and get data in Redis
def set_and_get_data():
    # Set a key-value pair in Redis
    redis_client.set('my_key', 'Hello, Redis!')

    # Retrieve a value from Redis
    value = redis_client.get('my_key')

    # Decode the value from bytes to a string
    if value is not None:
        value = value.decode('utf-8')
        print('Retrieved value:', value)
    else:
        print('Key not found in Redis.')

if __name__ == "__main__":
    set_and_get_data()
