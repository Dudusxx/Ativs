total_meses = int(input("Digite a quantidade de meses: "))

anos = total_meses // 12
meses = total_meses % 12

print(f"{total_meses} meses equivalem a {anos} ano(s) e {meses} mês(es)")
