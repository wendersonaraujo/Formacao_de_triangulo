print('-=-' * 20)
print('Analisando os triangolos')
print('-=-' * 20)
s1 = float(input('primero segmento:'))
s2 = float(input('segundo segmento:'))
s3 = float(input('terceiro segmento:'))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem sim se forma um triangolo')
else:
    print('Os segmentos acima nao podem forma nenhum triangolo')