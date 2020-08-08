import morse

m = "SOS We have hit an iceberg and need help quickly"

encoded_message = morse.encode(m)

print(f"Incoming message: {m}")
print(f"   Morse encoded: {encoded_message}")