from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = "6264119331:AAFN6ldEYfFmB4GgeTdbVMmoBjuzM-MLgi8"  # Забираем значение типа str
ADMINS = "5117455510"  # Тут у нас будет список из админов
#IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

support_ids = [
5117455510
]
