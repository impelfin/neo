import tiktoken

text = 'tiktoken is great!'
enc = tiktoken.get_encoding('cl100k_base')
# enc = tiktoken.encoding_for_model('gpt-3.5-turbo')

encoded_list = enc.encode(text)
token_num = len(encoded_list)
decode_text = enc.decode(encoded_list)

print('-' * 50)
print('- 인코딩 결과 : ', encoded_list, end='\n\n')
print('- 토큰 개수 : ', token_num, end='\n\n')
print('- 디코딩 결과 : ', decode_text, end='\n\n')