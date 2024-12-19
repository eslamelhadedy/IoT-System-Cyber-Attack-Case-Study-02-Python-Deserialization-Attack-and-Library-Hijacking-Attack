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
    
    
    



