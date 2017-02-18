from blockcypher import delete_wallet

is_deleted = delete_wallet(wallet_name='chi', api_key='0b955a57f12548209b090dfc5a4c4a72', is_hd_wallet=True)
print(is_deleted)

is_deleted = delete_wallet(wallet_name='donaldchi', api_key='0b955a57f12548209b090dfc5a4c4a72', is_hd_wallet=True)
print(is_deleted)

