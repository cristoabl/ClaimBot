import os
from web3 import Web3
from web3.utils.address import to_checksum_address  # Import to_checksum_address function
from telegram import Bot
import config

# Configura tu clave API de Etherscan aquí
ETHERSCAN_API_KEY = config.eth

# Configura tu clave de acceso al bot de Telegram aquí
TELEGRAM_BOT_TOKEN = config.tk
CHAT_ID = config.id  # Puedes obtenerlo de @userinfobot en Telegram

# Dirección del contrato y función que deseas seguir
CONTRACT_ADDRESS = to_checksum_address('0x6d0e0aff61fae221b2de4ca82cc4070e830c4013')
FUNCTION_SIGNATURE = '0xb487b699'

# Crea una instancia de Web3
w3 = Web3(Web3.HTTPProvider(config.inf))

# Crea una instancia del bot de Telegram
bot = Bot(token=TELEGRAM_BOT_TOKEN)

def check_transaction():
    # Escucha eventos en el contrato
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=[{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_TOKEN","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"Claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_state","type":"bool"}],"name":"EnableClaim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"TOKEN","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"wallet","type":"address[]"},{"internalType":"uint256[]","name":"amount","type":"uint256[]"}],"name":"addData","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_newOwner","type":"address"}],"name":"changeOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"changeToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"enableClaim","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalTokenClaimed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferStuckTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wallets","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}])  # Debes reemplazar ABI_DEL_CONTRATO con el ABI correcto

    # Filtra eventos de la función addData
    event_filter = contract.events.addData.createFilter(fromBlock="latest")

    while True:
        for event in event_filter.get_new_entries():
            # Envía un mensaje a Telegram cuando se confirma una transacción
            message = f"Se ha confirmado una transacción en el contrato {CONTRACT_ADDRESS}. Detalles: {event}"
            bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    check_transaction()
