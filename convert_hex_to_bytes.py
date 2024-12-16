# # An example data structure that cannot be converted to JSON, YAML, or XML format.
# from collections import OrderedDict
# data = OrderedDict({
#     'Timestamp': '2023-04-05 16:00:00',
#     'IoTData': {
#         'IP': '172.23.155.209',
#         'Port': 3001,
#         'value': [1.2, 1.3, 1.4],
#         'RptPeer': {
#             'Hub1': 1.2,
#             'Hub2': 1.3
#         },
#         'CfgSet': set(['CT100', 'COM3', 3])  # set data is not support by json
#     }
# })


import pickle
# # Serialize the data to bytes
# serialized_data = pickle.dumps(data)
# print(serialized_data)
# # Deserialize the bytes back to the original data
# deserialized_data = pickle.loads(serialized_data)
# print(deserialized_data)



# Hexadecimal string from Wireshark
hex_data = "8f80049584000000000000007d94288c07544553545f4d44944e8c0a52414441525f54595045944e8c0a52414441525f504f5254944e8c1552414441525f5550444154455f494e54455256414c944e8c065250545f4d44944e8c075250545f494e54944e8c0a5250545f5345525f4950944e8c0c5250545f5345525f504f5254944e8c085745425f504f5254944e752e"

# Convert hex string to bytes
binary_data = bytes.fromhex(hex_data)

# Load with pickle
try:
    obj = pickle.loads(binary_data)
    print("Loaded object:", obj)
except Exception as e:
    print("Error:", e)
    
    
    


# Hexadecimal string from Wireshark
# hex_data = "b5800595aa000000000000007d94288c07544553545f4d4494888c0a52414441525f54595045948c054354313030948c0a52414441525f504f5254948c04434f4d33948c1552414441525f5550444154455f494e54455256414c948c0131948c065250545f4d4494898c075250545f494e54948c0135948c0a5250545f5345525f4950948c093132372e302e302e31948c0c5250545f5345525f504f5254944d89138c085745425f504f5254948c043530303094752e"

# # Convert hex string to bytes
# binary_data = bytes.fromhex(hex_data)

# # Load with pickle
# try:
#     obj = pickle.loads(binary_data)
#     print("Loaded object:", obj)
# except Exception as e:
#     print("Error:", e)

