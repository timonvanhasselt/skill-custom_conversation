from neon_utils.mq_utils import send_mq_request
from neon_utils.file_utils import decode_base64_string_to_file

with open("fysio.nct") as f:
    text = f.read()
resp = send_mq_request("/neon_script_parser", {"text": text, "meta": {}}, "neon_script_parser_input", timeout=45)

data = resp["parsed_file"]
decode_base64_string_to_file(data, "fysio.ncs")
