import logging

import dave

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s [%(pathname)s:%(lineno)d] %(message)s",
)

session = dave.Session("", "", print)
print(session)
# print(session.process_commit((12,)))

d = bytes.fromhex("0dc5aedd5bdc3f20be5697e54dd1f437b896a36f858c6f20bbd69e2a493ca170c4f0c1b9acd49d324b92afa788d09b12b29115a2feb3552b60fff983234a6c9608af3933683efc6b0f5579a9")
enc = dave.Encryptor()
enc.assign_ssrc_to_codec(0, dave.Codec.opus)
print(enc.encrypt(dave.MediaType.audio, 0, d))
